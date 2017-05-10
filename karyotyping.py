import random
import numpy as np

random.seed(1)

numClasses = 10
numChromossomes = 20

#
probabilities = [[] for t in xrange(numChromossomes)]
for i in xrange(numChromossomes):
    for j in xrange(numClasses):
        probabilities[i].append(random.randint(0,99))
    #normalize
    mySum = sum(probabilities[i])
    probabilities[i] = [int(100*round((1.0*t)/mySum,2)) for t in probabilities[i]]
    
#
print np.array(probabilities),"\n"

#objective function
print "maximize\n"
objStr = ""
for i in xrange(numChromossomes):
    for j in xrange(numClasses):
        objStr += "%dx%dv%d +" % (probabilities[i][j],i+1,j+1)
objStr = objStr[:-1]
print objStr,"\n"

#subject to
print "subject to\n"
stStr = ""
for i in xrange(numChromossomes):
    stStr += "xs%d" % (i+1,)
    for j in xrange(numClasses):
        stStr += " - x%dv%d" % (i+1,j+1)
    stStr += " = 0\n"

for j in xrange(numClasses):
    stStr += "x%dt" % (j+1,)
    for i in xrange(numChromossomes):
        stStr += " - x%dv%d" % (i+1,j+1)
    stStr += " = 0\n"
print stStr

#bounds
print "bounds\n"
boundsStr = ""    
for i in xrange(numChromossomes):
    boundsStr += "1 <= xs%d <= 1\n" % (i+1,)
for j in xrange(numClasses):
    boundsStr += "x%dt <= 2\n" % (j+1,)
print boundsStr,
#end
print "\nend"
