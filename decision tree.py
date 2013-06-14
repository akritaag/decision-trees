#decision tree classification using the best split method for attributes assuming discrete values
#coded by Akrita Agarwal

import sys,math
from xlrd import open_workbook,cellname

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
            
def main(args):
    book = open_workbook('contact_lenses_dataset.xls')
    sheet = book.sheet_by_index(0)
    data = []
    
    for row in range(0,sheet.nrows):
        a=str(sheet.cell(row,1).value)+" "+str(sheet.cell(row,2).value)+" "+str(sheet.cell(row,3).value)+" " +str(sheet.cell(row,4).value)+" "+str(sheet.cell(row,5).value)
        a = a.split()
        data.append(a)

    infogain = information_gain(data,[])

if __name__ == "__main__": main(sys.argv)
