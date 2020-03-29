#Lab #2
#Due Date: 02/07/2020, 11:59PM
########################################
#                                      
# Name:
# Collaboration Statement:             
#
########################################

class VendingMachine:
    '''
        >>> x=VendingMachine()
        >>> x.purchase(215)
        'Machine out of stock'
        >>> x.deposit(10)
        'Machine out of stock. Take your $10 back'
        >>> x.restock(215, 9)
        'Invalid item'
        >>> x.newStock(215,2.50,9)
        'Current 215 stock: 9'
        >>> x.restock(215, 16)
        'Current item stock: 25'
        >>> x.newStock(156,3,3)
        'Current 156 stock: 3'
        >>> x.getStock()
        {215: [2.5, 25], 156: [3, 3]}
        >>> x.purchase(156)
        'Please deposit $3'
        >>> x.purchase(156, 2)
        'Please deposit $6'
        >>> x.purchase(156, 4)
        'Current 156 stock: 3'
        >>> x.deposit(2)
        'Balance: $2'
        >>> x.purchase(156)
        'Please deposit $1'
        >>> x.purchase(156, 2)
        'Please deposit $4'
        >>> x.deposit(5)
        'Balance: $7'
        >>> x.purchase(156)
        'Item dispensed, take your $4'
        >>> x.getStock()
        {215: [2.5, 25], 156: [3, 2]}
        >>> x.purchase(156)
        'Please deposit $3'
        >>> x.deposit(6)
        'Balance: $6'
        >>> x.purchase(156,2)
        'Item dispensed'
        >>> x.purchase(156)
        'Item out of stock'
        >>> x.deposit(62.5)
        'Balance: $62.5'
        >>> x.purchase(215,25)
        'Item dispensed'
        >>> x.deposit(6)
        'Machine out of stock. Take your $6 back'
        >>> x.newStock(156,3,3)
        'Item already registered'
        >>> x.restock(85, 10)
        'Invalid item'
    '''
    def __init__(self):
        self.stock = {}
        self.prices = {}
        self.balance = 0

    def anyStocks(self):
        return sum(v for k, v in self.stock.items()) > 0

    def purchase(self, item, qty=1):
        if not self.anyStocks():
            return 'Machine out of stock'
        if item not in self.stock:
            return 'Invalid item'
        if self.stock[item] == 0:
            return 'Item out of stock'
        if self.stock[item] < qty:
            return f'Current {item} stock: {self.stock[item]}'
        diff = self.prices[item]*qty - self.balance
        if diff > 0:
            return f'Please deposit ${diff}'
        else:
            self.balance = 0
            self.stock[item] -= qty
            if diff < 0:
                return f'Item dispensed, take your ${-diff}'
            elif diff == 0 and self.stock[item] == 0:
                return 'Item dispensed'
            elif diff == 0:
                return f'Current {item} stock: {self.stock[item]}'

    def deposit(self, amount):
        if self.anyStocks():
            self.balance += amount
            return f'Balance: ${self.balance}'
        else:
            return f'Machine out of stock. Take your ${amount} back'

    def restock(self, item, stock):
        if item not in self.stock:
            return 'Invalid item'
        else:
            self.stock[item] += stock
            return f'Current item stock: {self.stock[item]}'

    def newStock(self, item, price, stock):
        if item in self.stock:
            return 'Item already registered'

        self.stock[item] = stock
        self.prices[item] = price
        return f'Current {item} stock: {stock}'

    def getStock(self):
        return {k: [self.prices[k], v] for k, v in self.stock.items()}

class Complex:
    '''
        >>> a=Complex(5.2,-6)
        >>> b=Complex(2,14)
        >>> a+b
        (7.2, 8i)
        >>> a-b
        (3.2, -20i)
        >>> a*b
        (94.4, 60.8i)
        >>> a/b
        (-0.368, -0.424i)
        >>> b*5
        (10, 70i)
        >>> 5*b
        (10, 70i)
        >>> 5+a
        (10.2, -6i)
        >>> a+5
        (10.2, -6i)
        >>> 5-b
        (3, -14i)
        >>> b-5
        (-3, 14i)
        >>> print(a)
        5.2-6i
        >>> print(b)
        2+14i
        >>> b
        (2, 14i)
        >>> isinstance(a+b, Complex)
        True
        >>> a.conjugate
        (5.2, 6i)
        >>> b.conjugate
        (2, -14i)
        >>> b==Complex(2,14)
        True
        >>> a==b
        False
    '''
    def __init__(self, real, imag):
        # You are not allowed to modify the constructor lol
        self.real = real
        self.imag = imag

    def __str__(self):
        r = (float(self.real).is_integer() and int(self.real)) or float(self.real)
        i = (float(self.imag).is_integer() and int(self.imag)) or float(self.imag)

        sign = '+'
        if i < 0:
            sign = ''

        tail = sign + str(i) + "i"
        if i == 0:
            tail = ''

        return str(r) + tail

    def __repr__(self):
        return f"({self.real}, {self.imag}i)"

    def __add__(self, other):
        if isinstance(other, (float, int)):
            return Complex(self.real + other, self.imag)
        elif isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Complex(self.real * other, self.imag * other)
        elif isinstance(other, Complex):
            a = self.real * other.real
            b = self.real * other.imag
            c = self.imag * other.real
            d = self.imag * other.imag
            return Complex(a - d, b + c)

    def __truediv__(self, other):
        if other == 0:
            return None
        if isinstance(other, (float, int)):
            return Complex(self.real / other, self.imag / other)
        elif isinstance(other, Complex):
            return (self * other.conjugate) / (other * other.conjugate).real

    def __sub__(self, other):
        if isinstance(other, (float, int)):
            return Complex(self.real - other, self.imag)
        elif isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)

    def __neg__(self):
        return Complex(-self.real, -self.imag)

    def __eq__(self, other):
        return isinstance(other, Complex) and self.real == other.real and self.imag == other.imag

    @property
    def conjugate(self):
        return Complex(self.real, -self.imag)

    def __radd__(self, other): return self.__add__(other)
    def __rsub__(self, other): return -self.__sub__(other)
    def __rmul__(self, other): return self.__mul__(other)
    def __rdiv__(self, other): return self.__div__(other)
