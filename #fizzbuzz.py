#fizzbuzz

def fizzbuzz():
    # divide by 3 fizz 
    # divide by 5 buzz
    # 3 and 5 fizzbuzz
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue
        if i % 3 == 0 :
            print("Fizz")
            continue
        if i % 5 == 0:
            print("Buzz")
            continue
        else:
            print(i)
            



if __name__ == '__main__':
    fizzbuzz()

