from hashlib import sha256

def mine(a, b, f):
	for i in range (a,b):
		s = "winner is hossam, n="+str(i)
		h = sha256(s.encode())
		d = h.hexdigest()
		if d[0:f]==("0"*f):
			print d, i
			break



mine(1,10000,2)
