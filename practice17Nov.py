import pprint 
message = 'It was a bright cold day in ldhjfjkhdajflwkjfkl'
count={}

for char in message:
	count.setdefault(char, 0) # ensure the key is in the count dictionary
	count[char] = count[char] +1

pprint.pprint(count)  # prints prettily

pprint.pformat(count) # prints it into a string



#objective orientation
class MyList():
	def __init__(self):
		self._hidden_list=[]
	def getkthitem(k):
		return self._hidden_list[k]
	def append(v):
		self._hidden_list.append(v) # the   _  hides the hidden_list away from the user 


# encapsulation
#data structure -> Structure data and store in a useful
#you bundle together functions that operate on the data
#with the data itself

#List -> Append, Insert, Sort
#list(1,3,5,6,7)

#def square(x): return x*x
#def square(self): return self.x*self.x


#a.append(3)



#def append(self, v):

from collections import defaultdict

def removecount(lst):
	count=defaultdict(int)
	fset=[]
	for e in lst:
		count[e]+=1
		if count[e]==1:
			fset.append(e)
	return fset


class MySet() :
	def __init__(self, lst): #why do you need the __  #special function
		self.thisisset=removecount

	def union(self, lst):
		return MySet(removecount)


if __name__ == '__main__':
	print "You are running me as a main program!"


