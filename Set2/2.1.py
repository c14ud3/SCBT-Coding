from hashlib import sha256
from sha3 import keccak_256

## Problem 2.1 (a) ##
keccak = keccak_256() # init
keccak.update(b'') # set empty binary string
print(f"2.1 (a): {keccak.hexdigest()}") # output hexadecimal value


## Problem 2.1 (b) ##
strings = (
    "The Senate shall be composed of two Senators from each State, chosen by the Legislature thereof, for six Years; and each Senator shall have one Vote.",
    "The Senate shall be composed of two Senators from each State, chosen by the Legislature thereof, for six Years, and each Senator shall have one Vote."
)

for idx, string in enumerate(strings):
    sha = sha256() # create SHA256 object
    sha.update(string.encode('utf-8')) # set string
    print(f"2.1 (b) {idx + 1}: {sha.hexdigest()}")
