from Product import My_Product

class Store(object):
    def __init__(self, products, location, owner):
        self.products =  products
        self.location = location
        self.owner = owner
    def add_product(self, product):
        """

        :param product: object of My_Product which you want to add
        :return:
        """
        self.products.append(product)
    def remove_product(self, removed_name):
        """
        :param removed_name: name of product which you want to remove (string type)
        :return:
        """
        copy_products = self.products[:]

        for i in range(0, len(copy_products)):
            if copy_products[i].item_name == removed_name:
                del self.products[i]

    def inventory(self):
        for product in self.products:
            product.display_info()


new_products = [My_Product('item1',25,234,'used'),
                My_Product('item2', 35, 134, 'sell')]

my_store = Store(new_products,'usa','jessica')
my_store.add_product(My_Product('item3',18,354,'detective'))
my_store.remove_product(new_products[0].item_name)
my_store.inventory()

