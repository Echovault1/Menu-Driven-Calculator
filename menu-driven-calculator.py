def add(a,b): return a + b 
def sub(a,b) : return a - b
def mul(a,b): return a*b
def div(a,b): return a/b if b!= 0 else None

OPS = {"+" : add , "-" : sub, "*":mul, "/" : div}

def calculate (a, op, b):
    fn = OPS.get(op)
    if fn is None:
        return "Please enter a valid operator"
    result  = fn(a,b)
    return "Division by zero" if result is None else result


#Test case 1
#samples  = [(4, "+", 5), (10,"-", 3), (6, "*", 4),(8,"/",2),(9,"/", 0)]

a = float(input("Enter first number : "))
op = input("Enter operator(+,-,*,/) :  ")
b = float(input("Enter second number : "))

print(f"{a} {op} {b} = {calculate(a,op, b)}")

#for a, op, b in samples:
   # print(f"{a} {op} {b} = {calculate(a, op, b)}")
