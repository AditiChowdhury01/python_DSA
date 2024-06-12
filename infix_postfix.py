output =[]
operator =[]
priority={'(':0,'+':1,'-':1,'*':2,'/':2,'^':3}
exp = input("enter the expression:")
for item in exp:
    if (item=='('):
        operator.append(item)
    elif (item==')'):
        while (operator[-1]!='('):
            ele = operator.pop()
            output.append(ele)
        operator.pop()
    elif(item=='^' or item=='*' or item=='/' or item=='+' or item=='-'):
        if(len(operator)>0):
            while(priority[operator[-1]]>=priority[item]):
                ele = operator.pop()
                output.append(ele)
                if(len(operator)==0):
                    break
        operator.append(item)
    else:
        output.append(item)
while(len(operator)!=0):
    ele = operator.pop()
    output.append(ele)

print("the infix expression:",exp)
print("the postfix expression:",end=" ")
for ele in output:
    print(ele,end="")