#HW3
#Due Date: 03/27/2020, 11:59PM
########################################
#
# Name: Christopher Dumas
# Collaboration Statement:
#
########################################

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


class Stack:
    '''
        >>> x = Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.isEmpty()
        False
        >>> x.push(15)
        >>> x
        Top:Node(15)
        Stack:
        15
        4
        2
        >>> x.peek()
        15
        >>> x
        Top:Node(15)
        Stack:
        15
        4
        2
    '''
    def __init__(self):
        # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self.top = None
        self.count = 0

    def __str__(self):
        # YOU ARE NOT ALLOWED TO MODIFY THE THIS METHOD
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__ = __str__

    def isEmpty(self):
        return self.top is None

    def __len__(self):
        count = 0
        node = self.top
        while node is not None:
            count += 1
            node = node.next
        return count

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        node = self.top
        if node is not None:
            self.top = self.top.next
            return node.value
        else:
            return None

    def peek(self):
        if self.top is not None:
            return self.top.value
        else:
            return None


class Calculator:
    def __init__(self):
        self.__expr = None

    @property
    def getExpr(self):
        return self.__expr

    @property
    def operators(self):
        return {
            "(": 4,
            ")": 4,
            "^": 3,
            "*": 2,
            "/": 2,
            "+": 1,
            "-": 1
        }

    @property
    def argops(self):
        return ['*', '-', '+', '^', '/']  # Operators that take arguments


    def setExpr(self, new_expr):
        if isinstance(new_expr, str) and len(new_expr.strip()) > 0:
            self.__expr = new_expr
        else:
            print('setExpr error: Invalid expression')
            return None


    def isNumber(self, txt):
        if not isinstance(txt,str) or len(txt.strip()) == 0:
            print("Argument error in isNumber: " + str(txt))
            return False
        try:
            _ = float(txt.strip())
            return True
        except:
            return False

    def hasBalancedParens(self, txt):
        return txt.count("(") == txt.count(")")

    def insertMultiplication(self, tokens):
        copy = tokens[:]
        shift = 0
        for i, tok in enumerate(copy):
            prev = i >= 1 and copy[i - 1]
            cprev = i+shift >= 1 and tokens[i - 1 + shift]
            nex = i < (len(copy) - 1) and copy[i + 1]
            if tok == "(" and prev and (self.isNumber(prev) or prev == ")") and cprev != "*":
                tokens.insert(i + shift, "*")
                shift += 1
            elif tok == ")" and nex and (self.isNumber(nex) or nex == "("):
                tokens.insert(i + 1 + shift, "*")
                shift += 1
        return tokens

    def tokenize(self, txt):
        tokens = []
        token = ""
        i = 0
        for c in txt:
            ptok = i >= 1 and len(tokens) > 0 and tokens[min(i - 1, len(tokens) - 1)]
            isUnary = c == "-" and\
                (ptok and not (self.isNumber(ptok) or ptok == ")") or i == 0)\
                and (token == "" or not self.isNumber(token))
            if c in self.operators and not isUnary:
                if token != "":
                    tokens.append(token)
                    token = ""
                tokens.append(c)
                i += 1
            elif c == " ":
                if token != "":
                    i += 1
                    tokens.append(token)
                    token = ""
            elif c == "." or self.isNumber(c) or isUnary:
                i += 1
                token += c
        if token != "":
            tokens.append(token)
        return self.insertMultiplication(tokens)

    def getLexStats(self, tokens):
        # Could make this more efficient with a for loop, so we don't look twice
        # but this is more readable and i dont think this'll really be a bottleneck
        operator_count = len(list(filter(lambda x: x in self.argops, tokens)))
        number_count = len(list(filter(lambda x: self.isNumber(x), tokens)))
        return (operator_count, number_count)

    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing. Follow PEMDAS
            >>> x = Calculator()
            >>> x._getPostfix(' 2 ^        4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1*5+3^2+1+4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('    2 *       5.34        +       3      ^ 2    + 1+4   ')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix(' 2.1 *      5   +   3    ^ 2+ 1  +     4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('(2.5)')
            '2.5'
            >>> x._getPostfix ('((2))')
            '2.0'
            >>> x._getPostfix ('     2 *  ((  5   +   3)    ^ 2+(1  +4))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('  (   2 *  ((  5   +   3)    ^ 2+(1  +4)))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('  ((   2 *  ((  5   +   3)    ^ 2+(1  +4))))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('   2 *  (  5   +   3)    ^ 2+(1  +4)    ')
            '2.0 5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 *    5   +   3    ^ -2       +1  +4')
            '2.0 5.0 * 3.0 -2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix('   2 *  (  5   +   3)    ^ 2+(1  +4    ')
            >>> x._getPostfix('2*(5 +3)^ 2+)1  +4(    ')

            >>> x._getPostfix('     2 *    5   +   3    ^ -2+1  +4    ')
            '2.0 5.0 * 3.0 -2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('-2 *    5   +   3    ^ 2+1  +     4')
            '-2.0 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('-2 *    -5.3   +   3    ^ 2+1  +     4')
            '-2.0 -5.3 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2 *  +  5   +   3    ^ 2       +1  +4')
        '''
        if not isinstance(txt,str) or len(txt.strip()) == 0:
            print("Argument error in _getPostfix")
            return None
        elif not self.hasBalancedParens(txt):
            return None

        postfix_Stack = Stack()
        postfix_expression = ""

        # Go through and carry out infix -> postfix logic
        tokens = self.tokenize(txt)
        (operator_count, number_count) = self.getLexStats(tokens)
        if operator_count == 0 and number_count > 1:
            # We have an operator that takes two args, but not enough numbers
            return None
        for i, c in enumerate(tokens):
            if self.isNumber(c):
                postfix_expression += str(float(c)) + " "
            elif c in self.operators:
                if c in self.argops:
                    if i > 0 and tokens[i - 1] in self.argops+["("]:
                        # We have two operators that take args in a row
                        return None
                    if i < 1 or i + 1 >= len(tokens):
                        # We have an operator that doesn't have a second arg
                        return None
                if not postfix_Stack.isEmpty():
                    if c == "(":
                        pass  # No need for specia precidence logic
                    elif c == ")":
                        # We want to put in all of the self.operators that
                        # happened since the last opening bracket, because
                        # those were in this pair of brackets so if we're at
                        # the closing part now they need to be put BEFORE we
                        # close
                        op = postfix_Stack.pop()
                        while op is not None and op != "(":
                            postfix_expression += op + " "
                            op = postfix_Stack.pop()
                        if op is None:
                            # Didn't find an opening bracket
                            return None
                    elif self.operators[c] <= self.operators[postfix_Stack.peek()]:
                        # High precidence self.operators would have to be
                        # evaluated before this new lower one -- the lower one
                        # needs to be on the outside -- so get out all the
                        # higher ones.
                        op = postfix_Stack.pop()
                        while op is not None and self.operators[c] <= self.operators[op]:
                            if op == "(":
                                postfix_Stack.push(op)
                                break
                            postfix_expression += op + " "
                            op = postfix_Stack.pop()
                        if op is not None and op != "(":
                            postfix_Stack.push(op)
                if c != ")":
                    postfix_Stack.push(c)
        op = postfix_Stack.pop()
        while op is not None:
            postfix_expression += op + " "
            op = postfix_Stack.pop()
        return postfix_expression[0:-1]  # Chop off trailing whitespace

    @property
    def calculate(self):
        '''
            Required: calculate must call postfix
                      calculate must create and use a Stack to compute the final result as shown in the video lecture
            >>> x = Calculator()
            >>> x.setExpr('    4  +      3 -2')
            >>> x.calculate
            5.0
            >>> x.setExpr('  2  +3.5')
            >>> x.calculate
            5.5
            >>> x.setExpr('4+3.65-2 /2')
            >>> x.calculate
            6.65
            >>> x.setExpr(' 23 / 12 - 223 +      5.25 * 4    *      3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr('   2   - 3         *4')
            >>> x.calculate
            -10.0
            >>> x.setExpr(' 3 *   (        ( (10 - 2*3)))')
            >>> x.calculate
            12.0
            >>> x.setExpr(' 8 / 4  * (3 - 2.45      * (  4- 2 ^   3)) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr(' 2   *  ( 4 + 2 *   (5-3^2)+1)+4')
            >>> x.calculate
            -2.0
            >>> x.setExpr('2.5 + 3 * ( 2 +(3.0) *(5^2 - 2*3^(2) ) *(4) ) * ( 2 /8 + 2*( 3 - 1/ 3) ) - 2/ 3^2')
            >>> x.calculate
            1442.7777777777778


            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr("4++ 3 +2")
            >>> x.calculate
            >>> x.setExpr("4    3 +2")
            >>> x.calculate
            >>> x.setExpr('(2)*10 - 3*(2 - 3*2)) ')
            >>> x.calculate
            >>> x.setExpr('(2)*10 - 3*/(2 - 3*2) ')
            >>> x.calculate
            >>> x.setExpr(')2(*10 - 3*(2 - 3*2) ')
            >>> x.calculate
            >>> x.setExpr(' (3.5) ( 15 ) ')
            >>> x.calculate
            52.5
            >>> x.setExpr(' 3 ( 5 )-15 + 85 (12) ')
            >>> x.calculate
            1020.0
            >>> x.setExpr(' (-2/6)+      (5((9.4))) ')
            >>> x.calculate
            46.666666666666664


            >>> x.setExpr('     2 *    5   +   3    ^ -2+1  +4    ')
            >>> x.calculate
            15.11111111111111
            >>> x.setExpr('-2 *    5   +   3    ^ 2+1  +     4')
            >>> x.calculate
            4.0
            >>> x.setExpr(' -2 / (-4) * (3 - 2*( 4- 2^3)) + 3')
            >>> x.calculate
            8.5
            >>> x.setExpr('2 + 3 * ( -2 +(-3) *(5^2 - 2*3^(-2) ) *(-4) ) * ( 2 /8 + 2*( 3 -  1/ 3) ) - 2/ 3^2')
            >>> x.calculate
            4948.611111111111
        '''

        if not isinstance(self.__expr,str) or len(self.__expr.strip()) == 0:
            print("Argument error in calculate")
            return None

        calculator_Stack = Stack()
        expr = self._getPostfix(self.__expr)
        if expr is None:
            return None
        for c in expr.split(" "):
            if self.isNumber(c):
                calculator_Stack.push(float(c))
            elif c in self.operators:
                b = calculator_Stack.pop()
                a = calculator_Stack.pop()
                value = 0
                if c == "+":
                    value = a + b
                elif c == "-":
                    if a is None:
                        value = -b
                    else:
                        value = a - b
                elif c == "*":
                    value = a * b
                elif c == "/":
                    value = a / b
                elif c == "^":
                    value = a ** b
                calculator_Stack.push(value)
        if len(calculator_Stack) > 1:
            # Can't really check this easily at the parsing level, but super
            # easy to know when you don't have enough operators by here.
            return None
        return calculator_Stack.pop()
