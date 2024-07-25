

# class Fibonacci:

#     def __init__(self, thing):
#         self.thing = thing
#         self.x = 0
#         self.y = 1


#     def __iter__(self):
#         return self
    

#     def __next__(self):
#         if self.x > self.thing:
#             raise StopIteration
#         current = self.x
#         self.x, self.y = self.y, self.x + self.y
#         return current
    

# fibonacci_iterator = Fibonacci(100)


# print("Using for loop:")
# for num in fibonacci_iterator:
#     print(num)




# print("\n Using next() function:")
# fibonacci_iterator = Fibonacci(100)
# print(next(fibonacci_iterator))
# print(next(fibonacci_iterator))
# print(next(fibonacci_iterator))
# print(next(fibonacci_iterator))
# print(next(fibonacci_iterator))
# print(next(fibonacci_iterator))
# print(next(fibonacci_iterator))
# print(next(fibonacci_iterator))
# print(next(fibonacci_iterator))
# print(next(fibonacci_iterator))
# print(next(fibonacci_iterator))



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
 







    


