#!/usr/bin/env python3
# %%
"""
/lectureNote/chapters/chapt03/codes/examples/pi.py

Remarks:
1. Docstring goes here with triple double quotation marks.
   The end of the docstring is closed by another triple double
   quotation marks.

2. You can put a block of comment lines in this way, anywhere in
   the code.

3. If you want to comment an individual line, you can use #

"""


# Let's import NumPy library and give it a short nickname as 'np'
import numpy as np


def estimate_pi(threshold):

    # INDENTATION, INDENTATION, AND INDENTATION!!!
    print("pi estimator using threshold = ", threshold)

    error = 10 * threshold  # initialize to be larger than the threshold
    n = 0  # initialize counter
    pi_appn = 0  # initialize pi approximation

    while error > threshold:
        pi_appn += 16.0 ** (-n) * (
            4.0 / (8.0 * n + 1.0)
            - 2.0 / (8.0 * n + 4.0)
            - 1.0 / (8.0 * n + 5.0)
            - 1.0 / (8.0 * n + 6.0)
        )

        # Putting 'a dot' followed by 'absolute' after 'np' means that
        # 'absolute' is one of methods which is available and provided in
        # the NumPy module.
        error = np.absolute(pi_appn - np.pi)

        # 'augmented assignment statement', same as n = n+1
        n += 1

        # output to screen
        print(n, pi_appn, error)
    return


"""
Block comment:
Now call to the function, estimate_pi, using 10^(-16) as a threshold value.
Call the function only when the file is executed in the script mode, but not
when it is imported as a module (We will learn more on this soon!)
"""

print("printing name=", __name__)

if __name__ == "__main__":
    # INDENTATION, INDENTATION, AND INDENTATION!!!
    estimate_pi(1e-14)


# %%
