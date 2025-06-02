class KnapSack:
    def __init__(self):
        self.stored = dict()
        self.prices = [3, 8, 0, 20] # idx=weight; value=price

    def max_value(self, max_weight):
        if max_weight == 0:
            return 0
        if max_weight < 0:
            return float('-inf')
        
        get_stored = self.stored.get(max_weight)
        if get_stored is not None:
            return get_stored
        
        maximum = float('-inf')
        for weight, value in enumerate(self.prices):
            weight += 1
            if max_weight - weight < 0:
                continue

            temp = value + self.max_value(max_weight - weight)
            if temp > maximum:
                maximum = temp
        
        self.stored[max_weight] = maximum
        return maximum


if __name__ == "__main__":
    knap = KnapSack()
    print(knap.max_value(10))