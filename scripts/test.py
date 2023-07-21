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


#Transaction builder 
########### CREATE POOL #####################
def createPoolTX(_question, _propositions, _img, _link):
    tx = contract.functions.createPool(_question, _propositions,_img,_link).build_transaction(
    {
     "gasPrice": w3.eth.gas_price, "from": public_add, "nonce": nonce
    }
)
    return tx 
 
########### DEFINE VOTERS #####################
def defineVotersTX(_id,_voters):
    tx = contract.functions.addvoter(_id, _voters).build_transaction(
    {
     "gasPrice": w3.eth.gas_price, "from": public_add, "nonce": nonce
    }
)
    return tx 








#API
alchemy_url = "https://polygon-mumbai.g.alchemy.com/v2/6pQg1mPZJXFmHCDGv-VElUDI-hfLoNFr"
w3 = Web3(Web3.HTTPProvider(alchemy_url))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
print(f"Connection works: {w3.isConnected()}")
nonce = w3.eth.getTransactionCount(public_add)

contract = w3.eth.contract(address=factory_add, abi=data['abi'])



################# CREATE A POOL ###############################
_question = "Is this working ? "
_propositions = ["YES !!","NOOO :("]
_link = "https://twitter.com/ObscuresNFT/status/1655310848343121922/photo/1"
_img = "https://twitter.com/BeyondPuro/status/1678794993358585856"
tx = createPoolTX(_question, _propositions,_img,_link)
signed_tx = w3.eth.account.signTransaction(tx, private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(tx_receipt)

nonce = w3.eth.getTransactionCount(public_add)


_question = "Is this still working ? "
_propositions = ["OH YEAG !!","OKHHHHHH :("]
_link = "https://twitter.com/ObscuresNFT/status/1655310848343121922/photo/1"
_img = "https://twitter.com/BeyondPuro/status/1678794993358585856"
tx = createPoolTX(_question, _propositions,_img,_link)
signed_tx = w3.eth.account.signTransaction(tx, private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(tx_receipt)

nonce = w3.eth.getTransactionCount(public_add)


_question = "What do u think about it ? "
_propositions = ["I LOVE IT !!","NAH "]
_link = "https://twitter.com/ObscuresNFT/status/1655310848343121922/photo/1"
_img = "https://twitter.com/BeyondPuro/status/1678794993358585856"
tx = createPoolTX(_question, _propositions,_img,_link)
signed_tx = w3.eth.account.signTransaction(tx, private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(tx_receipt)



################# ADD VOTERS TO A SPECIFIED POOL ###############################
#_id = 1
#_voters = ["0x52C9a652a12800Fe804dB8673d34936BaD9250E7","0x046F1019313574cf088fCB5e7D83A77959B31Cce"]
#tx = defineVotersTX(_id,_voters)
#signed_tx = w3.eth.account.signTransaction(tx, private_key)
#tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
#tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
#print(tx_receipt)















