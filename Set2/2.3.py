from hashlib import sha3_256
from time import time

def find_string_with_hash_starting_with_zero(zeros = 1):
    base = "Hallo :) "
    ctr = 0

    while True:
        string_to_test = base + str(ctr) # append number
        sha = sha3_256(string_to_test.encode("utf-8")).hexdigest()
        if sha.startswith(zeros * "0"):
            print(f"----- {zeros} zeros -----")
            print(f"String: \"{string_to_test}\"")
            print(f"Hash: {sha.upper()}")
            return
        ctr += 1

def experiment(zeros):
    start = time()
    find_string_with_hash_starting_with_zero(zeros)
    end = time()
    print(f"Time needed: {int (end - start)}s")

experiment(7)
experiment(8)