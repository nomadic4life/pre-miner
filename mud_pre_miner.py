from threading import Thread
from multiprocessing import Process, current_process, freeze_support
import hashlib
# import requests

import sys
import os

from uuid import uuid4
import time

process_id = os.getpid()

# def valid_proof(last_proof, proof, difficulty):
#     """
#     Validates the Proof:  Does hash(last_proof, proof) contain `difficulty`
#     leading zeroes?
#     """
#     guess = f'{last_proof}{proof}'.encode()
#     guess_hash = hashlib.sha256(guess).hexdigest()
#     return guess_hash[:difficulty] == "0" * difficulty


# def proof_of_work(last_proof, difficulty):
#     """
#     Simple Proof of Work Algorithm
#     - Find a number p' such that hash(pp') contains `difficulty` leading
#     zeroes, where p is the previous p'
#     - p is the previous proof, and p' is the new proof
#     """

#     print("Searching for next proof")
#     proof = 0
#     while valid_proof(last_proof, proof, difficulty) is False:
#         proof += 1

#     print("Proof found: " + str(proof))
#     return proof


coins_mined = 0
pre_mined = {}


class Miner ():
    def __init__(self, last_proof=0, base=0, difficulty=1, multiplier=0, multiply_rate=10000000):
        self.base = base
        self.last_proof = last_proof
        self.difficulty = difficulty
        self.multiplier = multiplier
        self.multiply_rate = multiply_rate

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def set_last_proof(self, last_proof):
        self.last_proof = last_proof

    def proof_of_work(self):
        print("Searching for next proof")
        proof = self.base
        proof_string = self.full_char_cycle(proof)
        while self.valid_proof(proof, proof_string) is False:
            self.lambda_hash_rate(proof, proof_string)
            proof += 1
            self.proof = proof
            proof_string = self.full_char_cycle(
                proof, self.multiplier, proof_string)

        print("Proof found: " + str(proof_string))
        return proof_string

    def proof_of_work_mulitpier(self):
        print("Searching for next proof")
        proof = self.base
        self.proof = proof
        proof_string_list = [""] * (self.multiplier + 1)
        # for index in range(self.multiplier + 1):
        #     proof_string_list[index] = self.set_char(index)
        # print(proof_string_list)
        found = False
        while found is False:
            for multiply in range(self.multiplier + 1):
                set_multiply = multiply * self.multiply_rate
                proof_string_list[multiply] = self.set_char(multiply, proof)
                # proof_string_list[multiply] = self.full_char_cycle(
                #     proof, set_multiply, proof_string_list[multiply])
                if self.instance_of_Proof(proof, set_multiply, proof_string_list[multiply]):
                    value = self.multiplier + proof
                    found = True
                    break
                else:
                    proof_string_list[multiply]
            proof += 1
            # print(proof, proof_string_list)
            self.proof = proof
            self.lambda_hash_rate(proof, proof_string_list)
        return value

    def valid_proof(self, proof, proof_string):
        # self.lambda_hash_rate(proof)
        guess = f'{self.last_proof}{proof_string}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        if guess_hash[:self.difficulty] == "0" * self.difficulty:
            self.end = time.time()
            self.found_proof(proof, proof_string)

        return guess_hash[:self.difficulty] == "0" * self.difficulty

    def found_proof(self, proof, proof_string):
        duration = self.end - self.start
        proof_hash = self.proof * (self.multiplier + 1)
        LHR = proof_hash / duration
        if self.difficulty not in pre_mined:
            pre_mined[self.difficulty] = {}

        pre_mined[self.difficulty][self.last_proof] = proof
        print("Lambda Hash rate:", LHR)
        print("new proof: ", proof, "proof string: ", proof_string, "last proof: ", self.last_proof, "difficulty: ", self.difficulty,
              "time to mine: ", duration, "size of pre-mind: ", len(pre_mined))
        print(pre_mined)
        input("press enter to continue")

    def mine(self):
        while True:
            self.start = time.time()
            if self.multiplier != 0:
                self.proof_of_work_mulitpier()
            else:
                self.proof_of_work()

    def run(self):
        self.mine()

    def lambda_hash_rate(self, proof, proof_string):
        # if proof % 55294 == 0:
        #     print(proof_string, len(proof_string))
        if proof % 1000000 == 0 and proof != 0:
            self.end = time.time()
            duration = self.end - self.start
            proof = proof * (self.multiplier + 1)
            LHR = proof / duration
            print(self.multiplier)
            print("Lambda Hash rate:", LHR,
                  proof_string, len(proof_string), self.proof)

    def instance_of_Proof(self, proof, multiplier=0, proof_string=""):
        proof = multiplier + proof
        return self.valid_proof(proof, proof_string)

    def full_char_cycle(self, proof, multiplier=0, string=""):
        proof_range = 55295
        proof = multiplier + proof
        num = proof % proof_range
        pointer = 0
        size = len(string)
        text = chr(num)
        # print(size)

        if num == 0:
            if size == 0:
                string = f'{text}{string}'
                # print("here", proof)
            else:
                while True:
                    if size - 1 >= pointer:
                        current = size - 1 - pointer
                        value = string[current: len(string) - pointer]
                        value = ord(value)
                        # print("here test", value)
                        value += 1
                    else:

                        text = chr(num)
                        string = f'{text}{string}'
                        size = len(string)
                        pointer = 0
                        break

                    if value == proof_range:
                        # print("testing proof range")
                        value = 0
                        text = chr(value)
                        current = size - 1 - pointer
                        string = f'{string[ : current]}{text}{string[current + 1 : ]}'
                        pointer += 1
                    else:
                        # print("test")
                        text = chr(value)
                        current = size - 1 - pointer
                        string = f'{string[ : current]}{text}{string[current + 1 : ]}'
                        pointer = 0
                        break

        else:
            # print("hereereer")
            text = chr(num)
            current = size - 1 - pointer
            string = f'{string[ : current]}{text}{string[current + 1 : ]}'

        # if num == 65:
        #     print(string)

        return string

    def set_char(self, multiplier, proof):
        proof = multiplier * self.multiply_rate + proof
        # print(proof)
        string = ""
        while proof >= 55295:
            if proof >= 55295:
                num = proof % 55295
                text = chr(num)
                string = f'{text}{string}'
                proof = (proof // 55295)

        if proof != 0:
            num = (proof % 55295) - 1
        else:
            num = (proof % 55295)
        text = chr(num)
        string = f'{text}{string}'
        return string


miner = Miner(last_proof=0, difficulty=7, multiplier=23)
miner2 = Miner(last_proof=10, difficulty=6, multiplier=14)

miner2.mine()

# t = Thread(target=miner.mine)
# t2 = Thread(target=miner2.mine)

# t.start()
# t2.start()

# print("testing threading here")
# miner.test_print()


# def test(message):
#     print(message)
#     print("this is a process test")


# print("starting process")
# process = Process(target=miner.mine, args=(pre_mined,))
# process2 = Process(target=miner2.mine, args=(pre_mined,))


# if __name__ == '__main__':
#     freeze_support()
#     process.start()
#     process2.start()


# 40
# Lambda Hash rate: 379233.5600740309
# Lambda Hash rate: 378802.13133801345
# new proof:  222768594 last proof:  0 difficulty:  7 time to mine:  299.6613392829895 size of pre-mind:  1
# {7: {0: 222768594}}
# press enter to continue


# 0
# Lambda Hash rate: 362587.56464069075
# Lambda Hash rate: 362583.56940740696
# new proof:  222768594 last proof:  0 difficulty:  7 time to mine:  614.3924126625061 size of pre-mind:  1
# {7: {0: 222768594}}
# press enter to continue

# 1
# Lambda Hash rate: 329108.26273119106
# Lambda Hash rate: 329109.43829436373
# new proof:  222768594 last proof:  0 difficulty:  7 time to mine:  1292.9960021972656 size of pre-mind:  1
# {7: {0: 222768594}}
# press enter to continue

# 20
# Lambda Hash rate: 374306.00849751756
# Lambda Hash rate: 374245.63379712164
# new proof:  222768594 last proof:  0 difficulty:  7 time to mine:  1277.6113622188568 size of pre-mind:  1
# {7: {0: 222768594}}
# press enter to continue


# 22
# Lambda Hash rate: 372516.2946834552
# Lambda Hash rate: 372244.43595218577
# new proof:  222768594 last proof:  0 difficulty:  7 time to mine:  171.06410694122314 size of pre-mind:  1
# {7: {0: 222768594}}
# press enter to continue

# 23
# Lambda Hash rate: 370608.88344447844
# Lambda Hash rate: 371482.3722102683
# new proof:  222768594 last proof:  0 difficulty:  7 time to mine:  178.86785745620728 size of pre-mind:  1
# {7: {0: 222768594}}
# press enter to continue

# print("working")
# num = "가다"
# test = num.encode()
# test = test.decode()
# # test = num.decode("binary")
# print(test)

# # num = 65
# # text = f'\{hex(num)}'
# text = text.encode()
# text = text.decode()
# print(text)

# text = chr(1114111)
# print(text)
# stuff = "aaa"
# text = text.encode()
# print(text)
# arr = '0'
# for num in range(1114111 + 1):
#     if num == 1114111:
#         arr = f'1{arr}'
#         print("working", num % 1114111, arr)
#     if num == 1114110:
#         print("well???", num % 1114111)

# num = 0
# string = ""
# while True:
#     if num == 1114112:
#         num = 0
#     if num == 0:
#         if len(string) == 0:
#             text = chr(num)
#             string = f'{text}{string}'
#             size = len(string)
#             pointer = 0
#         else:
#             while True:
#                 if size - 1 >= pointer:
#                     current = size - 1 - pointer
#                     value = string[current: len(string) - pointer]
#                     value = ord(value)
#                     value += 1
#                 else:
#                     text = chr(num)
#                     string = f'{text}{string}'
#                     size = len(string)
#                     pointer = 0
#                     break

#                 if value == 1114112:
#                     value = 0
#                     text = chr(value)
#                     current = size - 1 - pointer
#                     string = f'{string[ : current]}{text}{string[current + 1 : ]}'
#                     pointer += 1
#                 else:
#                     text = chr(value)
#                     current = size - 1 - pointer
#                     string = f'{string[ : current]}{text}{string[current + 1 : ]}'
#                     pointer = 0
#                     break

#     else:
#         text = chr(num)
#         current = size - 1 - pointer
#         string = f'{string[ : current]}{text}{string[current + 1 : ]}'

#     if num == 65:
#         print(string)

#     num += 1


# 0
# Lambda Hash rate: 263913.11183234776 ੏勐 2 146000000
# Lambda Hash rate: 263905.2750931785
# new proof:  146634723 proof string:  ਗ਼먾 last proof:  10 difficulty:  7 time to mine:  555.6339218616486 size of pre-mind:  1
# {7: {10: 146634723}}
# press enter to continue


# 횽 2
# Ł횼 2
# ł횻 2
# Ń횺 2
# 0
# Lambda Hash rate: 252472.0246613568 ń燅 2 18000000
# ń횹 2
# Ņ횸 2
# ņ횷 2
# Ň횶 2
# ň횵 2
# ŉ횴 2
# Ŋ횳 2
# ŋ횲 2
# Ō횱 2
# ō횰 2
# Ŏ횯 2
# ŏ횮 2
# Ő횭 2
# ő횬 2
# Œ횫 2
# œ횪 2
# Ŕ횩 2
# ŕ효 2


# Lambda Hash rate: 242330.78308374452 ['k淫', 'Ġ䴠', 'Ǖⱕ', 'ʊஊ', '̾슾', 'ϳꇳ', 'Ҩ脨', '՝恝', 'ؒ㾒', 'ۇệ', 'ݻ헻', '࠰따', 'ࣥ鑥', 'চ玚',
#  '\u0a4f勏'] 15 6000000
# Lambda Hash rate: 242140.23850022943
# new proof:  146634723 proof string:  ਗ਼먾 last proof:  10 difficulty:  7 time to mine:  411.0049846172333 size of pre-mind:  1
# {7: {10: 146634723}}
# press enter to continue
