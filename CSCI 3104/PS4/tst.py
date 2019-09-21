import sys
import random
import string
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

def main():
    input = open("dist.all.last.txt","r")
    masterArr = []
    for z in range(1000):
        N = z
        namesList = []

        for i,lineRaw in enumerate(input):
            line = lineRaw.split("	")[0]
            if i < N:
                namesList.append(line)
            elif i >= N and random.random() < N/float(i+1):
                replace = random.randint(0,len(namesList)-1)
                namesList[replace] = line

        namesListSums = []
        hashedSums = [0]
        for line in namesList:
            lineP = 0
            for char in line:
                lineP += string.ascii_lowercase.index(char.lower())+1
            namesListSums.append(lineP)
            hashedSums.append(lineP % 200)
            print(lineP % 200)
        maximum = max(hashedSums)
        counter = 0
        for p in hashedSums:
            if p == maximum:
                counter += 1
        masterArr.append(counter)


    plt.plot(masterArr)
    plt.xlabel("n")
    plt.ylabel("Longest Chain")
    plt.title("Longest Chain Using h(x) Hashing for Increasing n")
    plt.show()

if __name__ == "__main__":
    main()
