import sys, argparse

def charToPrime(ch):
    if not ch.isalpha():
        return 1
    
    primedict = {'e':2, 't':3, 'a':5, 'o':7, 'i':11, 'n':13, 's':17, 'h':19, 'r':23, 'd':27, 'l':29,
                 'c':31, 'u':37, 'm':41, 'w':43, 'f':47, 'g':53, 'y':59, 'p':61, 'b':67, 'v':71,
                 'k':73, 'x':79, 'j':83, 'q':89, 'z':97}
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

