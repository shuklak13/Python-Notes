""" Closures are functions returned by other functions
    this can be used to create customizable templates for functions """

def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)    #this is a closure
print(multiplywith5(9)) # returns 45