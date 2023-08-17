from web3 import Web3
from solcx import compile_source


class BlockchainManager:

    def __init__(self, contract_address, private_key):
        self.web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
        self.contract_address = contract_address
        self.private_key = private_key

    def connect_to_network(self):
        self.web3.isConnected()

    def send_transaction(self, to_address, value):
        self.web3.eth.sendTransaction({'to': to_address, 'from': self.web3.eth.accounts[0], 'value': value})

    def read_data(self, contract_address):
        self.web3.eth.getBalance(contract_address)

    def manage_gas_fees(self):
        self.web3.eth.gasPrice