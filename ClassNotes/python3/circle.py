"""
A module for computing properties of circles

Functions in this module return properties of a circle as determined by
it's radius

Included functions:
area           -- Returns area of circle
circumference  -- Returns circumference of circle
"""

import numpy as np

def area(radius=1.0):
    """
    Compute area from radius

    Arguments:
    radius -- radius of circle (default 1.0)
    """
    area = np.pi*radius**2
    return(area)

def circumference(radius=1.0):
    """
    Compute circumference from radius

    Arguments:
    radius -- radius of circle (default 1.0)
    """
    
    circumference = 2.*np.pi*radius
    return circumference

if __name__ == "__main__":
    print('area of a circle with r = 1 is ', area())
    print('circumference of a circle with r = 1 is ', circumference())
    print('area of a circle with r = 2 is ', area(2.0))
    print('circumference of a circle with r = 2 is ', circumference(2.0))

print('this is a call to the circle module!')
