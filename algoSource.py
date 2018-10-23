import os
#SCF == smallest common factor == naimen'shiy obshiy delitel' == NOD
#src of material : https://younglinux.info/algorithm
#Algorithm of finder "SCF" across division
def Evkl_Division(inA, inB):
  a = int(inA)
  b = int(inB)
  try:
    while a!=0 and b!=0:
      if a > b:
        a = a % b
      else:
        b = b % a
    print (a+b)
  except IOError:
    print("ERROR : PROBLEM WITH VALUES OF INPUT")
  

if __name__ == '__main__':
  Evkl_Division(input("Enter a: "), input("Enter b: "))