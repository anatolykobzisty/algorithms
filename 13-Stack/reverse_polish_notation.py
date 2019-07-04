'''
   Обратная Польская нотация (Postfix) - алгоритм вычисления арифметических выражений в постфиксной нотации
   
   теория
   https://youtu.be/L4IU1bPKvHM?t=4150
   https://algorithmspython.wordpress.com/2013/02/01/%D1%81%D1%82%D0%B5%D0%BA-stack/
'''

expr = "2 7 + 5 *" 

ops = {
  "+": (lambda a, b: a + b),
  "-": (lambda a, b: a - b),
  "*": (lambda a, b: a * b),
  "/": (lambda a, b: a / b)
}

def eval(expr):
  tokens = expr.split()
  stack = []

  for token in tokens:
    if token in ops:
      arg2 = stack.pop()
      arg1 = stack.pop()
      result = ops[token](arg1, arg2)
      stack.append(result)
    else:
      stack.append(int(token))

  return stack.pop()

print(eval(expr))
            
            
            
            
            
    