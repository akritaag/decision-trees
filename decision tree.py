#decision tree classification using the best split method for attributes assuming discrete values
#Copyright 2013 Akrita Agarwal

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#Akrita Agarwal, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys,math

count = 0

def newdata(data,split,clas):
    newdata = []
    for d in data:
        if str(d[-1]) == clas:
            continue
        else:
            for v in range(0,len(d)):
                if v!=split:
                    if v==0:
                        temp = str(d[v])
                    else:
                        temp = temp+" "+str(d[v])
            temp = temp.split()
            newdata.append(temp)
    data = newdata
    return data

def information(data):
    classes = dict()
    count = 0
    info = 0
    for d in data[1:]:
        c = str(d[-1])
        if c not in classes:
            classes[c] = 1
        else :
            classes[c] = classes[c] + 1
        count = count + 1

    for c in classes:
         temp = float(classes[c]/float(count))
         classes[c] = -temp * math.log(temp)/math.log(2)
         info = info + classes[c]

    return info,classes

def information_gain(data,tree):
    values = dict()
    cols = len(data[0])
    best_split = dict()
    ig = [0 for x in range(0,cols)]
    temp = 0
    exp = 0
    split_a = 0
    best_ig = 0.0000001 #randomly assumed
    info,classes = information(data)
    for i in range(0,cols):
        for d in data[1:]:
            v = str(d[i])
            if v not in values:
                values[v] = 1
            else:
                values[v] = values[v] + 1
        for v in values:
            for d in data[1:]:
                datav = str(d[i])
                if datav==str(v):
                    a = str(d[-1])
                    classes[a] = classes[a]+1

            for c in classes:
                exp = float(classes[c]/float(values[v]))
                if exp != 0:
                    a = -exp * math.log(exp)/math.log(2)
                else :
                    a = 0
                temp = a + temp
                classes[c] = 0
            temp = temp * float(values[v]/float(len(data)))
            ig[i] = ig [i] + temp
            temp = 0
            
    for i in range(0,cols-1) :
        new_ig = float(info) - ig[i]
        if new_ig > best_ig:
            split_a = i
            best_ig = new_ig

    for c in classes:
        classes[c] = 0
    val = []
    values = []
    check = []
    for d in data[1:]:    
        v = str(d[split_a])+" "+str(d[-1])
        v = v.split()
        if str(d[split_a]) not in check:
            check.append(d[split_a])
        if v not in values:
                values.append(v)

    for v in values:
        val.append(v[0])

    split_tuple = []
    for v in values:
        if val.count(v[0]) == 1:
            split_tuple = data[0][split_a],v[0],v[1]
            print(split_tuple)
            tree.append(split_tuple)
            data = newdata(data,split_a,v[1])
            break

    cl = []
    for d in data[1:]:
        if str(d[-1]) not in cl:
            cl.append(str(d[-1]))
            
    if len(cl)>1:
        information_gain(data,tree)

    else:
        print('\n')
        for t in tree:
            print(str(t[0])+" ---("+str(t[1])+")---->" +str(t[2]))
            print("    |")
            print("    v")
        for c in classes:
            if str(t[2]) not in c:
                print("  "+str(c))

# File I/O function
def fileOpen(filename):
    f=open(filename) 
    data=[]
    for line in f:
        data.append(line.splitlines())    
    return data
            
def main(args):
    data = []
    dataIn = fileOpen("contact_lenses_dataset.csv")
    
    for i in dataIn:
        data.append(i[0].split(','))
    for i in data:
        del(i[0])

    infogain = information_gain(data,[])

if __name__ == "__main__": main(sys.argv)

