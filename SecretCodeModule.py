#Clues come in format of [[color sequence], number_of_reds, number_of_yellows]
#red = 1
#orange = 2
#yellow = 3
#green = 4
#blue = 5
#purple = 6
#pink = 7
#white = 8
def translate(*codes):
	rval = []
	for code in codes:
		dictionary = {1:'red', 2:'orange', 3:'yellow', 4:'green', 5:'blue', 6:'purple', 7:'pink', 8:'white'}
		rvalue = []
		for clue in code:
			for c in clue:
				rvalue += [dictionary[c]]
			rval += [[rvalue]]
			rvalue = []
	return rval
def get_clue(code, guess):
	code_c = code[:]
	guess_c = guess[:]
	rvalue = [guess[:], 0, 0]
	for i in range(4):
		while True:
			try:
				if code_c[i] == guess_c[i]:
					rvalue[1] += 1
					del code_c[i]
					del guess_c[i]
				else:
					break
			except IndexError:
				break
	for i in code_c[:]:
		for v in guess_c[:]:
			if i == v:
				rvalue[2] += 1
				del guess_c[guess_c.index(v)]
				del code_c[code_c.index(i)]
				break
	return rvalue
def SecretCode(*clues):
	possibles = []
	for i in range(1, 9):
		for v in range(1, 9):
			for x in range(1, 9):
				for l in range(1, 9):
					code = [i, v, x, l]
					is_correct = True
					possibles += [code]
					for clue in clues:
						if get_clue(code, clue[0]) != clue:
							del possibles[-1]
							break
	return possibles
print (translate(SecretCode([[1, 2, 3, 4], 1, 0], [[5, 6, 7, 8], 1, 0])))
print (len(SecretCode([[1, 2, 3, 4], 1, 0], [[5, 6, 7, 8], 1, 0])))
#Code:3, 2, 2, 3
