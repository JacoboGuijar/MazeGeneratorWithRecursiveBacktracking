import numpy as np
import random
import time

array = np.random.randint(10, size= 1000)

t0 = time.time()
loops = 100
media = 0
longesttime = 0
shortesttime = 0

for i in range(loops):
	media += random.randint(1,5)

# for i in range(loops):
# 	boolean = True
# 	numbers = []
# 	t0 = time.time()
# 	while boolean:
# 		n = random.randint(0,3)
# 		if len(numbers) == 4:
# 			t1 = time.time()
# 			boolean = False
# 			media += t1 - t0
# 			#print(numbers)
# 			if longesttime < t1-t0:
# 				longesttime = t1-t0
# 			else:
# 				pass
# 			if shortesttime > t1-t0:
# 				shortesttime = t1-t0
# 		else:
# 			if n not in numbers:
# 				numbers.append(n)
# 				#print(numbers)
# 			else:
# 				pass


print("longesttime: " + str(longesttime))
print("shortesttime: " + str(shortesttime))
print("total: " + str(media))
print("media: " + str(media/loops))


print("test")


boolean = bool(input("input a boolean"))
if boolean == True:
	print("The written boolean was True")
elif boolean == False:
	print("FALSE")
else:
	print("café con churros")


# print(len(array))
# print(len(array[1]))
# print(array[1][1])
# print("Norte [1 - 1][1]: " + str(array[1 - 1][1]))
# print("Sur: [1 + 1][1]: " + str(array[1 + 1][1]))
# print("Oeste [1][1 - 1]: " + str(array[1][1 - 1]))
# print("Este [1][1 + 1]:" + str(array[1][1 + 1]))

