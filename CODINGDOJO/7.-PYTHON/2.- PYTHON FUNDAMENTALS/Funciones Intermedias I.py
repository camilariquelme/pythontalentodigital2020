import random
def randInt(min=  50 , max=  500):
    num = random.random()
    return num
print(randInt(min=50, max=500))





#print(randInt()) 		    # should print a random integer between 0 to 100 0.30463387599337255
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50 0.3583766444598162
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100 0.2000901293614007
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500 0.544777228798777
