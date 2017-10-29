import random
numlist = []
for i in range(0,20):
    numlist.append(100*random.random())   

def problem4_2(ran_list):

    """ Compute the mean and standard deviation of a list of floats """
    import statistics
    print(statistics.mean(ran_list))
    print(statistics.stdev(ran_list))