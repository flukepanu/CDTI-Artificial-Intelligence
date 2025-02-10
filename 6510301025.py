x = [29,28,34,31,25]
y = [77,62,93,84,59]

n = len(x)

x_average = sum(x) / n
y_average = sum(y) / n

Sxy = sum((x[i] - x_average) * (y[i] - y_average) for i in range(n))
Sxx = sum((x[i] - x_average) ** 2 for i in range(n))

a = Sxy / Sxx  
b = y_average - (x_average * a) 

print(f"สมการ Regression: y = {a:.3f}  {b:.3f}")