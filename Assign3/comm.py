#!/usr/bin/python

import random, sys, locale
from optparse import OptionParser

def unorderedComm(file1, file2, colBool):
    lineDict = {}
    for w in file2:
        if (not w in lineDict):
            lineDict[w] = 1
        else:
            lineDict[w] += 1
    for m in file1:
        if (m in lineDict and lineDict[m] > 0):
            lineDict[m] -=1
            printLine(colBool, 3, m)
        elif (not m in lineDict or lineDict[m] == 0):
            printLine(colBool, 1, m)
        else:
            pass
    for w in file2:
        if (lineDict[w] > 0):
            printLine(colBool, 2, w)
            lineDict[w] -= 1
            
def orderedComm(file1, file2, colBool):
    marker1=0
    marker2=0
    printed1=False
    printed2=False
    end1=len(file1)
    end2=len(file2)
    while (marker1 < end1 and  marker2 < end2):
        if (file1[marker1] == file2[marker2]):
            printLine(colBool, 3, file1[marker1])
            marker1+=1
            marker2+=1
        elif (file1[marker1] < file2[marker2]):
            
            printLine(colBool, 1, file1[marker1])        
            marker1+=1
            if (marker1 < end1 and
                locale.strcoll(file1[marker1-1],file1[marker1])>0
                and not printed1):
                print("comm: file 1 is not in sorted order")
                printed1=True
        else:
            
            printLine(colBool, 2, file2[marker2])
            marker2+=1
            if (marker2 < end2
                and locale.strcoll(file2[marker2-1],file2[marker2])>0
                and not printed2):
                print("comm: file 2 is not in sorted order")
                printed2=True
                   
    if (marker1 == end1):
       for n in range(marker2, end2):
           
           printLine(colBool, 2, file2[n])
    else:
       for n in range(marker1, end1):
          
           printLine(colBool, 1, file1[n])
    return (printed2 or printed1)
               
def printLine(colBool, col, m):
    if (col == 1 and not colBool[0]):
        print(m)
    elif (col == 2 and colBool[0] and not colBool[1]):
        print(m)
    elif (col == 2 and not colBool[0]):
        print('\t' + m)
    elif (col == 3 and colBool[0] and colBool[1] and not colBool[2]):
        print(m)    
    elif (col == 3 and (colBool[0] != colBool[1]) and not colBool[2]):
        print('t' + m)
    elif (col==3 and not colBool[0] and not colBool[1] and not colBool[2]):
        print('\t' + '\t' + m)
    else:
        pass

def main():
    version_msg = "%prog 2.0"
    usage_msg = """"""    
    
    parser = OptionParser(version=version_msg,usage=usage_msg)
    parser.add_option("-1", action="store_true", dest="clear1", default=False)
    parser.add_option("-2", action="store_true", dest="clear2", default=False)
    parser.add_option("-3", action="store_true", dest="clear3",default=False)
    parser.add_option("-u", action="store_true", dest="unoFound", default=False)
           
    options, args = parser.parse_args(sys.argv[1:])
   
    file1std=False
    file2std=False
    
    for w in range(0,len(sys.argv)):
        if (sys.argv[w] == '-' and w <len(sys.argv)-1):
            file1temp = sys.stdin
            file1std=True
        elif (sys.argv[w] == '-' and w == (len(sys.argv)-1)):
            file2temp=sys.stdin
            file2std=True
            
        else:
            pass
    
    colBool = [options.clear1, options.clear2, options.clear3]
    argCount=1
    if (options.unoFound):
        argCount+=1
    for t in sys.argv:
        if (t == '-1' or t == '-2' or t == '-3' or t == '-12'
            or t == '-13' or t == '-23' or
            t == '-21' or t == '-31' or t == '-32' or t == '-123'
            or t == '-132' or t == '-231' or
            t == '-213' or t == '-312' or t == '-321'):
            sys.argv.remove(t)
    
    if (len(sys.argv) != argCount+2):
        print("comm: extra operand " + "\'"+sys.argv[len(sys.argv)-1]+ "\'")
        sys.exit(1)

    if (options.clear1 and options.clear2 and options.clear3):
        sys.exit(0)
    
    try:
        if (file1std):
            file1=file1temp.read().splitlines()
        else:
            with open(sys.argv[len(sys.argv)-2]) as f:
                file1 = f.read().splitlines()

        if(file2std):
            file2=file2temp.read().splitlines()
        else:
            with open(sys.argv[len(sys.argv)-1]) as f:
                file2 = f.read().splitlines()
    except:
        print("comm: No such file or directory")
        sys.exit(1)

    valueBool=False
    if (options.unoFound):    
        unorderedComm(file1, file2, colBool)  
    else:
        valueBool=orderedComm(file1, file2, colBool)
        
    if (valueBool):
        sys.exit(1)
    else:
        sys.exit(0)
            
if __name__ == "__main__":
    main()
