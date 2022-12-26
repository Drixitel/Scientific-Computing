# define the main() function
def main():

    i = 0  # required declared integer i (why?)
    x = 119.0  # declared a float x (decimal implies float)

    # print(f'Declared numbers i = {i} and x =  {x}')

    for i in range(120):  # loop [0,119]
        if i % 2 == 0:  # modulo: if i is divisible by 2
            # the remainder is zero, implies even
            x += 3
            # print(x)					#add 3 to i if even
        else:
            x -= 5  # subtract 5 if odd
            # print(x)

    s = "%3.2e" % x  # This creates a string s.t 3 is the total
    # characters alloted, e is the scientific not.
    # and 2 provides to two decimal places
    # the % is a call function that calls to the %x
    # just outside of the string
    print(s)  # function prints final value s


if __name__ == "__main__":  # __name__ is a set variable that checks hello_again.py
    main()  # if that matches to be the main script, then it
    # will execute the defined function main()
