def main():
    number = 0
    while number != -1:
        number = getInput("Please enter any positive number: ")
        if number == -1:
            continue
        prime = isPrime(number)
        printPrime(number, prime)
        if not prime:
            even = isEven(number)
            printEven(number, even)
    else:
        print("Goodbye!")

def getInput(question):
    print(question)
    number = input()
    if number == 'exit':
        return -1
    else:
        return number
        
def isPrime(number):
    num = int(number)
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    return prime

def isEven(number):
    num = int(number)
    if num % 2 == 0:
        return True
    else:
        return False

def printPrime(number, prime):
    if prime:
        print(f"{number} is prime!")
    else:
        print(f"{number} is NOT prime.")

def printEven(number, even):
    if even:
        print(f"{number} is even!")
    else:
        print(f"{number} is odd.")
  
if __name__== "__main__": main()

