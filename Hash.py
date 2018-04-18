from hashlib import sha256

def mine(a, b, n1, n2, n3):
	for i in range (a,b):
		s = "winner is hossam, n="+str(i)
		h = sha256(s.encode())
		d = h.hexdigest()
		if d[0:n1]==("0"*n1):
			print d, i, n1
		if d[0:n2]==("0"*n2):
			print d, i, n2
		if d[0:n3]==("0"*n3):
			print d, i, n3
			break
			



mine(1,10000000000,8,9,10)
