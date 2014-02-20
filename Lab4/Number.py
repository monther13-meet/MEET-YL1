class Integer(object): 
	def __init__(self, number, positive):
        	self.positive=positive
        	self.number = number
    
    	def display(self):
		if(self.positive==True):
       			print self.number
		else:
			print -1*self.number
class NegativeInteger(Integer):
	def __init__(self, number):
		Integer.__init__(self, number, False)
    	def display(self):
		Integer.display(self)
		print "This is NegativeInteger!!"
if __name__=="__main__":
	test=Integer(25)
	test.display()
	test2=NegativeInteger(5)
	test2.display()
	hi=[test, test2]
	for i in hi:
		i.display()

