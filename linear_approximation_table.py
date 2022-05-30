def to_binary(x,l):
	b = bin(x)[2:]
	r = [int(i) for i in b ]
	while(len(r) < l):
		r= [0]+r
	return r

def dot(m,n):
    sum = 0
    for i in range(4):
        sum+=m[i]*n[i]
    return sum%2

SBox = [8,4,2,1,12,6,3,13,10,5,14,7,15,11,9,0]

def NL(a,b):
    cont = 0
    for i in range(16):
        for j in range(16):
            if SBox[i] == j and dot(to_binary(a,4),to_binary(i,4))^dot(to_binary(b,4),to_binary(j,4)) == 0:
                    cont+=1
    return cont

linear_approximations = []
for i in range(16):
    linear_approximations.append([]);  
    for j in range(16):
        linear_approximations[i].append(NL(i,j));
        
for i in range(16):
    print(linear_approximations[i])
    
