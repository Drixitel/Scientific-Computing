# Basic Commands in Linux

- `cat filename` : shows contents of file
- `more filename`: shows contents of file
- `less filename`: shows contents but removes all other terminal objs, exit with `q`
- `cat > filename`: creates file
- `touch filename`: generates new or updates time stamp on existing file
- `cat filename1 filename2 > otherfile`: in order writes/overwrites file 1 & 2 onto other file
  - IF `cat file3 > otherfile` is ran after the previous command it will overwrite otherfile with file 3 contents
- `cat filename1 >> otherfile`: keeps the contents of `otherfile` and appends it with file 1 contents
- `-r`: gives acces to modify directories
- `wc filename`: gives (# of lines, # of words, # of characters)

# Error Messages

- live in the channel called Standard Error `stderr`
- Actually I have no idea
  - `cat filename1 2>> otherfile`: seems to only show file 1 contents on terminal but not overwrite/append otherfile.
  - IF `cat filethatdoesnotexists 2>> otherfile` is used it will append otherfile and say the file DNE
  - IF `cat filethatdoesnotexists 2> otherfile` is used it will overwite the file and say it DNE
- redirect input into an output file
  - e.g `wc -l < filename1 >> output_wordcount.txt`
    - this takes the command word count and applies it to file 1 then takes that output #number of lines and appends it to the output txt file.
- `sort filename`: sorts the lines of the file by number then by letter (IMPORTANT IT'S BY CHARACTER)
- `head -number` or `tail -number`: can take the 1st or last lines

# Create multiple directories at once

- `touch dir1/dir2/newdir{,1,2}`
  - this will create within dir2: newdir, newdir1, newdir2

# Conditional Commands

- `&&`: runs the second command only if the first one succeeds
- `||`: runs the secodn only if the first fails
- `;`: lets you put multiple commands all on one line running unconditionally

# Putting the error messages in a file

- Maybe you don't want the error messages to populate in your file
- we can create a `err.log` file and pipe the error into it as we try to make changes
- e.g.:
  - `cat filethatdoesnotexists >> output.txt 2>> err.log`
  - the error message is now in the log and not in the desired file
