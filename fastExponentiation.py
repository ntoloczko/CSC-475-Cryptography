def expMod(x, e, n):
    y = x
    print('\ni|xᵢ|\tSquaring y\t|\tMultiplying y') # Table header
    print('———————————————————————————————————————————————————————————————')
    print(f'0|{bin(e)[2:][0]} |              \t|{y}') # First row in the table (not in the iterative process)
    for i in range(1, len(bin(e)[2:])): # For every bit of the exponent in binary (excluding the first)
        table_row = f'{i}|{bin(e)[2:][i]} |{y}² mod {n} = {(y*y)%n}\t|' # Creates most of this iteration's row
        y = (y * y) % n
        if int(bin(e)[2:][i]) == 1: # If the current bit is a 1
            table_row += (f'{x} X {y} mod {n} = {(x*y)%n}') # Will append the multiplication if the process used
            y = (y * x) % n
        else:
            table_row += (f'{y}') # Otherwise will append the current y value

        print(table_row) # Prints the full row

    print('\n')

    return y