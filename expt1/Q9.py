class Product:
    def input(self):
        self.product_no = input("Enter the product number: ")
        self.product_name = input("Enter the product name: ")
        self.cost = float(input("Enter the cost of the product: "))
        self.quantity = int(input("Enter the quantity of the product: "))

    def calculate(self):
        self.total_amount = self.cost * self.quantity

    def display(self):
        print("Product Number:", self.product_no)
        print("Product Name:", self.product_name)
        print("Cost of the Product:", self.cost)
        print("Quantity of the Product:", self.quantity)
        print("Total Amount:", self.total_amount)



products = []

for i in range(5):
    print("\nEnter product", i + 1)
    p = Product()
    p.input()
    p.calculate()
    products.append(p)

highest_product = products[0]

for p in products:
    if p.total_amount > highest_product.total_amount:
        highest_product = p

print("\nProduct with the highest total amount:")
highest_product.display()