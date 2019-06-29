from os import listdir
from os.path import isfile, join
import json
import random

topics = []
for f in listdir('quotes/'):
	if isfile(join('quotes/', f)) and f[-5:] == '.json':
		topics.append(f[:-5])

intake = ''
while True:
	intake = input("Type a topic you're interested in or type 'quit' to end\n> ")
	if intake == 'quit':
		break
	elif intake not in topics:
		print("I'm sorry. I've either misunderstood you or don't seem to have much knowledge on that topic. Let's try again.\n")
	else:
		filename = 'quotes/' + intake + '.json'

		f = open(filename, 'r')
		data = json.load(f)
		f.close()

		quote = random.choice(list(data['quotes']))
		print('''{} once said "{}"\n'''.format(quote['author'], quote['quote']))