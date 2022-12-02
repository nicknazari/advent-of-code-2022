counter = 0
stack = []
highest = [] 
total = 0
scores = []

with open('./input.txt','r') as solution:
	for line in solution:
		if line != '\n':
			total += int(line.strip())
		else:
			scores.append(total)
			total = 0
threesol = []
for count in range(3):
	high = 0
	for score in scores:
		if score > high:
			high = score
	threesol.append(high)
	scores.remove(high)
print(sum(threesol))
