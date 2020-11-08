import json
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import scipy.integrate as integrate

with open("stepinator.json", "r") as f:
	data = json.load(f)

result = integrate.cumtrapz(data, initial=0)

fig, axs = plt.subplots(2)

loc = plticker.MultipleLocator(base=5)

axs[0].set_title("Acceleration")
axs[1].set_title("Velocity")

axs[0].xaxis.set_major_locator(loc)
axs[1].xaxis.set_major_locator(loc)

axs[0].plot(data)
axs[1].plot(result)

for x in  range(0, 185, 30):
    axs[0].axvline(x=x)
    axs[1].axvline(x=x)

plt.show()
