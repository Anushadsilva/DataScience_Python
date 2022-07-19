#2.Write a code which accepts a sequence of words as input and prints the words in a sequence
# after sorting them alphabetically. Hint: In case of input data being supplied to the question, it should be assumed
# to be a console input.


if __name__ == '__main__':
    y = input("Enter sequence of words ").split(',')
    for name in y:
        y.sort()
        print(','.join(y))


