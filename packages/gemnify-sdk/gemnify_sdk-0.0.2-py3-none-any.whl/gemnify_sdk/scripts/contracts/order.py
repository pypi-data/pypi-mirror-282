from gemnify_sdk.scripts.instance import ContractInstance

class Order:
    def __init__(self, config) -> None:
        self.instance = ContractInstance(config, 'OrderBook')

    def create_increase_order(self, *args, value):
        return self.instance.create_transaction("createIncreaseOrder", args, value)

    def update_increase_order(self, *args):
        return self.instance.create_transaction("updateIncreaseOrder", args)

    def cancel_increase_order(self, *args):
        return self.instance.create_transaction("cancelIncreaseOrder", args)

    def get_increase_order_index(self, *args):
        return self.instance.call_function("increaseOrdersIndex", args)

    def get_increase_order(self, *args):
        return self.instance.call_function("getIncreaseOrder", args)

    def update_decrease_order(self, *args):
        return self.instance.create_transaction("updateDecreaseOrder", args)

    def cancel_decrease_order(self, *args):
        return self.instance.create_transaction("cancelDecreaseOrder", args)

    def get_decrease_order_index(self, *args):
        return self.instance.call_function("decreaseOrdersIndex", args)

    def get_decrease_order(self, *args):
        return self.instance.call_function("getDecreaseOrder", args)

    def create_decrease_order(self, *args, value):
        return self.instance.create_transaction("createDecreaseOrder", args, value)

    def cancel_multiple(self, *args):
        return self.instance.create_transaction("cancelMultiple", args)

    def get_min_execution_fee(self):
        return self.instance.call_function("minExecutionFee")
