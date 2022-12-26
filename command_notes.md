# Number 6: Using file roster.txt, this is all the hw it starts at 6

## Part a:

Produce an output file roster_sort_lastName.txt that lists the class members in alphabetical order of their last names, together with the rest of the fields:

- `sort roster.txt > roster_sort_lastName.txt`

Now using roster_sort_lastName.txt as input, produce three output files. First, produce roster_sort_lastName_lastName.txt which displays only the last name in each row (i.e., no first name and no email):

- `cut -d' ' -f1 roster_sort_lastName.txt > roster_sort_lastName_lastName.txt`

Next, produce an output file roster_sort_lastName_firstLastNames.txt which displays both the last and first name only in each row (i.e., no email):

- `awk NF=2 roster_sort_lastName.txt > roster_sort_lastName_firstLastNames.txt`

and finally roster_sort_lastName_firstNameEmail.txt which displays only the first name and email in each row (i.e., no last name)

- `cut -d' ' -f2- roster_sort_lastName.txt > roster_sort_lastName_firstNameEmail.txt`

## Part b:

Produce an output file roster_sort_firstName.txt that lists the class members in alphabetical order of their first names together with the rest of the fields in order

- `sort -k2 roster_sort_lastName.txt > roster_sort_firstName.txt`

Using roster_sort_firstName.txt as input, produce an output file roster_sort_firstName_firstName.txt which displays only the first name in each row (i.e., no last name and no email)

- `awk '{print $2}' roster_sort_firstName.txt > roster_sort_firstName_firstName.txt`

Next, produce an output file roster_sort_firstName_firstLastNames.txt which displays both the first and last name in order in each row (i.e., no email)

- `awk '{print $2,$1}' roster_sort_firstName.txt > roster_sort_firstName_firstLastNames.txt`

Finally, produce an output file roster_sort_firstName_lastNameEmail.txt which displays the last name and email in each row (i.e., no first name)

- `awk '{print $1,$3}' roster_sort_firstName.txt > roster_sort_firstName_lastNameEmail.txt`

## Part c:

Using roster.txt as input, produce an output file roster_sort_lastName_noDuplicate.txt sorted by last name with all duplicate students removed (hint: use sort and uniq commands)

- `sort roster.txt | uniq > roster_sort_lastName_noDuplicate.txt`

## Part d:

Write a one-line Bash command that counts the number of enrolled students, using roster_sort_lastName_noDuplicate.txt as input

- `wc -l roster_sort_lastName_noDuplicate.txt`

## Part e:

Count how many students whose last names start with C or D are enrolled in the class. Save any output to prob6_e_answer.txt

- `grep -i '^[C-D]' roster_sort_lastName_noDuplicate.txt | wc -l > prob6_e_answer.txt`

## Part f:

Produce a list of students whose last names start with L or S in reverse alphabetical order. Save your output to prob6_f_answer.txt

- `grep -i '^L\|^S' roster_sort_lastName_noDuplicate.txt | sort -r > prob6_f_answer.txt`

# Number 7

## Part a: add the following to your .bashrc

- `export AM129_PATH='/home/drixit/2022Projects/pichardomichelle-am129-fall2022'`

## Part b: add the following to your .bashrc

- `alias wcl='wc -l'`

## Extra

### Path commands: add the following to your .bashrc

- `export SCOMP_PATH='/home/drixit/2022Projects/Scientific-Computing-'`
- `export ECENOTES_PATH='/home/drixit/2022Projects/ECE8-Robotics-Notetaker'`

### Editors: add the following to your .bashrc

- `alias vs='code -r'`
- `alias cl='clear'`

### Reduce the working directory in-terminal: add the following to your .bashrc

- `PROMPT_DIRTRIM=1`

# Number 8: add the following to your .bashrc

- Added provided code \
   function cd_up() { \
   cd \$(printf "%0.0s../" $(seq 1 $1)); \
   } \
   alias 'cd..'='cd_up'

- Find a way to write a routine that tells you the pwd on N levels upper directory location s.t you do not move from your present location.

### Print upper dir: add the following to your .bashrc

    function pwd_up() {
        CURRENTDIR=$(pwd);
        cd \$(printf "%0.0s../" $(seq 1 $1));
        pwd;
        cd $CURRENTDIR;
    }
    alias 'pwd..'='pwd_up'

# Number 9:

- Created a README.md with provided text
- added `#!/usr/bin/more` to the top line
- ran the following commands,
  - mv README README.sh
  - chmod a+x README.sh
- this created an executable file from the markdown and the text appeared in terminal
- the file changed from `-rw-r--r--` to `-rwxr-xr-x`
- To execute run: `./README.sh`
