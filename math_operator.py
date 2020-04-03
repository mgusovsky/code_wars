def calc(expression, ans = 0):
    # Initializes with first number
    # Iteration is according to structure: find next operator, compute next number
    # If '*' or '/', do operation and continue
    # If '+' or '-' recursively calculate next number
    # Base case: when only '+', '-', and numbers are left, do all operations
    ns_exp = expression.replace(' ', '')
    ans, ns_exp = next_step(ns_exp) 
    while len(ns_exp) > 0:
        op, ns_exp = ns_exp[0], ns_exp[1:]
        num, ns_exp = next_step(ns_exp)
        while (op != '/') and (len(ns_exp) > 0):
            if (ns_exp[0] == '*') or (ns_exp[0] =='/'):
                next_op, ns_exp = ns_exp[0], ns_exp[1:]
                num2, ns_exp = next_step(ns_exp)
                num = operator(num, next_op, num2)
            else: break
        ans = operator(ans, op, num)
    return ans

# Decides the next step. Expected next character in string is:
    # number -> return number
    # '-' -> adds a (-1) then return number
    # '(' -> finds lenght of '()' and recursively runs calc())
def next_step(ns_exp, sign = 1):
    if ns_exp[0].isdigit():
        return num_reader(ns_exp, sign)
    if ns_exp[0] == '-':
        return next_step(ns_exp[1:], -1)
    if ns_exp[0] == '(':
        return parenthesys(ns_exp, sign)
                
# Reads a number
def num_reader(ns_exp, sign):
    num_str = str()
    while len(ns_exp) > 0 and ns_exp[0].isdigit(): 
            num_str += ns_exp[0]
            ns_exp = ns_exp[1:]
    return sign * int(num_str), ns_exp

# Finds length of parenthesys, recursively recalculates number value
def parenthesys(ns_exp, sign):
    par_counter, i = 1, 0
    while par_counter > 0: # Only works on valid expressions
        i += 1
        if ns_exp[i] == '(':
            par_counter += 1
        if ns_exp[i] == ')':
            par_counter += -1
    ans = sign * calc(ns_exp[1:i])
    if i == (len(ns_exp) - 1):
        return ans, list()
    return ans, ns_exp[(i+1):]
    
# Actual math operator function
def operator(num1 = 0, op = '+', num2 = 0):
    if op == '+':
        ans = num1 + num2
    elif op == '-':
        ans = num1 - num2
    elif op == '*':
        ans = num1 * num2
    elif op == '/':
        ans = num1 / num2
    else: print('Something\'s wrong :\(')
    return ans

print(calc('2 + 3 * 4 / 3 - 6 / 3 * 3 + 8'))

# tests = [
#     "1 + 1",
#     "8/16",
#     "3 -(-1)",
#     "2 + -2",
#     "10- 2- -5",
#     "(((10)))",
#     "3 * 5",
#     "-7 * -(6 / 3)"
# ]

# for i in range(len(tests)):
#     print(calc(tests[i]))