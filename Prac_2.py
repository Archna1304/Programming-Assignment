print("Archana Vyas 20CE157")
import numpy as np
arr = list(map(int, input().split(' ')))

minimum = min(arr)
maximum = max(arr)
mean = np.mean(arr)
Variance = float(np.var(arr))
Standard_Deviation = float(np.std(arr))

print(minimum, maximum, mean, '{:.2f}'.format(Standard_Deviation), '{:.2f}'.format(Variance))







