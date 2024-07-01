from gemnify_sdk.scripts.utils import default_chain

class Config:
    def __init__(self, chain = default_chain):
        self.chain = chain
        self.rpc = None
        self.private_key = None
        self.chain_name = "arbitrum-sepolia"
        self.logger_level = "fatal"

    def set_rpc(self, value):
        self.rpc = value

    def set_chain_name(self, value):
        self.chain_name = value

    def set_logger_level(self, value):
        self.logger_level = value

    def set_private_key(self, value):
        self.private_key = value