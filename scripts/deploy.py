from brownie import accounts, config, SmartNodes
from dotenv import load_dotenv
import json

# load_dotenv("..")

def main():
    account = accounts[0]
    erc20 = SmartNodes.deploy({"from": account})

    erc20.createValidator(
        "21c99fa3c263570d20132c24ef1b347e1b8afcdcfe88c303fb1f45b84b387a5b",
        {"from": accounts[0]}
    )
    erc20.createValidator(
        "dd24f40e6f597f435fcda42465ce0ee8e59ca4ee06ec7681bb251885bb959b3d",
        {"from": accounts[1]}
    )
    erc20.createValidator(
        "bd9e075b31d32220361afe2e0bf4e863700d25189a7f406847aae82ef39429ea",
        {"from": accounts[2]}
    )