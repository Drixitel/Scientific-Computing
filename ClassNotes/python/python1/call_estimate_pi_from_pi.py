"""
/lectureNote/chapters/chapt03/codes/examples/call_estimate_pi_from_pi.py

Remark:
1. In this caller routine, you can import pi.py as a module
   and use the estimate_pi function defined therein.

2. We will learn more on this soon.

"""

import pi

print(pi.__name__)

print(pi.estimate_pi(1e-16))
