student_score1 = 50
student_score2 = 50
student_score3 = 50
student_score4 = 50

#	  0  1  2  3  4 
scores = [50,34,45,50,25]

cart = ['banana', 33, 'juice', 2.5, ["fish", "palm oil"],True]
print(cart[4][1])

cart = ['banana', 33, 'juice', 2.5, ["fish", "palm oil"],True]
print(cart[0].upper()) 
 

print("we have",len(scores), "scores")
print(scores[2])

print("we have",len(scores), "scores")
print(scores[0:3:2])

#print("we have",len(scores), "scores")
#scores2 = scores(0:3:2)
#print(x,y)

for score in scores:
	print(score)

for idx in range(len(scores)):
	print(idx)


for index, value in enumerate(cart):
	print(index,value)

scores.append(99)
scores.pop(1)
print(scores)

scores.append(99)
scores.pop(1)
cart[4].insert(0,6)
print(cart)


#scores.append(99)
#scores.pop(1)
cart[4].insert(0,6)
#scores.extend([34,67,87,65])
print(scores)

#scores.append(99)
#scores.pop(1)
cart[4].insert(0,6)
#scores.extend([34,67,87,65])
new_list = cart + scores
print(new_list)

#scores.append(99)
#scores.pop(1)
cart[4].insert(0,6)
#scores.extend([34,67,87,65])
new_list = cart * 3
print(new_list)

#scores.append(99)
#scores.pop(1)
cart[4].insert(0,6)
#scores.extend([34,67,87,65])
new_list = cart + scores
print(scores[-1])

#scores.append(99)
#scores.pop(1)
cart[4].insert(0,6)
#scores.extend([34,67,87,65])
new_list = cart + scores
print(scores[::2])
#Slicing


print(enumerate(cart))

print(list(enumerate(cart)))

print(list(enumerate(cart))[4])





 
 