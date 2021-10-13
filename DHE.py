integer = input("Input an integer")
def is_prime(n):
    for i in range(2, int(integer)):
        if int(integer) % i == 0:
            return False
    else:
        return True
def primitve_root(prime):
    primitveRange= range(1,prime)
    primitiveRoots = []
    for i in range(1,prime):
        modulus =
if is_prime(integer) == True:
    sharedPrime = int(integer)
else:
    print("Not a prime number")

sharedBase = 5

user1_private = 6
user2_private = 15

user1_share = (sharedBase**user1_private) % sharedPrime
user2_share = (sharedBase**user2_private) % sharedPrime

user1_secret = (user2_share**user1_private) % sharedPrime
user2_secret = (user1_share**user2_private) % sharedPrime

print(user1_secret)
print(user2_secret)
