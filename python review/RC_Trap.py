class Buy:
    #  Liquidation variables
    leverage_liquidation_prices = 0.0  # first liquidation price
    liquidation = 5  # first liquidation value is 500%
    divider_value = 0.1  # divider of liquidation value
    limit_value = 0.0000000000000001  # limit of float liquidation price value
    end_limit_counter = 100000000000000000000000000000000000  # end limit of counter value
    counter_value = 0.00000000000000000000001  # counter value for calculate liquidation
    counter = 0

    #  Lists
    assets_list = []
    liquidations_list = []
    positions_list = []
    crypto_assets_list = []
    crypto_assets_total_list = []
    positions_base_list = []
    percentage_profit_list = []
    positions_value_list = []
    levels_profit_list = []
    levels_commission_list = []
    stop_price_list = []
    real_liquidation_price_list = []
    leverage_liquidations_list = []

    #  Different Levels Calculated
    crypto_different_levels_value = 0.0

    # Commission for USD$-M
    maker_usd_m = float(0.0002)  # Maker Commission
    taker_usd_m = float(0.0004)  # Taker Commission

    def __init__(self, price, asset, leverage, percentage, target_price):
        self.price = float(price)
        self.asset = float(asset)
        self.leverage = leverage
        self.percentage = float(percentage)
        self.target_price = float(target_price)
        self.total_asset = float((self.asset * self.leverage))
        self.calculator()

    def asset_divider(self, divider_a=4, divider_b=3):
        asset5 = (self.total_asset - (self.total_asset / divider_a))
        asset4 = (asset5 / divider_a)
        asset3 = (asset4 / divider_a)
        asset2 = (asset3 / divider_a)
        asset1 = (asset2 / divider_b)
        self.assets_list = [asset1, asset2, asset3, asset4, asset5]

    def liquidation_divider(self, divider_a=2):
        liquid5 = self.liquidation
        liquid4 = (liquid5 / divider_a)
        liquid3 = (liquid4 / divider_a)
        liquid2 = (liquid3 / divider_a)
        liquid1 = (liquid2 / divider_a)
        self.liquidations_list = [liquid1, liquid2, liquid3, liquid4, liquid5]

    def position_divider(self):
        level4_buy = (self.price - (self.price * self.percentage))
        perc_up = (1 / (1 - (self.liquidation / 2)))
        start = (level4_buy * perc_up)
        level5 = (start - (start * self.liquidations_list[4]))
        level4 = (start - (start * self.liquidations_list[3]))
        level3 = (start - (start * self.liquidations_list[2]))
        level2 = (start - (start * self.liquidations_list[1]))
        level1 = (start - (start * self.liquidations_list[0]))
        self.positions_list = [level1, level2, level3, level4, level5]

    def crypto_assets(self, divider_a=4, divider_b=3):
        crypto_asset1 = (self.assets_list[0] / self.positions_list[0])
        crypto_asset2 = (crypto_asset1 * divider_b)
        crypto_asset3 = (crypto_asset2 * divider_a)
        crypto_asset4 = (crypto_asset3 * divider_a)
        crypto_asset5 = (crypto_asset4 * divider_a)
        self.crypto_assets_list = [crypto_asset1, crypto_asset2, crypto_asset3, crypto_asset4, crypto_asset5]

    def crypto_assets_total(self):
        level1 = self.crypto_assets_list[0]
        level2 = (self.crypto_assets_list[1] + level1)
        level3 = (self.crypto_assets_list[2] + level2)
        level4 = (self.crypto_assets_list[3] + level3)
        level5 = (self.crypto_assets_list[4] + level4)
        self.crypto_assets_total_list = [level1, level2, level3, level4, level5]

    def crypto_different_levels(self):
        self.crypto_different_levels_value = ((self.crypto_assets_list[1] + self.crypto_assets_list[0])
                                              / self.crypto_assets_list[0])

    def position_base(self):
        base1 = self.positions_list[0]
        base2 = (((base1 - self.positions_list[1]) / self.crypto_different_levels_value) + self.positions_list[1])
        base3 = (((base2 - self.positions_list[2]) / self.crypto_different_levels_value) + self.positions_list[2])
        base4 = (((base3 - self.positions_list[3]) / self.crypto_different_levels_value) + self.positions_list[3])
        base5 = (((base4 - self.positions_list[4]) / self.crypto_different_levels_value) + self.positions_list[4])
        self.positions_base_list = [base1, base2, base3, base4, base5]

    def percentage_profit(self, num_p=1):
        per_profit1 = ((self.target_price / self.positions_base_list[0]) - num_p)
        per_profit2 = ((self.target_price / self.positions_base_list[1]) - num_p)
        per_profit3 = ((self.target_price / self.positions_base_list[2]) - num_p)
        per_profit4 = ((self.target_price / self.positions_base_list[3]) - num_p)
        per_profit5 = ((self.target_price / self.positions_base_list[4]) - num_p)
        self.percentage_profit_list = [per_profit1, per_profit2, per_profit3, per_profit4, per_profit5]

    def position_value(self):
        value1 = (self.crypto_assets_total_list[0] * self.positions_base_list[0])
        value2 = (self.crypto_assets_total_list[1] * self.positions_base_list[1])
        value3 = (self.crypto_assets_total_list[2] * self.positions_base_list[2])
        value4 = (self.crypto_assets_total_list[3] * self.positions_base_list[3])
        value5 = (self.crypto_assets_total_list[4] * self.positions_base_list[4])
        self.positions_value_list = [value1, value2, value3, value4, value5]

    def levels_profit(self):
        lv_profit1 = (self.positions_value_list[0] * self.percentage_profit_list[0])
        lv_profit2 = (self.positions_value_list[1] * self.percentage_profit_list[1])
        lv_profit3 = (self.positions_value_list[2] * self.percentage_profit_list[2])
        lv_profit4 = (self.positions_value_list[3] * self.percentage_profit_list[3])
        lv_profit5 = (self.positions_value_list[4] * self.percentage_profit_list[4])
        self.levels_profit_list = [lv_profit1, lv_profit2, lv_profit3, lv_profit4, lv_profit5]

    def levels_commission(self):
        coms1 = ((self.positions_list[0] * self.crypto_assets_list[0]) * self.maker_usd_m)
        coms2 = ((self.positions_list[1] * self.crypto_assets_list[1]) * self.maker_usd_m)
        coms3 = ((self.positions_list[2] * self.crypto_assets_list[2]) * self.maker_usd_m)
        coms4 = ((self.positions_list[3] * self.crypto_assets_list[3]) * self.maker_usd_m)
        coms5 = ((self.positions_list[4] * self.crypto_assets_list[4]) * self.maker_usd_m)
        cost4 = (coms1 + coms2 + coms3 + coms4)
        cost5 = (coms1 + coms2 + coms3 + coms4 + coms5)
        self.levels_commission_list = [coms1, coms2, coms3, coms4, coms5, cost4, cost5]

    def stop_price(self, num_p=1):
        stop = (self.positions_base_list[3] * (num_p - (num_p / self.leverage)))
        lost = ((((self.positions_base_list[3] - stop) * self.crypto_assets_total_list[3])
                 + self.levels_commission_list[5]) + ((self.crypto_assets_total_list[3] * stop) * self.maker_usd_m))
        percentage_lost = lost / self.asset
        remainder = self.asset - lost
        self.stop_price_list = [stop, lost, percentage_lost, remainder]

    def leverage_liquidation_price(self, num_p=1):
        self.leverage_liquidation_prices = (self.positions_base_list[4] * (num_p - (num_p / self.leverage)))

    def real_liquidation_price(self):
        different_level5 = (self.positions_base_list[4] - self.positions_list[4])  # different between base5 and level5
        my_full_assets = (self.positions_base_list[4] * self.crypto_assets_total_list[4])  # assets($) with leverage
        coms_full_assets = (my_full_assets * self.taker_usd_m)  # all commission I will give until liquidation price
        real_liquid = (((self.crypto_assets_total_list[4] * different_level5) + coms_full_assets)
                       + self.levels_commission_list[6])  # Real Liquidation Price with all commissions and leverage
        different = float(self.asset - real_liquid)  # different between my assets and liquidated assets

        self.real_liquidation_price_list = [different_level5, coms_full_assets, real_liquid, different]

    def calculator(self):
        while True:
            self.asset_divider()
            self.liquidation_divider()
            self.position_divider()
            self.crypto_assets()
            self.crypto_assets_total()
            self.crypto_different_levels()
            self.position_base()
            self.percentage_profit()
            self.position_value()
            self.levels_profit()
            self.levels_commission()
            self.stop_price()
            self.leverage_liquidation_price()
            self.real_liquidation_price()

            self.counter += 1
            if self.real_liquidation_price_list[3] < self.limit_value:
                self.liquidation -= self.divider_value
                self.counter_value += self.counter_value
                if self.counter_value > self.end_limit_counter:
                    break
            elif self.real_liquidation_price_list[3] > self.limit_value:
                self.liquidation += self.divider_value
                self.divider_value /= 10

    def calculator_liquidation_range(self, start=1, end=101):
        for i in range(start, end):
            self.leverage = i
            self.total_asset = float((self.asset * self.leverage))
            liquidator = Buy(self.price, self.asset, self.leverage, self.percentage, self.target_price)
            self.leverage_liquidations_list.append(liquidator.liquidation)


# price01 = 19800
# asset01 = 25
# leverage01 = 100
# percentage01 = 0.03
# target_price01 = 19800

# buy01 = Buy(price01, asset01, leverage01, percentage01, target_price01)
# buy01.calculator_liquidation_range()

# **********************************
# print(asset01)
# print(buy01.total_asset)
# print(buy01.assets_list)
# print(buy01.liquidations_list)
# print(buy01.positions_list)
# print(buy01.crypto_assets_list)
# print(buy01.crypto_assets_total_list)
# print(buy01.crypto_different_levels_value)
# print(buy01.positions_base_list)
# print(buy01.percentage_profit_list)
# print(buy01.positions_value_list)
# print(buy01.levels_profit_list)
# print(buy01.levels_commission_list)
# print(buy01.stop_price_list)
# print(buy01.leverage_liquidation_prices)
# print(buy01.real_liquidation_price_list)
# print(buy01.leverage_liquidations_list)
# **********************************
