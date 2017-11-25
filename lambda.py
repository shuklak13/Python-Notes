# Lambda
f = lambda x, y : x + y
f(1,1)

# Map
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)

# Filter
fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x%2==0, fib)  # [0, 2, 8, 34]

# Reduce
lst = [1, 2, 3]
lst_sum = reduce(lambda x,y: x+y, lst)  # 6 