#!/bin/bash

# Check the disk usage under out local directory

# Total disk usage

# Output:

# du -sh $AM129_PATH

# Sub & files disk usage

# sort the contents

# by size in decreasing order

# du -ah $AM129_PATH | sort -hr

# outputs the 3 largest enteries to a file

# output file name : dirSizes.txt

du -ah $AM129_PATH | sort -hr | head -3 > dirSizes.txt && cat dirSizes.txt

# Finally output the entire list to the screen:

# du -ah $AM129_PATH | sort -hr
