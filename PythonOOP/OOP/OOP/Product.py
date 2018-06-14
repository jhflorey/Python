class My_Product(object):
    def __init__(self, item_name, price, weight, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.status = status


    def sell(self):
        self.status = "Sold"
        return self

    def add_tax(self, tax):
        self.price += self.price*tax
        return self

    def return_prod(self, reason):
        if reason == 'detective':
            self.status = 'detective'
            self.price = 0
        elif reason == 'new':
            self.status = 'for sale'
        else:
            self.status = 'used'
            self.price = 0.8*self.price
        return self

    def display_info(self):
        print("Item name :  %s \nPrice : %s \nWeight :  %s \nStatus is %s" % (self.item_name, self.price, self.weight, self.status))

