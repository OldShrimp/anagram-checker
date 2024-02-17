import sys, argparse

def charToPrime(ch):
    primedict = {'\n':1, ' ':1, 'a':2, 'b':3, 'c':5, 'd':7, 'e':11, 'f':13, 'g':17, 'h':19, 'i':23, 'j':27, 'k':29,
                 'l':31, 'm':37, 'n':41, 'o':43, 'p':47, 'q':53, 'r':59, 's':61, 't':67, 'u':71,
                 'v':73, 'w':79, 'x':83, 'y':89, 'z':97}
    return primedict[ch.lower()]

def strToPrimeProduct(st):
    product = 1
    for ch in st:
        product *= charToPrime(ch)
    return product

def main(argv):
    parser = argparse.ArgumentParser(description='groups lines from an input .txt file and groups them into anagrams in the output .txt file')
    parser.add_argument('input')
    parser.add_argument('output')

    args = parser.parse_args()
    inputfile = args.input
    outputfile = args.output
            
    buckets = dict()
    with open(inputfile) as dictionary:
        for line in dictionary:
            word = line.replace('\n', '')
            num = strToPrimeProduct(line)
            if not (num in buckets):
                buckets[num] = set()
            buckets[num].add(word)
    
    largest = 0
    most = 0
    most_key = 0
    with open(outputfile, 'w') as output:
        for key in buckets:
            for words in buckets[key]:
                output.write(words + '\n')
            output.write('\n')
            
            largest = max(largest, key)
            if most < len(buckets[key]):
                most = len(buckets[key])
                most_key = key
            
    print("largest word:", buckets[largest], "product:", largest)
    print("largest word group:", buckets[most_key], ", # words:", most)
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])

