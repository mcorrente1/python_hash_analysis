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
			if word != '':
				words.append(word)


	table = [] # table is an array with size modulus. 
				#,	Each element is a list of values that are hashed to the elements index
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
	for i in range(0, len(table)-1):
		indices.append(i)
		repeats.append(len(table[i])) # get chain size 
	
	return indices, repeats, len(words) 


def test_modulus_radix_pairs(fileName, outFileName, moduli, radices): 
	plt.figure(figsize=(20, 8))
	max_repeat = 0
	plot_num = 1
	for modulus in moduli:
		for radix in radices:
			indices, repeats, key_count = get_repeat_plot(fileName, radix, modulus)
			for r in repeats:
				if r > max_repeat:
					max_repeat = r
			ax = plt.subplot(len(moduli), len(radices), plot_num)
			if plot_num == 1: # title on first plot
				ax.set_title("Key Clustering for " + fileName + " with " + str(key_count) + " Keys ")

			#ax.bar(indices, repeats, width)
			ax.plot(indices, repeats,'-o', label='Radix:' + str(radix) + '/Modulus:'  + str(modulus))
			ax.legend(loc='upper left')
			plot_num += 1
		
	ax.set_ylabel('Key count')
	ax.set_xlabel('Table Index')
	plt.savefig(outFileName)
	plt.show()

radices = [128]
moduli = [32, 127, 97]
test_modulus_radix_pairs('dataFiles/5lw-s.dat', 'plots/5lw-s-plot.png', moduli, radices)
test_modulus_radix_pairs('dataFiles/wordList.txt', 'plots/wordList.png', moduli, radices)

radices = [256]
moduli = [50, 500, 5000]
test_modulus_radix_pairs('dataFiles/5lw-m.dat', 'plots/5lw-m-plot.png', moduli, radices)



radices = [256]
moduli = [100, 1000, 10000]
test_modulus_radix_pairs('dataFiles/5lw.dat', 'plots/5lw-plot.png', moduli, radices)