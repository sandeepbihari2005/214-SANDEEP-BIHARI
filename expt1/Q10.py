class Employee:
    def __init__(self):
        self.empid = int(input("Enter Employee ID: "))
        self.name = input("Enter Employee Name: ")
        self.basicpay = float(input("Enter Basic pay: "))
        self.ta = float(input("Enter TA: "))
        self.da = float(input("Enter DA: "))

    def calculate(self):
        self.grosspay = self.basicpay + (0.10 * self.ta) + (0.05 * self.da)

    def display(self):
        print("\nEmployee Details:")
        print("Employee ID:", self.empid)
        print("Employee Name:", self.name)
        print("Basic Pay:", self.basicpay)
        print("TA:", self.ta)
        print("DA:", self.da)
        print("Gross Pay:", self.grosspay)
e = Employee()
e.calculate()
e.display()