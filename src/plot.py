import Hash
import matplotlib.pyplot as plt
import time
import pandas as pd

def get_repeat_plot(fileName, radix,modulus):
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

def get_all_hash_values(fileName, radix,modulus):
	file = open(fileName)
	lines = file.read().strip().split('\n')
	words = []
	for line in lines:
		for word in line.strip().split(' '):
			if word != '':
				words.append(word)

	hashList = []

	for word in words:
		hash = int(Hash.hash(word, radix, modulus))
		hashList.append(hash)

	return hashList


def test_modulus_radix_pairs_hist(fileName, outFileName, moduli, radices):
	plt.figure(figsize=(20, 8))
	max_repeat = 0
	plot_num = 1
	for modulus in moduli:
		for radix in radices:
			hashes = get_all_hash_values(fileName, radix, modulus)
			indices, repeats, key_count = get_repeat_plot(fileName, radix, modulus)
			zeros = 0
			for r in repeats:
				if r == 0:
						zeros += 1
				if r > max_repeat:
					max_repeat = r
			ax = plt.subplot(len(moduli), len(radices), plot_num)
			if plot_num == 1: # title on first plot
				ax.set_title("Key Clustering for " + fileName + " with " + str(key_count) + " Keys ")
			ax.hist(hashes, bins = modulus, histtype='step', label='Radix:' + str(radix) + '/Modulus:'  + str(modulus))
			ax.legend(loc='upper left')
			ax.set_ylabel('Frequency')
			ax.set_xlabel('Table Index')
			plot_num += 1
			s = pd.Series(hashes)
			print s.describe()
			print 'number of empty locations: ' + str(zeros)
			print 'number of singles: ' + str(repeats.count(1))
			print(' ')

	plt.savefig(outFileName)
	plt.show()

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
			if plot_num == 1:  # title on first plot
				ax.set_title("Key Clustering for " + fileName + " with " + str(key_count) + " Keys ")

			# ax.bar(indices, repeats, width)
			ax.plot(indices, repeats, '-o', label='Radix:' + str(radix) + '/Modulus:' + str(modulus))
			ax.legend(loc='upper left')
			plot_num += 1

	ax.set_ylabel('Key count')
	ax.set_xlabel('Table Index')
	plt.savefig(outFileName)
	plt.show()

def plot_histogram_hash(fileName, outFileName, moduli, radices):
	plt.figure(figsize=(20, 8))
	plot_num = 1
	for modulus in moduli:
		for radix in radices:
			hashes = get_all_hash_values(fileName, radix, modulus)
			ax = plt.subplot(len(moduli), len(radices), plot_num)
			if plot_num == 1:  # title on first plot
				ax.set_title("Key Clustering for " + fileName + " with " + str(len(hashes)) + " Keys ")
			ax.hist(hashes)
			ax.legend(loc='upper left')
			plot_num += 1

	ax.set_ylabel('Key count')
	ax.set_xlabel('Table Index')
	plt.savefig(outFileName)
	plt.show()

radices = [128, 256]
moduli = [127, 123, 213, 255]
test_modulus_radix_pairs_hist('../dataFiles/5lw-m.dat', '../plots/5lw-m-plot2.png', moduli, radices)