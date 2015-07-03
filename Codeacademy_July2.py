#choice = raw_input('please give me a number: ')
#choice2 = raw_input('please give me a word: ')
#choice3 = raw_input('please give me a sentence: ')
choice4 = raw_input('please give me a list of numbers: ')


# def digit_sum(n): 
# 	listy = []
# 	for i in str(n):
# 		listy.append(int(i))
# 	return sum(listy)
# 	
# print digit_sum(choice)

# 
# score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
#          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
#          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
#          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
#          "x": 8, "z": 10}
# 
# list = []
# for x in choice2:
# 	list.append(score[x.lower()])
# 
# print sum(list)


# def fun():
# 	if "cats" in "cats like dogs":
# 		return True
# 	else: 
# 		return False
# 
# print fun() 

# def censor_cats(sentence):
# 	list1 = sentence.split()
# 	list2 = []
# 	for x in list1:
# 		if x != "cats":
# 			list2.append(x)
# 		else:
# 			list2.append("kats")
# 	return " ".join(list2)
# 
# 
# print censor_cats(choice3)
# 
# 
# 
# def censor(text,word):
# 	list1 = text.split()
# 	list2 = []
# 	for x in list1:
# 		if x != word:
# 			list2.append(x)
# 		else:
# 			list2.append("*" * len(word))
# 	return " ".join(list2)
# 
# print censor(choice3, choice2)


def median(list1):
    sorted_list = sorted(list1)
    if len(list1) % 2 == 1: 
    	return sorted_list[len(list1)/2]
    else:
    	middle_right_index = len(list1)/2
    	middle_left_index = middle_right_index - 1
    	left = sorted_list[middle_left_index]
        right = sorted_list[middle_right_index]
        return 0.5 * (left + right)
        
print median(eval(choice4))

def contains(y,x):
	if y in x:
		return True
	else:
		return False

print contains(choice2,choice3)

print 'hello'

# print choice3.split(" ")
# 
# print "SPACE".join(choice3.split(" "))
# 
