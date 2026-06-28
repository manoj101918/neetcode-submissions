class StockSpanner:

    def __init__(self):
        self.stock=[]
        

    def next(self, price: int) -> int:
        self.stock.append(price)
        c=0
        if self.stock:
            for i in range(len(self.stock)-1,-1,-1):
                if self.stock[i]<=price:
                    c+=1
                else:
                    break
        else:
            return 1
        return c

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)