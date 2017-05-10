import random
import numpy as np

random.seed(1)

casamentosMulheres = 70
casamentosHomens   = 25
multiplo    = 3
numHomens   = multiplo * casamentosMulheres 
numMulheres = multiplo * casamentosHomens

#
probabilities = [[] for t in xrange(numMulheres)]
for i in xrange(numMulheres):
    for j in xrange(numHomens):
        probabilities[i].append(random.randint(0,99))
    #normalize
    mySum = sum(probabilities[i])
    probabilities[i] = [int(100*round((1.0*t)/mySum,2)) for t in probabilities[i]]
    
#
print np.array(probabilities),"\n"

#objective function
print "maximize\n"
objStr = ""
for i in xrange(numMulheres):
    for j in xrange(numHomens):
        objStr += "%dx%dv%d +" % (probabilities[i][j],i+1,j+1)
objStr = objStr[:-1]
print objStr,"\n"

#subject to
print "subject to\n"
stStr = ""
for i in xrange(numMulheres):
    stStr += "xs%d" % (i+1,)
    for j in xrange(numHomens):
        stStr += " - x%dv%d" % (i+1,j+1)
    stStr += " = 0\n"

for j in xrange(numHomens):
    stStr += "x%dt" % (j+1,)
    for i in xrange(numMulheres):
        stStr += " - x%dv%d" % (i+1,j+1)
    stStr += " = 0\n"
print stStr

#bounds
print "bounds\n"
boundsStr = ""    
for i in xrange(numMulheres):
    boundsStr += "%d <= xs%d <= %d\n" % (casamentosMulheres,i+1,casamentosMulheres)
for j in xrange(numHomens):
    boundsStr += "x%dt <= %d\n" % (j+1,casamentosHomens)

for i in xrange(numMulheres):
    for j in xrange(numHomens):
        boundsStr += "x%dv%d <= 1\n" % (i+1,j+1)

print boundsStr,
#end
print "\nend"
