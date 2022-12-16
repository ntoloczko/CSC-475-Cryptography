import time
import random

def primeNumberGen(print_trace=False):
    binary_num = '1' # Used to add to first and last bit of the number
    seed_spacer = random.randint(1, 11) # Used because sometimes the machine works too fast and grabs the same prime twice
    randomSeed = int(time.time()) - seed_spacer
    random.seed(randomSeed)
    trace = '' # Stores the trace
    counter = 5

    for i in range(0, 5):
        random_num = bin(random.randint(0, 1000001)) # Any number between one and a million so that the computer does not take a massive number like 540 trillion
        random_bit = random_num[len(random_num) - 1]
        binary_num += random_bit
        trace += (f'\nb_{counter}|{random_num[2:]}|{random_bit}')
        counter -= 1

    binary_num += '1'
    decimal_num = int(binary_num, 2)
    binary_num = '{:032b}'.format(decimal_num) # converts to 32 bits
    trace += (f'\nNumber|{decimal_num}|{binary_num}')

    if print_trace is True:
        print(trace)

    return decimal_num

def primalityTest(x, e, n, print_trace=False):
    y = x
    table_header = f'\nP = {n} a = {x}'
    table_header += '\ni|xᵢ|z  \t|\tSquaring y\t|\tMultiplying y' # Table header
    table_header += '\n———————————————————————————————————————————————————————————————'
    table_header += f'\n0|{bin(e)[2:][0]} |1   \t|1              \t|{y}' # First row in the table (not in the iterative process)
    if print_trace is True:
        print(table_header)
    for i in range(1, len(bin(e)[2:])): # For every bit of the exponent in binary (excluding the first)
        z = y
        table_row = f'{i}|{bin(e)[2:][i]} |{z}  \t|{y}² mod {n} = {(y*y)%n}  \t|' # Creates most of this iteration's row
        y = (y * y) % n
        if y == 1 and z != 1 and z != e: # If the square root is bad
            return None
        if int(bin(e)[2:][i]) == 1: # If the current bit is a 1
            table_row += (f'{x} X {y} mod {n} = {(x*y)%n}') # Will append the multiplication if the process used
            y = (y * x) % n
        else:
            table_row += (f'{y}') # Otherwise will append the current y value

        if print_trace is True:
            print(table_row) # Prints the full row

    if y != 1:
        return False
    elif y == 1:
        return True

def euclid(m, n):
    if m < n:
        m, n = n, m #swaps m and n so that m will always be the greater integer
    
    modulo = m

    i = 1
    s = [] 
    t = [] 
    q_values = []
    print(f'i | q\t \tm\t n\t r\t s\t t')
    print('—————————————————————————————————————————————————————————')

    while n != 0:
        q = m//n #quotient
        q_values.append(q)
        r = m % n #remainder
        if i == 1:
            s.append(1)
            t.append(0)
        elif i == 2:
            s.append(0)
            t.append(1)
        elif i > 2:
            s.append(s[i-3]-(q_values[i-3]*s[i-2]))
            t.append(t[i-3]-(q_values[i-3]*t[i-2]))

        print(f'{i} | {q}   \t{m}\t {n}\t {r}\t {s[i-1]}\t {t[i-1]}') #creates most of the table
        m = n #switches current n to be new m
        n = r #does the same with r and n
        i += 1

    s.append(s[i-3]-(q_values[i-3]*s[i-2])), t.append(t[i-3]-(q_values[i-3]*t[i-2]))
    q, n, r = '', '', ''
    print(f'{i} | {q}    \t{m}\t {n}\t {r}\t {s[i-1]}\t {t[i-1]}') #creates the last line of the table

    if t[i-1] < 0:
        t[i-1] = t[i-1] + modulo

    print('\n')
    return m, t[i-1]

def keyGen():
    print('-----------------------------------')
    prime1 = primeNumberGen(True)
    prime2 = primeNumberGen()

    success = 0
    failure = 0
    good_primes = 0
    prime1_result = None
    prime2_result = None


    while good_primes < 2 or prime1 == prime2:
        if prime1 == prime2:
            prime1 = primeNumberGen()
            prime2 = primeNumberGen()
        if prime1_result == 'failed':
            prime1 = primeNumberGen()
        if prime2_result == 'failed':
            prime2 = primeNumberGen()

        for num in range(1, 21): # Tries 20 bases
            base1 = random.randint(1, prime1) % prime1 # Finds a suitable base
            if primalityTest(base1, prime1-1, prime1) is True and num == 20 and success == 0: # If the 'prime' passed all 20 bases
                good_primes += 1
                primalityTest(base1, prime1-1, prime1, True)
                print(f'{prime1} is perhaps a prime')
                success += 1
            elif primalityTest(base1, prime1-1, prime1) is True and num == 20:
                good_primes += 1
            elif primalityTest(base1, prime1-1, prime1) is True and num != 20: # If it is working through the cases
                continue
            else: # If it failed
                prime1_result = 'failed'
                if failure == 0:
                    primalityTest(base1, prime1-1, prime1, True)
                    print(f'{prime1} is not a prime because {prime1-1} ^ {prime1-1} mod {prime1} != 1')
                    failure += 1
    

        for num in range(1, 21): # Tries 20 bases
            base2 = random.randint(1, prime1) % prime2 # Finds a suitable base
            if primalityTest(base2, prime2-1, prime2) is True and num == 20 and success == 0: # If the 'prime' passed all 20 bases
                good_primes += 1
                primalityTest(base2, prime2-1, prime2, True)
                print(f'{prime2} is perhaps a prime')
                success += 1
            elif primalityTest(base2, prime2-1, prime2) is True and num == 20:
                good_primes += 1
            elif primalityTest(base2, prime2-1, prime2) is True and num != 20: # If it is working through the cases
                continue
            else: # If it failed
                prime2_result = 'failed'
                if failure == 0:
                    primalityTest(base2, prime2-1, prime2, True)
                    print(f'{prime2} is not a prime because {prime2-1} ^ {prime2-1} mod {prime2} != 1')
                    failure += 1
        
    if success == 2:
        primalityTest(random.randint(1, 6) % 6, 6-1, 6, True) # Known non-prime used when both primes are correct on first run
    
    n = prime1 * prime2
    
    print('\n')

    e = 3 # Starts with e of 3
    print(f'e = {e}')
    d = euclid(e, n)
    while d[0] % n != 1: # If there is no inverse associated with that e
        e += 1
        print(f'e = {e}')
        d = euclid(e, n)
    print(f'd = {d[1]}')

    print('\n')

    private_n = n
    private_d = d[1]


    print(f'p = {prime1}, q = {prime2}, n = {n}, e = {e}, d = {d[1]}') # Formats the output
    prime1 = '{:032b}'.format(prime1) 
    print(f'p = {prime1}')
    prime2 = '{:032b}'.format(prime2) 
    print(f'q = {prime2}')
    n = '{:032b}'.format(n) 
    print(f'n = {n}')
    e = '{:032b}'.format(e) 
    print(f'e = {e}')
    d = '{:032b}'.format(d[1]) 
    print(f'd = {d}')
    print('\n')

    return (private_n, private_d) # Returns the private key

keyGen() # Runs the program
