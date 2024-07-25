
# --- Tub sonlar ---



def gen_from(n):
    while True:
        yield n
        n += 1

for i in gen_from(0):
    if i > 100:
        break
    else:
        print(i)

class Tub(object):
    def __init__(self, ntp):
        self.ntp = ntp
    def __iter__(self):
        return self
    def __next__(self):
        try:
            head = self.ntp.__next__()
            self.ntp = filter(lambda x: x % head != 0, self.ntp)
            return head
        except StopIteration as e:
            raise e
for prime in Tub(gen_from(2)):
    if prime > 100:
        break
    else:
        print(prime)
 

