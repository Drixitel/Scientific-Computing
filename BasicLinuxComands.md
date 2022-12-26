# Basic Commands in Linux & Git

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
  - `wc -l`: gives line count

# Removal

- `rm -rf`: rm is remove `-r` recursive i.e. remove all sub dir, `f` force

# Error Messages

- live in the channel called Standard Error `stderr`
- using `2>, 2>>` makes it so the standard message, which might be a blank overwriting of a file bc the first file DNE instead will write the erro into the file so you're aware that an error occurred.
- Actually I have no idea
  - `cat filename1 2>> otherfile`: seems to only show file 1 contents on terminal but not overwrite/append otherfile.
  - IF `cat filethatdoesnotexists 2>> otherfile` is used it will append otherfile and say the file DNE
  - IF `cat filethatdoesnotexists 2> otherfile` is used it will overwrite the file and say it DNE
- redirect input into an output file
  - e.g `wc -l < filename1 >> output_wordcount.txt`
    - this takes the command word count and applies it to file 1 then takes that output #number of lines and appends it to the output txt file.
- `sort filename`: sorts the lines of the file by number then by letter (IMPORTANT IT'S BY CHARACTER)
- `head -number` or `tail -number`: can take the 1st or last lines

## Redirect ALL standard error

- use `&>`: can capture standard AND stderr in a file
  - Most useful
  - e.g.:
    - `ls &> filename1` : writes the ls files to a file
    - `cat filename1`: check the contents
    - `ls filethatDNE &> filename1`
    - `cat filename`: rewritten error message

# Create multiple directories at once

- `touch dir1/dir2/newdir{,1,2}`
  - this will create within dir2: newdir, newdir1, newdir2

# Conditional Commands

- `&&`: runs the second command only if the first one succeeds
  - e.g.:
    - cd into a dir and rm all contents in final dir
    - cd dir1/dir2 && rm\*
- `||`: runs the second only if the first fails
- `;`: lets you put multiple commands all on one line running unconditionally - runs all at the same time

# Putting the error messages in a file

- Maybe you don't want the error messages to populate in your file
- we can create a `err.log` file and pipe the error into it as we try to make changes
- e.g.:
  - `cat filethatdoesnotexists >> output.txt 2>> err.log`
  - the error message is now in the log and not in the desired file

# Find

- `find`: searches any dir and sub dir
  - `find . -name file.txt`

# Grep (also finding)

- Search the contents of any file
- `grep word *.txt`: find all .txt files that contain the word "word"
- `grep -i WorD *.txt`: find all with out the case
  sensitivity
- `grep -in WorD *.txt`: find the file and show the line it is found in
- `grep -il WorD *.txt`: gives all the files that contain the word
- `grep -rli WorD .`: find all case insensitive instances within all subdirectories
- Search Recursively:
  - `greop -rli aPPle .`
- `which`
  - e.g.:`which ls` : tells about ls
- `whereis`
  - e.g.: `whereis ls` : tells where the file is

# Wildcard \*, ?, []

- all used for pattern matching aka "globbing"
- e.g.: `ls *.txt`
  - shows all txt files
- `?`: matches characters
  - e.g.:
    - `ls *.??`
    - show all files with only two end characters,as in
      - `.md, .sh, .ex`...
- `[]` shows a range of characters
  - e.g.: `ls [e-f]*`
    - shows any file that starts with e or f
  - e.g.: `ls [e-f]*.txt`
    - same but we want them to be text files only

# Accessing Bash to create alias

- commands:
  - `cd`
  - `ls - a`
  - find .bashrc and open to edit
  - add alias and restart terminal

# Git

- `git status -s`: shortened version of status, of untracked or tracked changes
- `git log --oneline`
  - `git checkout ID230482` ID found from prev. command -able to look around
  - `git checkout main` return to future
- `git checkout -- filename` : if you did not like the changes you made to this particular file this command will return it to the most recent saved version !

# Fortran
