# Name: Michael Schaefer-Pham
# ID: 1715994
# CMPUT 274, Fall 2021
# Test program

p = input("p")
if p == "True":
	p = True
elif p == "False":
	p = False

q = bool(input("q"))
if q == "True":
	q = True
elif q == "False":
	q = False

test = (not(p and q))

print(test)

#print(p or not q,not p or q,not(p and q),p and p,q or q,sep=" ")