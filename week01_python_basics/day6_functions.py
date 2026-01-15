#Example of defining and calling a function
def wish(name):
    print("Happy birthday, " + name + "!")

wish("Aditya")

#Example of function with return keyword
def myfunction():
  return "hello" + "there!"
  print("Hello, Aditya!")

print(myfunction())

#Median of 2 numbers
def median_of_two_numbers(a, b):
   median = (a + b) / 2
   return median
 
m = median_of_two_numbers(100, 400)
print("Median of the 2 numbers is:", m)

#To check which distribution to use based on sample size
def check_distribution(sample_size):
    if sample_size < 30:
        return "Use t-distribution"
    else:
        return "Use normal distribution"
s = check_distribution(25)
print("For the specified sample size:", s)

#To return mean and variance of numbers discretely distributed
def mean_variance(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return mean, variance

m, V = mean_variance([10, 20, 30, 40, 50])
print("Mean is:", m)
print("Variance is:", V)