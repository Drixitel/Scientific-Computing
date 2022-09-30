# Find .SSH File from WSL

- run command explorer.exe .
- will open a file exploer from the current directory and allow the user to find required folder/files

# Public and Private key

- must match to allow access
- Public Key can go everywhere but not Private
  - for sec. reasons

# increase length of bits

- `ssh-keygen -b 4096` (bits)

# Passphrase

- create one and add sec.

# Checking if it works

Instance URL is git.ucsc.edu and it will find your info from your key

- `ssh -T git@git.ucsc.edu`
- new?
  - `yes`
  - retype previous command
