def edgeTO(a,b):
    return str(a) + "_" + str(b)

str1 = 'ATG'
length1 = len(str1)
str2 = 'GCTA'
length2 = len(str2)
alpha = 10
beta  = 5
gij   = 3
cost = {'AA':0 ,'AC':3,'AG':5,'AT':7,
        'CA':20,'CC':0,'CG':9,'CT':2,
        'GA':30,'GC':5,'GG':0,'GT':3,
        'TA':15,'TC':9,'TG':8,'TT':0}


f = open('out.lp','w')
print 'minimize'

obj = ''

for row in xrange(length1):
    for col in xrange(length2):
        #horizontal
        n1 = str(row)+ '_' + str(col)
        n2 = str(row)+ '_' + str(col+1)
        obj += str(beta) + 'xh' + str(n1) + ' + '
        #vertical
        n1 = str(row)+ '_' + str(col)
        n2 = str(row+1)+ '_' + str(col)
        obj += str(alpha) + 'xv' + str(n1) + ' + '
        #diagonal
        n1 = str(row)+ '_' + str(col)
        n2 = str(row+1)+ '_' + str(col+1)
        obj += str(cost[str1[row]+str2[col]]) + 'xd' + str(n1) + "+"
print obj[:-1]

#subject to
print "subject to";
print("xh0_0 + xv0_0 + xd0_0 = 1")
print("-xh" + edgeTO(length1,length2-1)+ " - " + "xv" + edgeTO(length1-1,length2) + "- xd" + edgeTO(length1-1,length2-1)+ " = -1")

for row in xrange(length1+1):
    for col in xrange(length2+1):
        if row == 0 and col == 0:
            continue
        if row == length1 and col == length2:
            continue
        #horizontal constraint
        if row == length1:
            if  col == 0:
                print "y" + edgeTO(row,col) + ": " + "xh%d_%d - xv%d_%d" % (row,col,row-1,col) + " = 0"
            else:
                print "y" + edgeTO(row,col) + ": " + "xh%d_%d - xh%d_%d - xv%d_%d - xd%d_%d" % (row,col,row,col-1,row-1,col,row-1,col-1) + " = 0"            
        elif col == length2:
            if row == 0:
                print "y" + edgeTO(row,col) + ": " + "xv%d_%d - xh%d_%d" % (row,col,row,col-1) + " = 0"
            else:
                print "y" + edgeTO(row,col) + ": " + "xv%d_%d - xh%d_%d - xv%d_%d - xd%d_%d" % (row,col,row,col-1,row-1,col,row-1,col-1) + " = 0"
        elif row == 0:
            print "y" + edgeTO(row,col) + ": " + "xh%d_%d + xv%d_%d + xd%d_%d - xh%d_%d" % (row,col,row,col,row,col,row,col-1) + " = 0"
        elif col == 0:
            print "y" + edgeTO(row,col) + ": " + "xh%d_%d + xv%d_%d + xd%d_%d - xv%d_%d" % (row,col,row,col,row,col,row-1,col) + " = 0"
        else:
            hc = "xh%d_%d - xh%d_%d" % (row,col,row,col-1)        
            #vertical constraint
            vc = "xv%d_%d - xv%d_%d" % (row,col,row-1,col)
            #diganoal constraint
            dc = "xd%d_%d - xd%d_%d" % (row,col,row-1,col-1)
            print "y" + edgeTO(row,col) + ": " + hc + " + " + vc + " + " + dc + " = 0"
#
print "end"

