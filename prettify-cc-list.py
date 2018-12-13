import pyperclip
import sys
import re

def correctTheCC(my_string):
	#my_string_ex1 = "\"CHELSEA,SWNA\\BOLING,X.Y@CO.com,\"BOLING,\"EHHH"
	my_list = my_string.split(",")
	matching2 = [s for s in my_list if re.match('[a-zA-Z]*', s,0)]
	print matching2
	theDifference = set(my_list) - set(matching2)
	cc_list = list(theDifference)

	leText = ', '.join(str(s) for s in cc_list)
	pyperclip.copy(leText)
	return letext

if __name__ == '__main__':
	flags = {"text": '-t'}
	ccText ='haha'
	stringCorrect = False

	for arg in  sys.argv:
		if arg in flags.values():
			if arg == flags["text"]:
				stringCorrect = True
		else:
			if stringCorrect == True:
				ccText = arg
	print 'this is: ' + ccText +' \t'
	theRealDeal = correctTheCC(ccText)
	print theRealDeal + ' has been copied to your clipboard'

	#clear