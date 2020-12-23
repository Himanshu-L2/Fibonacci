endnum = int(input('Please enter your last number:'))
num1 = 0
num2 = 1
print(0)
var1=0
while (num1 < endnum) and (num2 < endnum) and (var1+num2<endnum):
    var1 = (int(num1)) + (int(num2))
    num2 = num1
    num1 = var1
    print(var1)
