from random import randint

firstWord=['admin','python','ruby','github','jquery','AJAX','login','data','java','php']
secondWord=['client','script','code','game','API','program','tutorial','description0','embed','sharer']

def noteGen():
	return firstWord[randint(0,9)] + ' ' + secondWord[randint(0,9)]

if __name__=='__main__':
	print (noteGen())