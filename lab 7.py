def main():
    fil = str(open('numbers.txt', 'rt'))
    nums = fil.split(' ')
    nums = list(map(int, nums))
    s = (sum(nums))
    b = s / (len(nums))
    print(f''' 
    Sum is {s}
    Average is {b})
    largest number is ''', max(nums),
    '''smallest number is ''', min(nums))
main()