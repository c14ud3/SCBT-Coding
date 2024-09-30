from hashlib import sha256
from sha3 import keccak_256
from time import time

def find_string_with_hash_starting_with_zero():
    base = "Hallo :) "
    ctr = 0

    while True:
        string_to_test = base + str(ctr) # append number
        sha = sha256(string_to_test.encode("utf-8")).hexdigest()
        if sha.startswith("0"):
            print(f"String: \"{string_to_test}\"")
            print(f"Hash: {sha.upper()}")
            return
        ctr += 1

start = time()
find_string_with_hash_starting_with_zero()
end = time()
print(f"Time needed: {(end - start)}s")