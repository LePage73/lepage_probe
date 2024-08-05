# 7 1
class Product():
    def __init__(self,*args):
        self.name = args[0]
        self.weight = args[1]
        self.category = args[2]
        pass

    def __str__(self):
        str_ = str(self.name) + ', '+ str(self.weight) + ', ' + str(self.category)
        return str(str_)

    pass


class Shop():
    def __init__(self):
        self.__file_name = 'product.txt'
        self.file = []
    def __open_file_for_read(self):
        self.file = open(self.__file_name, "r")
        pass
    def __open_file_for__app(self):
        self.file = open(self.__file_name,"a")
        pass
    def __close_file(self):
        self.file.close()
        pass
    def get_products(self):
        self.__open_file_for_read()
        str_ = self.file.read()
        self.__close_file()
        return str_
        pass
    def add(self, *args):
        for product_ in args:
            if str(product_.name) in self.get_products():
                print(f'Продукт {product_.name} уже есть в магазине')
            else:
                self.__open_file_for__app()
                self.file.write(str(product_) + '\n')
                self.__close_file()
        pass
pass

s1 = Shop()
#s1.add(Product('Potato', 50.5, 'Vegetables'))
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print('Product \n',p2) # __str__

s1.add(p1, p2, p3)

print('Get product\n',s1.get_products())