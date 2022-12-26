"""
/lectureNote/chapters/chapt03/codes/examples/dictionaries/histogram.py

"""
# %%
def histogram(s):
    # initialize with an empty dictionary !!!! ONLY CHECKS THE KEYS
    d = dict()

    for c in s:
        # print(c)
        if c not in d:
            # This is the first instance of c
            # Insert it as a key and set the value to 1
            d[c] = 1
        else:
            # c has already appeared, increment counter
            d[c] += 1

    # return dictionary
    return d


def histogram_ternary(s):  # ternary = collapse the if statement to one line

    # This is exactly the same as histogram
    # but using a so-called 'ternary operator':
    # a if test else b
    #
    # Ex: x='apple' if a > 2 else 'orange'
    # Translating this into English gives
    # x is 'apple' if a > 2; otherwise x is 'orange'

    d = dict()
    for c in s:
        # the ternary expression is shorter, though also terse
        d[c] = 1 if c not in d else d[c] + 1
    return d


def histogram_ternary_get(s):

    # This is exactly the same as histogram
    # but using 'get' method defined in dictionary:
    # See help(dict) and check out:
    #
    # get(...)
    # D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
    # i.e., if D is a dictionary,
    #                    /D[k] if k in D
    #      D.get(k,d) = |
    #                   \ d if k not in D
    #
    # Ex: x='apple' if a > 2 else 'orange'
    # Translating this into English will be
    # x is 'apple' if a > 2; otherwise x is 'orange'

    d = dict()
    for c in s:
        # Insert c with value 0 if it doesn't exist yet
        # otherwise return current value.
        # Either way, increment before storing
        d[c] = d.get(c, 0) + 1
    return d


if __name__ == "__main__":
    # first function
    h1 = histogram("apple")
    print("(a):", h1)

    # second function which uses the ternary operator
    h2 = histogram_ternary("apple")
    print("(b):", h2)

    # are they the same?
    print("(c):", h1 is h2)
    print("(d):", h1 == h2)

    # print keys
    print("(e):", h1.keys())

    # does 'a' appear as a key?
    print("(f):", "a" in h1)

    # print values
    print("(g):", h1.values())

    # does 2 appear as a value?
    print("(h):", 2 in h1.values())

    # 'get' takes a key and a default value
    # If the key appears in the dictionary
    # 'get' returns the corresponding value;
    # otherwise it returns the user defined
    # default value, e.g., 159 in the following example:
    print("(i):", h1.get("a", 159))  # .get('key from dic', number conditional)
    print(
        "(j):", h1.get("w", 159)
    )  # if the value exsists print the value else print the dummy number

# %%
