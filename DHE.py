integer = input("Input an integer: ")
def is_prime(n):
    for i in range(2, int(integer)):
        if int(integer) % i == 0:
            print("Not a prime number")
            return False
    else:
        return True
def primitive_root(prime):
    primitveRange= range(1,prime)
    primitiveRoots = []
    num_to_check = 0
    for each in range(1,prime):
        num_to_check += 1
        possible_roots = []
        for i in range(1,prime):
            modulus = (num_to_check**i) % prime
            possible_roots.append(modulus)
            clean_possible_roots = set(possible_roots)
            if len(clean_possible_roots) == len(range(1,prime)):
                primitiveRoots.append(num_to_check)
    print(primitiveRoots)
if is_prime(integer) == True:
    sharedPrime = int(integer)
base = list(primitive_root(sharedPrime))
sharedBase = base[0]

user1_private = 6
user2_private = 15

user1_share = (sharedBase**user1_private) % sharedPrime
user2_share = (sharedBase**user2_private) % sharedPrime

user1_symmetric = (user2_share**user1_private) % sharedPrime
user2_symmetric = (user1_share**user2_private) % sharedPrime

print(user1_symmetric)
print(user2_symmetric)
primitive_root(23)
