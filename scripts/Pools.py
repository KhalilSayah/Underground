from dotenv import load_dotenv
import os
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware





#loading the contract add and the ABI 
load_dotenv()
factory_add = os.getenv("factory")
private_key = os.getenv("PRIVATE_KEY")
public_add = '0x52C9a652a12800Fe804dB8673d34936BaD9250E7'

with open("../build/contracts/Factory.json",'r') as f:
    data = json.loads(f.read())

with open("../build/contracts/Pool.json",'r') as f:
    data_pool = json.loads(f.read())

#API
alchemy_url = "https://polygon-mumbai.g.alchemy.com/v2/6pQg1mPZJXFmHCDGv-VElUDI-hfLoNFr"
w3 = Web3(Web3.HTTPProvider(alchemy_url))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
print(f"Connection works: {w3.isConnected()}")
nonce = w3.eth.getTransactionCount(public_add)

contract = w3.eth.contract(address=factory_add, abi=data['abi'])

pools_array_length = contract.functions.getPoolsLength().call()

# Access individual elements of the 'pools' array
pools_array_elements = []
for i in range(pools_array_length):
    pool_element = {
        "address": contract.functions.pools(i).call(),
        "id": i
    }
    pools_array_elements.append(pool_element)

print(pools_array_elements)


def getdata(dictpool):
    pool = dictpool['address']
    pool_contract = w3.eth.contract(address=pool, abi=data_pool['abi'])
    proposal_array_length = pool_contract.functions.getProposalsLength().call()

    # Access individual elements of the 'proposals' array
    proposals_array_elements = []
    for i in range(proposal_array_length):
        proposal_element = pool_contract.functions.proposals(i).call()
        proposals_array_elements.append(proposal_element)

    print(proposals_array_elements )

    pool_question = pool_contract.functions.question().call()
    print(pool_question)
    pool_image = pool_contract.functions.img_ipfs().call()
    pool_link= pool_contract.functions.link().call()

    return {
        "address" : pool,
        "id" : dictpool['id'],
        "data":{
            "question" :pool_question,
            "proposals":proposals_array_elements,
            "image": pool_image,
            "link": pool_link
        }
    }

dump_data = []
for pool in pools_array_elements:
    pool_data = getdata(pool)
    dump_data.append(pool_data)


with open('dumpdata','w') as f:
    f.write(json.dumps(dump_data))



