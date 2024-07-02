from gemnify_sdk.scripts.instance import ContractInstance

class Reader:
    def __init__(self, config) -> None:
        self.config = config
        self.reader = ContractInstance(config, 'Reader')
        self.vault = ContractInstance(config, 'Vault')

    def get_aum(self):
        return self.reader.call_function("getAum")

    def get_global_OI(self):
        return self.reader.call_function("getGlobalOI")

    def get_pool_info(self, *args):
        return self.vault.call_function("getPoolInfo", args)
