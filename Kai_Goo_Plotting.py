#Kai_Goo_Plotting
#1

import numpy
from numpy import log, exp
import matplotlib.pyplot as plt

#importing the numpy and matlab info
import time
#idk why, but this code only works if i import time first. Can I get some feedback on that?

#2a. dis da x values
x_100 = (-3, 3, 100)
x_10000= (-5, 5, 10000)
x_1000000: tuple[int, int, int]= (-10, 10, 1000000)
#I wanted to practice setting up the x value array two different ways, just to review that it
#works the same way, no matter how it's written, AND I REMEMEBER FROM THE LECTURE WHAT
# I learned what MAKES THEM DIFFERENT/STRICTER/LOSER


#print(x_100[0])
#I had this print function in there to double check that the x array was working


#3. Here da y values array
y_100= numpy.exp(log(x_100))
y_10000= numpy.exp(log(x_10000))
y_1000000= numpy.exp(log(x_1000000))

#print(y_100[0])
#I had this print funct to make sure that the y array was working


#4 : plotting out da 10,000 points of data
plt.plot(x_10000, y_10000, color='blue', label="10000 points")
plt.title("How long for make 10,000 and 1,000,000")
plt.plot(x_1000000, y_1000000, color='red', label="1000000 points")
plt.xlabel("Number of cycles of X")
plt.ylabel("Number of points plotted on Y")
plt.legend()
plt.grid(True)
plt.show()

#5: how long da buggah take?
start = time.time()
plt.plot(x_1000000, y_1000000, color="green", label='1000000 points')
plt.xlabel("Number of cycles of X")
plt.ylabel("Number of points plotted on Y")
plt.legend()
plt.grid(True)
plt.show()
end = time.time()
print(end - start)
