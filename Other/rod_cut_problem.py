class RodCut:
    def __init__(self):
        self.prices = dict()

    def rod_cut(self, lenght, price):
        if lenght == 0:
            return 0
        
        price_stored = self.prices.get(lenght)
        if price_stored is not None:
            return price_stored
        
        max = float('-inf')
        for i in range(1, lenght+1):
            temp = price[i] + self.rod_cut(lenght-i, price)
            if temp > max:
                max = temp
        
        self.prices[lenght] = max
        return max


if __name__ == "__main__":
    rod_prices = [0, 0, 1.9, 2.2, 0, 4.5, 0, 0, 0, 0, 0, 0, 0, 0]
    rod_lenght = 10
    rod_cutter = RodCut()
    print(rod_cutter.rod_cut(rod_lenght, rod_prices))
    print(rod_cutter.prices)
    

