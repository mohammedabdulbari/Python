
class InvalidFormulaException(Exception):
    pass

def evaluate(formula):

    f = formula.split()
    if len(f) < 3:
        raise InvalidFormulaException('Formula should have SPACES ex: 10 + 5')

    if f[1] == '+' or f[1] == '-' or f[1] == '*' or f[1] == '/':
        op1 = int(f[0])
        op2 = int(f[2])
        if f[1] == '+':
            res = op1 + op2
        elif f[1] == '-':
            res = op1 - op2
        elif f[1] == '*':
            res = op1 * op2
        else:
            res = op1 / op2
        return res
    else:
        raise InvalidFormulaException('Formula should be in this form ex: 10 + 5')


try:
    formula = input('Enter the formula Ex: 10 - 4')
    print(evaluate(formula))
except InvalidFormulaException as e:
    print(e)
