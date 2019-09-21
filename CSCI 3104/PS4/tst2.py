import sys
import math
import random
import string
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

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
