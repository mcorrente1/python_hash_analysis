import Hash
import matplotlib.pyplot as plt
import time
times = []
collisions = []
radix = 128
mods = []
n =  1000

for i in range(n, n+100):
	table = []
	for x in range(i):
		table.append(0)
	for j in range(0,n):
		val = chr((i+j)*2%255)
		now = time.clock()
		collision = 0
		hash = int(Hash.hash(val, radix, len(table)))
		while table[hash] != 0:
			collision += 1
			hash += 1
			hash %= len(table)
		table[hash] = val
		speed = time.clock() - now
		mods.append(len(table))
		collisions.append(collision)
		times.append(speed)

plt.plot(mods, times)
plt.title('Table size v Runtime')
plt.show()

plt.plot(mods, collisions)
plt.title('Table size v Collisions')
plt.show()