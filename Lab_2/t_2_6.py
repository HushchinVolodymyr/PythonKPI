class Node:
    def __init__(self, code_product, price, amount = 0):
        self.left = None
        self.right = None
        self.code_product = code_product
        self.price = price
        self.amount = amount


class Binary_Tree:
    def __init__(self):
        self.root = None

    def add_product(self, node):
        if self.root is None:
            self.root = node
        else:
            product = self.root
            fl = True

            while fl:
                if node.code_product < product.code_product:
                    if product.left is None:
                        product.left = node
                        fl = False
                    else:
                        product = product.left
                else:
                    if product.right is None:
                        product.right = node
                        fl = False
                    else:
                        product = product.right

    def find_product(self, code_product):
        product = self.root

        while product.code_product != code_product:
            if code_product < product.code_product:
                product = product.left
            else:
                product = product.right
        
        return product

    def count_price(self):
        queue = [self.root]
        count_price = 0 

        while len(queue):
            product = queue.pop()
            if product.left:
                queue.append(product.left)
            if product.right:
                queue.append(product.right)

            count_price += product.price * product.amount
        
        return count_price
