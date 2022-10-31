def gcd(m, n):
    print("\n")
    if m < n:
        m, n = n, m #swaps m and n so that m will always be the greater integer
    i = 0
    print(f"i | q\t m\t n\t r")
    print("——————————————————————————————————————")

    while n != 0:
        q = m//n #quotient
        r = m % n #remainder
        print(f"{i} | {q}\t {m}\t {n}\t {r}") #creates most of the table
        m = n #switches current n to be new m
        n = r #does the same with r and n
        i += 1
    q, r = "", "STOP"
    print(f"{i} | {q}\t {m}\t {n}\t {r}") #creates the last line of the table

    print("\n")
    return m

def main():
    print("The Euclidean Algorithm")
    print("-----------------------------")
    num1 = input("Enter the first number for the algorithm: ")
    is_int = False
    while is_int is False:
        try:
            num1 = int(num1)
            is_int = True
        except:
            num1 = input("Error! The value entered was not valid, please enter an integer: ")

    num2 = input("Enter the second number for the algorithm: ")
    is_int = False
    while is_int is False:
        try:
            num2 = int(num2)
            is_int = True
        except:
            num2 = input("Error! The value entered was not valid, please enter an integer: ")
    gcd(num1, num2)

    
main()