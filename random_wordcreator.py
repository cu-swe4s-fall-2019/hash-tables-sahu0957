import random
import string

for i in range(10000):
    rangeint = random.randrange(1, 30, 1)
    randword = ''.join([random.choice(string.ascii_letters + string.digits)
                       for n in range(rangeint)])
    print(randword)
