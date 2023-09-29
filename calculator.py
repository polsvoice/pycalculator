expression = input("Enter your math expression: ")
expression = expression.replace(" ", "")

if "+" in expression:
  y = expression.split("+")
  total = int(y[0]) + int(y[1])
elif "-" in expression:
  y = expression.split("-")
  total = int(y[0]) - int(y[1])
elif "*" in expression:
  y = expression.split("*")
  total = int(y[0]) * int(y[1])
elif "/" in expression:
  y = expression.split("/")
  total = int(y[0]) / int(y[1])
print(total)