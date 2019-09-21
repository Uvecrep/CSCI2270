# My code is split into labelled sections, compiled into a single .py file for
# the submission. To run the code please comment out all but one section at a
# time. Thank you.
#Credit:
# Miked98 on blogspot.com - used reference to his reservoir sampling in perl to do random sampling in python
# Mode.com - for reference on how to construct histograms using pandas library
# Pandas.pydata.org - For additional reference for pandas syntax etc.
# Stack Overflow - As always the go to for understanding errors and bugs in my CORDER

import sys
import random
import math
import string
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

#Coding Question 2.a

def main():
    input = open("dist.all.last.txt","r")
    N = 44399
    namesList = []

    for i,lineRaw in enumerate(input):
        line = lineRaw.split("	")[0]
        if i < N:
            namesList.append(line)
        elif i >= N and random.random() < N/float(i+1):
            replace = random.randint(0,len(namesList)-1)
            namesList[replace] = line

    namesListSums = []
    hashedSums = []
    for line in namesList:
        lineP = 0
        for char in line:
            lineP += string.ascii_lowercase.index(char.lower())+1
        namesListSums.append(lineP)
        hashedSums.append(lineP % 200)

    d = {
        "Hashed Sums by Bin":hashedSums
    }

    df = pd.DataFrame(data = d)
    df.hist(bins = 200)
    plt.xlabel("Bins (1 to 200)")
    plt.ylabel("# of Names Per Bin")
    plt.show()

if __name__ == "__main__":
    main()

###END###

#Coding Question 2.c.plot1

def main():
    input = open("dist.all.last.txt","r")
    namesList = []
    masterArr = []
    for i,lineRaw in enumerate(input):
        line = lineRaw.split("	")[0]
        namesList.append(line)
    random.shuffle(namesList)
    for n in range(1000):
        namesList2 = namesList[:n+1]
        namesListSums = []
        hashedSums = []
        for line in namesList2:
            lineP = 0
            for char in line:
                lineP += string.ascii_lowercase.index(char.lower())+1
            namesListSums.append(lineP)
            hashedSums.append(lineP % 200)
        masterArr.append(max(hashedSums))

    plt.plot(masterArr)
    plt.xlabel("n")
    plt.ylabel("Longest Chain")
    plt.title("Longest Chain in h(x) Hash Function for Increasing n")
    plt.show()

if __name__ == "__main__":
    main()


###END###

#Coding Question 2.c.plot2

def main():
    logs=[]
    for i in range(1000):
        logs.append(2*math.log(i+1,2))
    plt.plot(logs)
    plt.xlabel("n")
    plt.ylabel("Levels of Tree")
    plt.title("Levels of a Red Black Tree for Increasing N")
    plt.show()

if __name__ == "__main__":
    main()


###END###

#Coding Question 2.c.plot3

def main():
    vals=[]
    for i in range(1000):
        vals.append(i/200)
    plt.plot(vals)
    plt.xlabel("n")
    plt.ylabel("Longest Chain")
    plt.title("Longest Chain in a Uniform Hash Table")
    plt.show()

if __name__ == "__main__":
    main()


###END###
