"""
/lectureNote/chapters/chapt03/codes/examples/dictionaries/invert_dictionary.py

"""

def invert_dictionary(d):
    # create an empty dictionary
    inverse = dict()

    # traverse through keys in dictionary "d"
    for key,val in d.items():
        if val not in inverse:
            # val hasn't been seen yet
            # insert it into the inverse dictionary
            # note [key] is wrapped as a list
            inverse[val] = [key]
        else:
            # val has been seen before
            # append the key to list stored in inverse[val]
            inverse[val].append(key)
    return inverse


if __name__ == "__main__":

    # import histogram method from histogram.py
    from histogram import histogram

    # compute histogram
    hist = histogram('apple')
    print( hist )

    # compute inverse map of dictionary
    inv = invert_dictionary(hist)
    print( inv )
