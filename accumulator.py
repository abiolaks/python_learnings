import time
# check the time taken to run the code
def sumOfN2(n):
    """
    
    Function to compute the sum of the first n integers.
    algorithmic approach:
    * initialize the start time
    * use the idea of an accumulator- a variable
    * initialize the accumulator to 0
    * Then iterates through the n integers, adding each integer to the accumulator
    * get the end time
    * Finally, return the value of the accumulator
    * compute the time difference between the start and end time to the time taken to run the code

    """
    start = time.time()
    theSum = 0
    for i in range(1, n+1):
         theSum = theSum + i
    end = time.time()
    return theSum, end-start

# calling the function with n =10000, for 5 invocation
for i in range(5):
    print("Sum is %d required %10.7f seconds" % sumOfN2(1000000))
def sumOfN(n):
    """
    Function to compute the sum of the first n integers.
    algorithmic approach:
    * use the idea of an accumulator- a variable
    * initialize the accumulator to 0
    * Then iterates through the n integers, adding each integer to the accumulator
    * Finally, return the value of the accumulator
    
    """
    accumulator = 0
    for i in range(1, n+1):
        accumulator = accumulator + i
    return accumulator

# calling the function
print(sumOfN(10))


# another approach to compute the sum of the first n integers
def sumOfN3(n):
    start = time.time()
    sum = (n*(n+1))/2
    end = time.time()
    return sum, end-start


for i in range(5):
    print("Sum is %d required %10.7f seconds" % sumOfN3(10000000))
# this product a consistent answer irrespective of the number of n