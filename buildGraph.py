import json
from os import walk
import re
import random
import itertools

def readSymbol():
	f = open("symbols.txt","r")
	data = json.loads(f.read())
	return data

def getSubset(term_id = "4530",search_terms=""):
	term_id = "./data/" + term_id 
	search_terms = re.sub('[^a-zA-Z0-9\n\.]', ' ', search_terms)
	search_terms = search_terms.lower().split()
	subset = []
	symbols = readSymbol()
	for (dirpath, dirnames, filenames) in walk(term_id):
		for f in filenames:
			if f != "term.info":
				data = json.loads(open(dirpath+"/"+f).read())
				string = symbols[data['subject']] + " " + data['title'] + " " + data['instructor']['name']
				string = re.sub('[^a-zA-Z0-9\n\.]', ' ', string)
				string = string.lower().split()

				if set.intersection(set(search_terms),set(string)):
					subset.append((data['title'],string))
	return subset

def getGraph(term_id = "4530",search_terms=""):
	subset = getSubset(search_terms=search_terms)
	data = {}
	data['nodes'] = {}
	data['edges'] = {}
	for i in subset:
		data["nodes"][i[0]] = {}
		data["nodes"][i[0]]['borders'] = random.sample(range(2,10),1)[0]
		data["nodes"][i[0]]['length'] = random.sample(range(400,2000),1)[0]

	for i in itertools.combinations(subset,2):
		if not data['edges'].has_key(i[0][0]):
			data['edges'][i[0][0]] = {}
		if len(data['edges'][i[0][0]].keys()) >= 1:
			continue
		else :
			data['edges'][i[0][0]][i[1][0]] = {}
			data['edges'][i[0][0]][i[1][0]]['border'] = random.sample(range(70,300),1)[0]		
	return data


if __name__ == "__main__":
	graph = getGraph(search_terms="management science")
	f = open("./static/atlas/maps/asia.json","w")
	f.write(json.dumps(graph))
	f.close()