from brownie import config, network, accounts, Contract, Factory
import requests




def deploy():
    account = accounts.add(config["wallets"]["from_key"])
    sys = Factory.deploy({"from":account})
    print("The Factory is succefuly deployed !")
    return sys

def update_add(var,add):
    variable_name = var
    new_value = add
    
    

    with open('.env', 'r') as f:
        
        lines = f.readlines()

    # Modify the line with the specified variable name
    for i, line in enumerate(lines):
        if line.startswith(f'export {variable_name} ='):
            lines[i] = f'export {variable_name} = {new_value}\n'
            break
        if line.startswith(f'export {variable_name}_abi ='):
            lines[i] = f'export {variable_name} = {Factory.abi}\n'
            break

    # Save the changes back to the .env file
    with open('.env', 'w') as f:
        f.writelines(lines)


def main():
    sys = deploy()
    update_add("factory",sys.address)