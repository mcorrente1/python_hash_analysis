import Hash
import matplotlib.pyplot as plt
import time

def get_repeat_plot(fileName, radix,modulus):
	radix = 128
	n =  0

	file = open(fileName)
	lines = file.read().strip().split('\n')
	words = []
	for line in lines:
		for word in line.strip().split(' '):
			words.append(word)


	table = [] # table is an array with size modulus. 
				#	Each element is a list of values that are hashed to the elements index
	for i in range(modulus):
		table.append(0)
		table[i] = []
	for word in words:
		now = time.clock()
		hash = int(Hash.hash(word, radix, modulus))
		if table[hash] == None:
			table[hash] = []
		table[hash].append(word)
		speed = time.clock() - now

	indices = []
	repeats = []
	for i in range(0, len(table)):
		indices.append(i)
		repeats.append(len(table[i])) # get chain size 
	return indices, repeats


def test_modulus_radix_pairs(fileName, outFileName, moduli, radices): 
	plt.title("Table Index vs. Size of Chain for " + fileName)
	ax = plt.subplot()
	max_repeat = 0
	for modulus in moduli:
		for radix in radices:
			indices, repeats = get_repeat_plot(fileName, radix, modulus)
			for r in repeats:
				if r > max_repeat:
					max_repeat = r
			ax.plot(indices, repeats,' o', label='Radix:' + str(radix) + '/Modulus:'  + str(modulus))
	ax.set_ylim(0,max_repeat+max_repeat*0.1)
	legend = plt.legend(loc='upper center', shadow=True)
	plt.savefig(outFileName)
	plt.show()

radices = [128]
moduli = [32, 127, 97]
test_modulus_radix_pairs('dataFiles/5lw-s.dat', 'plots/5lw-s-plot.png', moduli, radices)


radices = [138]
moduli = [132, 2027, 307]
test_modulus_radix_pairs('dataFiles/5lw-m.dat', 'plots/5lw-m-plot.png', moduli, radices)