x = [29, 28, 34, 31, 25] 
y = [77, 62, 93, 84, 59] 

n = len(x)

x_mean = sum(x) / n
y_mean = sum(y) / n

Sxy = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
Sxx = sum((x[i] - x_mean) ** 2 for i in range(n))

a = Sxy / Sxx  
b = y_mean - (x_mean * a) 

print(f"สมการ Regression: y = {a:.3f}  {b:.3f}")
