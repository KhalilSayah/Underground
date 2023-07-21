from dotenv import load_dotenv
import os
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware


#ABI's
with open("../build/contracts/Factory.json",'r') as f:
    data = json.loads(f.read())

with open("../build/contracts/Pool.json",'r') as f:
    data_pool = json.loads(f.read())

#data
with open("../scripts/dumpdata",'r') as f:
    poolsdata = json.loads(f.read())



#loading the contract add and the ABI 
load_dotenv()
factory_add = os.getenv("factory")
private_key = os.getenv("PRIVATE_KEY")
public_add = '0x52C9a652a12800Fe804dB8673d34936BaD9250E7'


#CONNECTION
alchemy_url = "https://polygon-mumbai.g.alchemy.com/v2/6pQg1mPZJXFmHCDGv-VElUDI-hfLoNFr"
w3 = Web3(Web3.HTTPProvider(alchemy_url))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
print(f"Connection works: {w3.isConnected()}")
nonce = w3.eth.getTransactionCount(public_add)

contract = w3.eth.contract(address=factory_add, abi=data['abi'])




def vote(pool,proposal):
    nonce = w3.eth.getTransactionCount(public_add)

    pool_contract = w3.eth.contract(address=pool, abi=data_pool['abi'])
    tx = pool_contract.functions.vote(proposal).build_transaction(
    {
     "gasPrice": w3.eth.gas_price, "from": public_add, "nonce": nonce
    })
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(tx_receipt)




test_pool = poolsdata[0]['address']

########### DEFINE VOTERS #####################
def defineVotersTX(_id,_voters):
    tx = contract.functions.addvoter(_id, _voters).build_transaction(
    {
     "gasPrice": w3.eth.gas_price, "from": public_add, "nonce": nonce
    }
)
    return tx 

################# ADD VOTERS TO A SPECIFIED POOL ###############################
_id = 0
_voters = ["0x52C9a652a12800Fe804dB8673d34936BaD9250E7","0x046F1019313574cf088fCB5e7D83A77959B31Cce"]
tx = defineVotersTX(_id,_voters)
signed_tx = w3.eth.account.signTransaction(tx, private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(tx_receipt)

vote(test_pool,0)


