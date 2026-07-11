import numpy as np

#sigmoid function

# def sigmoid(array):
#     return 1/(1+np.exp(-array))

# a=np.arange(10)

# print(sigmoid(a))



# mean squared error

actual=np.random.randint(1,50,25)
predicted=np.random.randint(1,50,25)

# def mse(actual,predicted):
#     return np.mean((actual-predicted)**2)

# print(mse(actual, predicted))


# categorical cross entropy

# def cce(actual, predicted):
#     return -np.sum(actual*np.log(predicted))

# print(cce(actual, predicted))


# binary cross entropy

def bce(actual, predicted):
    return -np.mean(actual*np.log(predicted)+(1-actual)*np.log(1-predicted))

print(bce(actual, predicted))

