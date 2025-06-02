class CoinChange:
    def __init__(self):
        self.stored = dict()
        self.coins = [25, 20, 10, 5, 2, 1]

    def get_min_coins(self, value):
        if value <= 0:
            return 0
        
        min_coins = self.stored.get(value)
        if min_coins is not None:
            return min_coins
        
        min_count = float('inf')
        for i in self.coins:
            if value - i < 0:
                continue
            temp_count = 1 + self.get_min_coins(value - i)
            if temp_count < min_count:
                min_count = temp_count
        
        self.stored[value] = min_count
        return min_count


if __name__ == "__main__":
    coin_change = CoinChange()
    print(coin_change.get_min_coins(49))