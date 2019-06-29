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
	intake = input("Type 'quit' to end, type a topic you're interested in, or simply click enter\n> ")
	if intake == 'quit':
		break
	elif len(intake) == 0:
		intake = random.choice(topics)
		print('Topic: ' + intake)
	elif intake.lower() not in topics:
		print("I'm sorry. I've either misunderstood you or don't seem to have much knowledge on that topic. Let's try again.\n")
		continue

	filename = 'quotes/' + intake + '.json'
	f = open(filename, 'r')
	data = json.load(f)
	f.close()

	quote = random.choice(list(data['quotes']))
	print('''{} once said "{}"\n'''.format(quote['author'], quote['quote']))