y="zxsihdhis1234"
print(y)
result = 0
result1 = 0
for i in range(len(y)):
    if(y[i].isalpha()):
        result= result+1

    elif(y[i].isdigit()):
        result1 = result1+1

print(result)
print(result1)        