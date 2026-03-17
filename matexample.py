import random
import matplotlib.pyplot as plt
import numpy as np

day =np.arange(1,31)
temp =np.random.randint(20,40,30)


plt.plot(day, temp)
plt.scatter(day,temp)

max_index = np.argmax(temp)
plt.scatter(day[max_index], temp[max_index], color='red')

plt.xlabel("day")
plt.ylabel("temp in celcious")
plt.title("Temp prediction", loc='left')

plt.show()