import numpy as np

def get_seq(state, cp, n):
    state = list(state)
    list_output = []
    
    for i in range(n):
        feedback = 0
        for s, c, in zip(state, cp):
            feedback += s*c
        feedback = feedback % 2
        list_output.append(state.pop(0))
        state.append(feedback)
        
    return list_output

connection_polynomials = [
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]]
  
keystream = '01000011010010110100110011101111111110100000001011000010011010101001011110011110111000100000011101000100101111101100111101110001011111000110110101101111110111110000010001001010000110010100100100000111'

keystream = np.array( [int(k) for k in keystream])
n = len(keystream)
print(keystream);

def to_binary(x, l):
    b = bin(x)[2:]
    r = [int(i) for i in b]
    while(len(r) < l):
        r = [0] + r
    return r

def correlation_value(a, b):
    return np.count_nonzero(a-b)/n
    
def crack_lfsr(cp):
    correlation_values = []
    initial_state = []
    l = len(cp)
    
    for i in range(2**l):
        i = to_binary(i,l)
        seq = get_seq(i, cp, n)
        seq = np.array(seq)
        
        c = abs(1 - correlation_value(seq, keystream))
        
        correlation_values.append(c)
        initial_state.append(i)
    
    return (initial_state, correlation_values)
    
key = []

for cp in connection_polynomials:
    init, corr = crack_lfsr(cp)
    max_corr = max(corr)
    possible_state = init[corr.index(max_corr)]
    print( max_corr, possible_state)
    key.append(possible_state)
    
print(key)

result = np.zeros(n)
for k,cp in zip(key, connection_polynomials):
    result = np.add(result, np.array(get_seq(k,cp,n)))

result = result >= 2

print ((result==keystream).all()) 

         
    