from time import time


import time

def fibo_gen(max: int):
    n1 = 0
    n2 = 1
    counter = 0
    max = max
    try:
        while True:
            if counter > max:
                raise StopIteration        
            elif counter == 0:
                counter += 1
                yield n1
            elif counter == 1:
                counter += 1
                yield n2
            else:
                aux = n1 + n2
                n1, n2 = n2, aux
                counter += 1
                yield aux
    except StopIteration:
        print("Fin iteración")

if __name__ == "__main__":
    fibonacci = fibo_gen(5)
    for element in fibonacci:
        print(element)
        time.sleep(1) 