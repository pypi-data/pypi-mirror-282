from gemnify_sdk.scripts.instance import ContractInstance

class Liquidity:
    def __init__(self, config) -> None:
        self.config = config
        self.instance = ContractInstance(config, 'RewardRouter')

    def add_liquidity(self, *args):
        return self.instance.create_transaction("mintAndStakeUlp", args)

    def remove_liquidity(self, *args):
        return self.instance.create_transaction("unstakeAndRedeemUlp", args)

    def get_tokens_amount_out(self, *args):
        reader_instance = ContractInstance(self.config, 'Reader')
        return reader_instance.call_function("getAmountOutWhenSellUlp", args)

    def handleRewards(self, *args):
        return self.instance.create_transaction("handleRewards", args)

    def get_claimable(self, *args):
        tracker = ContractInstance(self.config, 'RewardTracker')
        return tracker.call_function("claimable", args)

    def get_user_ulp(self, *args):
        tracker = ContractInstance(self.config, 'RewardTracker')
        return tracker.call_function("depositBalances", args)

    def get_total_ulp(self, *args):
        tracker = ContractInstance(self.config, 'RewardTracker')
        return tracker.call_function("totalDepositSupply", args)
