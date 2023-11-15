class Car:
    def __init__(self, model_year, price):
        self.__model_year = model_year
        self.__purchase_price = price
    def calculateCurrentValue(self, current_year):
        self.__current_year = current_year
        DEPRECIATION_RATE = 0.15
        car_age = self.__current_year - self.__model_year
        self.current_value = round(self.__purchase_price * (1 - DEPRECIATION_RATE) ** car_age)
    def print_info(self):
        print(f"Car's information: \
              \n  Model year: {self.__model_year} \
              \n  Purchase price: ${self.__purchase_price} \
              \n  Current value: ${self.current_value}")

def main():
    car = (Car(int(input("Enter the model year: ")), int(input("Enter the purchase price: "))))
    car.calculateCurrentValue(int(input("Enter the current year: ")))
    car.print_info()

main()
