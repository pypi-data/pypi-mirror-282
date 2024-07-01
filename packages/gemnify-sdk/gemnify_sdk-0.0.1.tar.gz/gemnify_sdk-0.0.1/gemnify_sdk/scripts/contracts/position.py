from gemnify_sdk.scripts.instance import ContractInstance

class Position:
    def __init__(self, config) -> None:
        self.config = config
        self.instance = ContractInstance(config, 'PositionRouter')

    def create_increase_position(self, *args, value):
        return self.instance.create_transaction("createIncreasePosition", args, value)

    def create_decrease_position(self, *args, value):
        return self.instance.create_transaction("createDecreasePosition", args, value)

    def get_min_execution_fee(self):
        return self.instance.call_function("minExecutionFee")

    def get_position(self, *args):
        instance = ContractInstance(self.config, 'Vault')
        return instance.call_function("getPosition", args)
