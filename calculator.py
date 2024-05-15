class Calculate():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))
cal = Calculate(a, b)
while True:
    def options():
        x = "1. Add \n2. Sub \n3. Multiply \n4. Divide"
        print(x)
    options()

    choice = int(input("Please choose one of the following : "))
    if choice == 1:
        print("Result: ", cal.add())
        break
    elif choice == 2:
        print("Result: ", cal.sub())
        break
    elif choice == 3:
        print("Result: ", cal.multiply())
        break
    elif choice == 4:
        print("Result: ", cal.divide())
        break
    else:
        print("Invalid option")
        break