List = []
List2 = []

def main():
    infile = open('C:\\Users\\gavin\\OneDrive\\Desktop\\text.txt', 'rt')
    outfile = open('C:\\Users\\gavin\\OneDrive\\Desktop\\lines-copy.txt', 'wt')
    total = 0
    length = 0
    for line in infile:
        List = line.split()
        for x in List:
            x = int(x)
            total = total + x
            length = length + 1
    avg = total / length
    Max = max(List)
    Min = min(List)

    outfile.close()
    print(List)
    print(f"\n{total}")
    print(f"\n{avg}")
    print(f"\n{Max}")
    print(f"\n{Min}")
    print('\ndone.')

if __name__ == '__main__':
    main()