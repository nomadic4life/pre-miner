import hashlib
# import requests

import sys

from uuid import uuid4
import time

hash = {}


def proof_of_work(last_proof, difficulty, proof):
    """
    Simple Proof of Work Algorithm
    - Find a number p' such that hash(pp') contains `difficulty` leading
    zeroes, where p is the previous p'
    - p is the previous proof, and p' is the new proof
    """

    print("Searching for next proof")
    start = time.time()
    proof_1 = 0
    proof_2 = 200000000
    proof_3 = 400000000
    proof_4 = 600000000
    proof_5 = 800000000
    proof_6 = 1000000000
    proof_7 = 1200000000
    proof_8 = 1400000000
    proof_9 = 1600000000
    proof_10 = 1800000000
    while True:
        proof = {"proof": proof, "proof_1": proof_1, "proof_2": proof_2, "proof_3": proof_3, "proof_4": proof_4,
                 "proof_5": proof_5, "proof_6": proof_6, "proof_7": proof_7, "proof_8": proof_8, "proof_9": proof_9, "proof_10": proof_10}
        valid_proof(last_proof, proof, difficulty, start)
        proof_1 += 1
        proof_2 += 1
        proof_3 += 1
        proof_4 += 1
        proof_5 += 1
        proof_6 += 1
        proof_7 += 1
        proof_8 += 1
        proof_9 += 1
        proof_10 += 1

    print("Proof found: " + str(proof))
    return proof


def valid_proof(last_proof, proof, difficulty, start):
    """
    Validates the Proof:  Does hash(last_proof, proof) contain `difficulty`
    leading zeroes?
    """
    while True:
        if proof["proof_1"] == 0:
            proof["proof_1"] = 1
            proof_1 = proof["proof_1"]
            proof_2 = proof["proof_2"]
            proof_3 = proof["proof_3"]
            proof_4 = proof["proof_4"]
            proof_5 = proof["proof_5"]
            proof_6 = proof["proof_6"]
            proof_7 = proof["proof_7"]
            proof_8 = proof["proof_8"]
            proof_9 = proof["proof_9"]
            proof_10 = proof["proof_10"]
            proof_11 = 2000000000
            proof_12 = 2200000000
            proof_13 = 2400000000
            proof_14 = 2600000000
            proof_15 = 2800000000
            proof_16 = 3000000000
            proof_17 = 3200000000
            proof_18 = 3400000000
            proof_19 = 3600000000
            proof_20 = 3800000000
        else:
            proof_1 += 1
            proof_2 += 1
            proof_3 += 1
            proof_4 += 1
            proof_5 += 1
            proof_6 += 1
            proof_7 += 1
            proof_8 += 1
            proof_9 += 1
            proof_10 += 1
            proof_11 += 1
            proof_12 += 1
            proof_13 += 1
            proof_14 += 1
            proof_15 += 1
            proof_16 += 1
            proof_17 += 1
            proof_18 += 1
            proof_19 += 1
            proof_20 += 1

        guess_1 = f'{last_proof}{proof_1}'.encode()
        guess_2 = f'{last_proof}{proof_2}'.encode()
        guess_3 = f'{last_proof}{proof_3}'.encode()
        guess_4 = f'{last_proof}{proof_4}'.encode()
        guess_5 = f'{last_proof}{proof_5}'.encode()
        guess_6 = f'{last_proof}{proof_6}'.encode()
        guess_7 = f'{last_proof}{proof_7}'.encode()
        guess_8 = f'{last_proof}{proof_8}'.encode()
        guess_9 = f'{last_proof}{proof_9}'.encode()
        guess_10 = f'{last_proof}{proof_10}'.encode()
        guess_11 = f'{last_proof}{proof_11}'.encode()
        guess_12 = f'{last_proof}{proof_12}'.encode()
        guess_13 = f'{last_proof}{proof_13}'.encode()
        guess_14 = f'{last_proof}{proof_14}'.encode()
        guess_15 = f'{last_proof}{proof_15}'.encode()
        guess_16 = f'{last_proof}{proof_16}'.encode()
        guess_17 = f'{last_proof}{proof_17}'.encode()
        guess_18 = f'{last_proof}{proof_18}'.encode()
        guess_19 = f'{last_proof}{proof_19}'.encode()
        guess_20 = f'{last_proof}{proof_20}'.encode()

        guess_hash_1 = hashlib.sha256(guess_1).hexdigest()
        guess_hash_2 = hashlib.sha256(guess_2).hexdigest()
        guess_hash_3 = hashlib.sha256(guess_3).hexdigest()
        guess_hash_4 = hashlib.sha256(guess_4).hexdigest()
        guess_hash_5 = hashlib.sha256(guess_5).hexdigest()
        guess_hash_6 = hashlib.sha256(guess_6).hexdigest()
        guess_hash_7 = hashlib.sha256(guess_7).hexdigest()
        guess_hash_8 = hashlib.sha256(guess_8).hexdigest()
        guess_hash_9 = hashlib.sha256(guess_9).hexdigest()
        guess_hash_10 = hashlib.sha256(guess_10).hexdigest()
        guess_hash_11 = hashlib.sha256(guess_11).hexdigest()
        guess_hash_12 = hashlib.sha256(guess_12).hexdigest()
        guess_hash_13 = hashlib.sha256(guess_13).hexdigest()
        guess_hash_14 = hashlib.sha256(guess_14).hexdigest()
        guess_hash_15 = hashlib.sha256(guess_15).hexdigest()
        guess_hash_16 = hashlib.sha256(guess_16).hexdigest()
        guess_hash_17 = hashlib.sha256(guess_17).hexdigest()
        guess_hash_18 = hashlib.sha256(guess_18).hexdigest()
        guess_hash_19 = hashlib.sha256(guess_19).hexdigest()
        guess_hash_20 = hashlib.sha256(guess_20).hexdigest()

        rate = 0
        if proof_1 % 1000000 == 0:
            end = time.time()
            print(proof_1, end - start, "hash rate", rate)

        if proof_2 % 1000000 == 0:
            end = time.time()
            print(proof_2, end - start, "hash rate", rate)

        if proof_3 % 1000000 == 0:
            end = time.time()
            print(proof_3, end - start, "hash rate", rate)

        if proof_4 % 1000000 == 0:
            end = time.time()
            print(proof_4, end - start, "hash rate", rate)

        if proof_5 % 1000000 == 0:
            end = time.time()
            print(proof_5, end - start, "hash rate", rate)

        if proof_6 % 1000000 == 0:
            end = time.time()
            print(proof_6, end - start, "hash rate", rate)

        if proof_7 % 1000000 == 0:
            end = time.time()
            print(proof_7, end - start, "hash rate", rate)

        if proof_8 % 1000000 == 0:
            end = time.time()
            print(proof_8, end - start, "hash rate", rate)

        if proof_9 % 1000000 == 0:
            end = time.time()
            print(proof_9, end - start, "hash rate", rate)

        if proof_10 % 1000000 == 0:
            end = time.time()
            print(proof_10, end - start, "hash rate", rate)

        if proof_11 % 1000000 == 0:
            end = time.time()
            print(proof_11, end - start, "hash rate", rate)

        if proof_12 % 1000000 == 0:
            end = time.time()
            print(proof_12, end - start, "hash rate", rate)

        if proof_13 % 1000000 == 0:
            end = time.time()
            print(proof_13, end - start, "hash rate", rate)

        if proof_14 % 1000000 == 0:
            end = time.time()
            print(proof_14, end - start, "hash rate", rate)

        if proof_15 % 1000000 == 0:
            end = time.time()
            print(proof_15, end - start, "hash rate", rate)

        if proof_16 % 1000000 == 0:
            end = time.time()
            print(proof_16, end - start, "hash rate", rate)

        if proof_17 % 1000000 == 0:
            end = time.time()
            print(proof_17, end - start, "hash rate", rate)

        if proof_18 % 1000000 == 0:
            end = time.time()
            print(proof_18, end - start, "hash rate", rate)

        if proof_19 % 1000000 == 0:
            end = time.time()
            print(proof_19, end - start, "hash rate", rate)

        if proof_20 % 1000000 == 0:
            end = time.time()
            print(proof_20, end - start, "hash rate", rate)

        if guess_hash_1[:difficulty] == "0" * difficulty:

            hash[last_proof] = proof_1
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_1)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_2[:difficulty] == "0" * difficulty:

            hash[last_proof] = proof_2
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_2)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_3[:difficulty] == "0" * difficulty:

            hash[last_proof] = proof_3
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_3)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_4[:difficulty] == "0" * difficulty:

            hash[last_proof] = proof_4
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_4)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_5[:difficulty] == "0" * difficulty:

            hash[last_proof] = proof_5
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_5)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_6[:difficulty] == "0" * difficulty:

            hash[last_proof] = proof_6
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_6)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_7[:difficulty] == "0" * difficulty:

            hash[last_proof] = proof_7
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_7)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_8[:difficulty] == "0" * difficulty:

            hash[last_proof] = proof_8
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_8)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_9[:difficulty] == "0" * difficulty:

            hash[last_proof] = proof_9
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_9)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_10[:difficulty] == "0" * difficulty:
            hash[last_proof] = proof_10
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_10)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_11[:difficulty] == "0" * difficulty:

            hash[last_proof] = proof_11
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_11)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_12[:difficulty] == "0" * difficulty:

            hash[last_proof] = proof_12
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_12)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_13[:difficulty] == "0" * difficulty:

            hash[last_proof] = proof_13
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_13)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_14[:difficulty] == "0" * difficulty:

            hash[last_proof] = proof_14
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_14)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_15[:difficulty] == "0" * difficulty:

            hash[last_proof] = proof_15
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_15)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_16[:difficulty] == "0" * difficulty:

            hash[last_proof] = proof_16
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_16)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_17[:difficulty] == "0" * difficulty:

            hash[last_proof] = proof_17
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_17)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_18[:difficulty] == "0" * difficulty:

            hash[last_proof] = proof_18
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_18)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_19[:difficulty] == "0" * difficulty:

            hash[last_proof] = proof_19
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_19)
            print("hash size", len(hash))
            input("press enter to continue")

        if guess_hash_20[:difficulty] == "0" * difficulty:
            hash[last_proof] = proof_20
            print("last hash", last_proof, "new hash", hash[last_proof])
            print(guess_hash_20)
            print("hash size", len(hash))
            input("press enter to continue")


    # return guess_hash[:difficulty] == "0" * difficulty
if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0

    # Load or create ID
    # f = open("my_id.txt", "r")
    # id = f.read()
    # print("ID is", id)
    # f.close()
    # if len(id) == 0:
    #     f = open("my_id.txt", "w")
    #     # Generate a globally unique ID
    #     id = str(uuid4()).replace('-', '')
    #     print("Created new ID: " + id)
    #     f.write(id)
    #     f.close()
    auth_key = "479432788140a41ce5cb792d873f49bb1fa40212"
    # Run forever until interrupted
    proof = None
    while True:
        # Get the last proof from the server
        if proof is None:
            print("yes")
            proof = 0
        else:
            print("here", proof)
            proof += 1
        last_proof = 0
        difficulty = 7
        new_proof = proof_of_work(last_proof, difficulty, proof)


# 181000000 600.9770922660828
# 345000000 1200.2642998695374
# 222000000 738.1722693443298
# last hash 0 new hash 222768594
# 0000000e087326d26d92c5bf232b1296d9b9dccdccd439643cd1066fa6017441
# hash size 1

# 749000000 2615.0332362651825
# last hash 0 new hash 749356440
# 0000000bddd8273702982ad75c1bda20c5f5a647cd097a1999c31d4f7a025536
# hash size 1


# last hash 0 new hash 222768594
# 0000000e087326d26d92c5bf232b1296d9b9dccdccd439643cd1066fa6017441
# hash size 1
# press enter to continue
# 23000000 642.0226652622223 hash rate 0

# last hash 0 new hash 1650904045
# 00000005c6f3fe9cf7b70a34494f82972dca60d58c40ac048ad1d57e814ef0d2
# hash size 1
# press enter to continue
# 51000000 1415.8258669376373 hash rate 0

# last hash 0 new hash 1286362126
# 0000000f1f84e2014986d8a925549eac66e53340bba67dab85c7164637b0088a
# hash size 1
# press enter to continue
# 87000000 2415.0733757019043 hash rate 0

# last hash 0 new hash 749356440
# 0000000bddd8273702982ad75c1bda20c5f5a647cd097a1999c31d4f7a025536
# hash size 1
# press enter to continue
# 150000000 4154.713445663452 hash rate 0


# last hash 0 new hash 2012823217
# 000000093b3e4f44215cd2facd52b2f96626e8e07619f7e4b5715d24f6a4189d
# hash size 1
# press enter to continue
# 13000000 566.0883574485779 hash rate 0

# last hash 0 new hash 222768594
# 0000000e087326d26d92c5bf232b1296d9b9dccdccd439643cd1066fa6017441
# hash size 1
# press enter to continue
# 23000000 974.98885679245 hash rate 0

# last hash 0 new hash 2225152410
# 0000000756ffaedd9b50139bc48179d0dce7abb3861cec774de223530d092b8b
# hash size 1
# press enter to continue
# 26000000 1111.5324926376343 hash rate 0

# last hash 0 new hash 3250732665
# 000000061e316cc4d9fa0a99b2806e18c6423f78b1da2707a4f7b9bdd43e7021
# hash size 1
# press enter to continue

# last hash 0 new hash 1650904045
# 00000005c6f3fe9cf7b70a34494f82972dca60d58c40ac048ad1d57e814ef0d2
# hash size 1
# press enter to continue
# 51000000 2365.039622783661 hash rate 0

# init
# curl -X GET -H 'Authorization: Token 2e289710723b27949296f5ad3152027ecb6061f1' https://lambda-treasure-hunt.herokuapp.com/api/adv/init/

# #move
# curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"direction":"n"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/move/

# #last proof
# curl -X GET -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/

# 2e289710723b27949296f5ad3152027ecb6061f1
