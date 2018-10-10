# main function 
def main():
    number = ''
    while number != 'exit':
        number = getinput('choose a number:')
        if number == 'exit':
            break
        isprime(number)
        printprime(number)
        if isprime(number) is False:
            iseven(number)
            printeven(number)
        else: continue
# asks user for a number
def getinput(question):
    number = (input(question))
    return number;
# finds out if its prime
def isprime(number):
    factor = 2
    number = int(number)
    while number % factor != 0:
        if number == 1:
            break
        factor = factor + 1
    if number != factor and number != 1:
        return False
    else:
        return True
# if not prime, finds out if even   
def iseven(number):
    number = int(number)
    if number % 2 == 0:
        return True
    else:
        return False
# prints whether is prime or not
def printprime(number):
    if isprime(number) is True:
        print(f'{number} is a prime number')
    elif isprime(number) is False:
        print(f'{number} is not a prime number')
# if not prime, prints whether is even or not
def printeven(number):
    if iseven(number) is True:
        print(f'{number} is even')
    elif iseven(number) is False:
        print(f'{number} is not even')
main()
print('sayonara')