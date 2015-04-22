import random
from time import time

count = 0
secret = random.randint(1, 10)
start = time()
print("Gissa ett nummer mellan 1-10: \n")

while count < 5:
    print("Din gissning: \n")
    x = input()
    x = int(x)

    count = count + 1

    if x < secret:
        print("Högre!")

    if x > secret:
        print("Lägre")

    if x == secret:
        break
time_took = time() -start
if x == secret:
    print("Du gissade rätt!\n ", +secret)
    print("Tid: ", +time_took)

if x != secret:
    print("Du gissa fel fem gånger, numret var ", +secret) 
    print("Tid", +time_took)
