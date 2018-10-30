import os
#src of material : https://ru.wikibooks.org/wiki/%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8_%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D0%BE%D0%B2/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%95%D0%B2%D0%BA%D0%BB%D0%B8%D0%B4%D0%B0#Python
#Algorithm of finder "GCD" across division (Greatest Common Divisor)
'''
An example as math:
GCD(235:150)=GCD(150;85)=GCD(85;65)=GCD(65;20)=GCD(20;5)=5
235/150 = 1(85), 150/85 = 1(65) ... 65/20 = 3(5), 20/5 = 4(5)
'''
def GCD(inA, inB):
  try:
    a = abs(int(inA)) # get module
    b = abs(int(inB)) # get module
    if a != 0 and b != 0:
      while a!=0 and b!=0:
        if a > b:
          a = a % b # ret a residue (tr:ostatok)
        else:
          b = b % a # ret a residue (tr:ostatok)
      print (a+b)
  except ValueError:
    print("error, you were not put a numeral")
  else:
    print("if code is succesfull")
  finally:
    print("switch on always")



def BubbleSort(inList):
  print("Start bubble sort...")
  print(inList)
  n = 1
  trash = 0
  if inList != None:
    try:
      # bubble  
      ''' # url https://younglinux.info/algorithm/bubble
      while n < len(inList):
        for i in range( len(inList) - n ):
          if inList[i] > inList[i + 1]:
            trash = inList[i]
            inList[i] = inList[i+1]
            inList[i+1] = trash
            #inList[i], inList[i+1] = inList[i+1], inList[i]
        n += 1
      #output
      #['32', '53', '2', '300']
      #['2', '300', '32', '53']
      '''
      #buble url wiki
      for i in range(len(inList)):
        for j in range(len(inList) - 1, i, - 1):
          if inList[j] < inList[j - 1]:
            trash = inList[j]
            inList[j] = inList[j-1]
            inList[j-1] = trash
      print(inList)
      #output
      #['20', '1000', '12', '7']
      #['1000', '12', '20', '7']
    except OSError:
      print("Error, that is bad")
    except IndexError:
      print("Error, index")
    #finally:
  else:
    print("Error, list is None")

def LCM_P(self):
  try:
    pass
  except ValueError:
    pass
  else:
    pass
  finally:
    pass

if __name__ == '__main__':
  #GCD(input("enter a: "), input("enter b: "))
  #task 1: 
  # 1) bubble sort list 
  ls = [1,243,100,54,1234] # list
  print(ls)
  tr = 0  # temp value
  if ls != None:
    for i in range(len(ls)):
      for j in range(len(ls) -1, i,-1):
        if ls[j] < ls[j-1]:
          temp = ls[j]
          ls[j] = ls[j-1]
          ls[j-1] = temp
  print(ls)          
  # 2) find GCD

  '''Bubble Sort
  work_list = []
  cycle = 0
  while cycle != 4:
    work_list.append(input("input max size list:"))
    cycle += 1
  BubbleSort(work_list)
  '''