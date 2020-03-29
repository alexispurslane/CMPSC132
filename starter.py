# Quiz 1 - Coding Part, Spring 2020
# February, 2020


#QUESTION 1

class BadSodaMachine:
    '''
        >>> m = BadSodaMachine('Diet Coke', 10)
        >>> m.purchase()
        'Please deposit $10'
        >>> m.deposit(7)
        'Balance: $7'
        >>> m.purchase()
        'Please deposit $3'
        >>> m.deposit(5)
        'Balance: $12'
        >>> m.purchase()
        'Diet Coke dispensed, remaining balance: $2'
        >>> m.purchase()
        'Please deposit $8'
        >>> m.deposit(15)
        'Balance: $17'
        >>> m.purchase()
        'Diet Coke dispensed, remaining balance: $7'
        >>> x = BadSodaMachine('Fanta', 5)
        >>> x.deposit(7)
        'Balance: $7'
        >>> x.purchase()
        'Fanta dispensed, remaining balance: $2'
    '''

    def __init__(self, product_name, price):
        self.price = price
        self.product_name = product_name
        self.__balance = 0

    def purchase(self):
        if self.__balance >= self.price:
            self.__balance -= self.price
            return f'{self.product_name} dispensed, remaining balance: ${self.__balance}'
        else:
            return f'Please deposit ${self.price - self.__balance}'

    def deposit(self, amount):
        self.__balance += amount
        return f'Balance: ${self.__balance}'

# QUESTION 2

class Temperature:
    '''
        >>> t1 = Temperature(31, "F")
        >>> t1
        272.59 K
        >>> t2 = Temperature(662, "C")
        >>> t1 + t2
        1207.74 K
        >>> t1 = Temperature(65, "K")
        >>> t2 = Temperature(656, "F")
        >>> t1 - t2
        -554.82 K
        >>> t1 = Temperature(31, "C")
        >>> t2 = Temperature(31, "K")
        >>> t1 * t2
        9428.65 K
        >>> t1 = Temperature(55, "F")
        >>> t2 = Temperature(6725, "C")
        >>> t1 / t2
        0.04 K
        >>> t1.fahrenheit()
        55.0
        >>> t1.celsius()
        12.78
        >>> t1.kelvin()
        285.93
    '''

    def to_kelvin(val, unit):
        if unit == 'K':
            return val
        elif unit == 'C':
            return val + 273.15
        elif unit == 'F':
            return (val - 32) * (5 / 9) + 273.15

    def __init__(self, val, unit):
        self.__kelvin = round(Temperature.to_kelvin(val, unit), 2)

    def __repr__(self):
        return f'{self.__kelvin} K'

    def __eq__(self, other):
        return self.__kelvin == other.kelvin()

    def __add__(self, other):
        return Temperature(self.__kelvin + other.kelvin(), 'K')

    def __sub__(self, other):
        return Temperature(self.__kelvin - other.kelvin(), 'K')

    def __mul__(self, other):
        return Temperature(self.__kelvin * other.kelvin(), 'K')

    def __truediv__(self, other):
        return Temperature(self.__kelvin / other.kelvin(), 'K')

    def fahrenheit(self):
        return round((self.__kelvin - 273.15) * (9 / 5) + 32, 2)

    def celsius(self):
        return round(self.__kelvin - 273.15, 2)

    def kelvin(self):
        return self.__kelvin
