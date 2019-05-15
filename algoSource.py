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
    print("Error, list is None.")  

#Binary tree in Python############################
# For realize the binary tree, are using 
# 1) knot/node (kir: uzel)
# 2) addresses (kir: ssilki)
class BinarySearchTree:

    def __init__(self):
      self.root = None
      self.size = 0

    def length(self):
      return self.size

    def __len__(self):
      return self.size

    def __iter__(self):
      return self.root.__iter__()
	  
 
##################################################
# Линейный поиск в массиве
def array_search(A:list, N:int, x:int):
	"""	Осуществляет поиск числа x в массиве A
		от 0 до N-1 индекса включительно.
		Возвращает индекс элемента x в списке A.
		Или -1, если такого нет.
		Если в массиве несколько одинаковых элементов,
		равных x, то вернть индекс первого по счёту.
	"""
	for k in range(N):
		if A[k] == x:
			return k
	return -1


def test_array_search():
	A1 = [1,2,3,4,5]
	m = array_search(A1, 5 ,8)
	if m == -1:
		print("#test1 - ok", m)
	else:
		print("test1 - fail", m)

		
	A2 = [-1,-2,-3,-4,-5]
	m = array_search(A2, 5 ,-3)
	if m == -1:
		print("#test2 - ok", m)
	else:
		print("test2 - fail", m)
	
	A3 = [10,20,30,10,50]
	m = array_search(A3, 5 ,10)
	if m == -1:
		print("#test3 - ok", m)
	else:
		print("test3 - fail", m)
		
##################################################
# Инвертирование списка
def invert_array(A:list, N:int):
	"""	Обращение массива (поворот задом-наперёд)
		в рамках индексов от 0 до N-1.
	"""
	for k in range(N//2):
		A[k], A[N-1-k] = A[N-1-k], A[k]
	
def test_invert_array():
	A1 = [1,2,3,4,5]
	print(A1)
	invert_array(A1, 5)
	print(A1)
	if A1 == [5,4,3,2,1]:
		print("#test1 - ok")
	else:
		print("#test1 - fail")
		
	A2 = [0,0,0,0,0,0,0,10]
	print(A2)
	invert_array(A2, 8)
	print(A2)
	if A2 == [10,0,0,0,0,0,0,0]:
		print("#test1 - ok")
	else:
		print("#test1 - fail")
	

if __name__ == "__main__":
	test_invert_array()
  