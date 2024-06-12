operator = ['+','-','/','*','^']
operand=[]
exp = input("enetr the expression:")
expression = exp.split(' ')
for item in exp:
    if(item not in operator):
        operand.append(item)
    else:
        num1 = eval(operand.pop())
        num2 = eval(operand.pop())
        if (item=='+'):
            res = num1+num2
        elif (item=='-'):
            res = num2-num1
        elif (item=='*'):
            res = num1*num2
        elif (item=='/'):
            res = num2/num1
        elif (item=='^'):
            res = num2**num1
        operand.append(str(res))
print("the answer is",operand[-1])