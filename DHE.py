sharedPrime = 23
sharedBase = 5

user1_private = 6
user2_private = 15

user1_share = (sharedBase**user1_private) % sharedPrime
user2_share = (sharedBase**user2_private) % sharedPrime

user1_secret = (user2_share**user1_private) % sharedPrime
user2_secret = (user1_share**user2_private) % sharedPrime

print(user1_secret)
print(user2_secret)
