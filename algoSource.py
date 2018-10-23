import os
#SCF == smallest common factor == naimen'shiy obshiy delitel' == NOD
#src of material : https://younglinux.info/algorithm
#Algorithm of finder "SCF" across division
def Evkl_Division(inA, inB):

  while inA!=0 and inB!=0:
    if inA > inB:
        inA = inA % inB
    else:
        inB = inB % inA
  print (inA+inB)

if __name__ == '__main__':
  Evkl_Division(input("Enter a: "), input("Enter b: "))