import re
print('Hello Python lesson')

def get_number(userstr):
    # rawstr = input('Enter a number: ')
    try:
        inputVal = int(userstr)
    except:
        inputVal = -1

    if inputVal >= 0:
        print(inputVal, 'is a nice number')
    else :
        print('Not a Number')

def print_smallest():
    smallest = None
    print("Before:", smallest)
    for itervar in [3, 41, 2, 12, 9, 74, 15, 1]:
        if smallest is None or itervar < smallest:
            smallest = itervar
    print("Smallest:", smallest)

def loop_exercise():
    num = 0
    count = 0
    total = 0.0

    while True:
        userval = input('Enter number: ')
        if userval == "done":
            break
        try:
            flval = float(userval)
        except:
            print('Invalid Input')
            continue
        print('Float Val:', flval)
        count = count + 1
        total = total + flval
    print('Total:', total, 'Count:', count, 'Average:', total / count)

def strings_details():
    test = 'Hallo Python'
    print(test[0:4])
    print(type(test))
    # print(dir(test))

def reading_files():
    file = open('../data/testFile.txt') # File handle
    def count_file_lines():
        count = 0
        for line in file:
            count = count + 1
            if not line.startswith('Hi'):
                continue
            print(line.rstrip())
        print('Line counts:', count)
    
    def count_file_characters():
        charfile = open('../data/testFile.txt') # File handle
        chars = charfile.read()
        print('File contains', len(chars), 'characters')
        # quit()

    count_file_lines()
    count_file_characters()

def list_section():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = a + b

    newlist = []
    newlist.append('sleep')
    newlist.append('now')

    print(c[1:4])
    print(c)
    print(len(c))
    print(newlist)
    print('awake' in newlist)

def dictionaries():
    dates = {"Fri": 20, "Thu": 6, "Sat": 1}
    exists = "Fri" in dates
    list_dates = list(dates) # convert dictionary to list
    vals = dates.values()
    print(dates.keys()) # Returns list of keys
    print(dates.values()) # Returns list of values
    print(dates.items()) # Returns List of Tuples
    print(exists)
    print('List Dates:', list_dates)

    for key, value in dates.items():
        print(key, value)

    counts = dict()
    names = ['Sam', 'Rob', 'Jul', 'Amy', 'Happy', 'Sam', 'Sam', 'Rob', 'Jul']
    for name in names:
        counts[name] = counts.get(name, 0) + 1
    print(counts)

def dictionaries_exercise():
    # count words in this file
    dic_file = open('../data/testFile2.txt')
    word_counts = dict()
    for line in dic_file:
        words = line.split()
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
    
    big_word = None
    highest_count = None
    for key, value in word_counts.items():
        if highest_count is None or value > highest_count:
            big_word = key
            highest_count = value
    # print(word_counts)
    print('The word with biggest count is:', big_word, 'with:', highest_count, 'occurences')

def tuples_section():
    (a, b) = ('Sam', 'Jul')
    print(b)
    # Sort list of tuples
    alph = {'a': 12, 'b': 2, 'c': 5, 'd': 20}
    # count words in this file
    dic_file = open('../data/testFile2.txt')
    word_counts = dict()
    for line in dic_file:
        words = line.split()
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
    
    tmp_list = list()
    for k, v in word_counts.items():
        tmp_list.append((v, k))
    tmp_list = sorted(tmp_list, reverse=True)
    # print( sorted( [ (v, k) for k, v in word_counts.items() ], reverse=True ))
    print('Sorted:', tmp_list[:3])

def regex_section():
    text = 'My, 2 favourite, numbers are 19 and 28,'
    s = 'A message from csev@umich.edu to cwen@iupui.edu about meet'
    fnum = re.findall('[0-9]+', text)
    tg = re.findall('[aEIMOU]', text) # Find any of the characters in the [] as single or in a word
    gd = re.findall('^M.+?,', text)
    emails = re.findall('\\S+@\\S+', s)
    dom = re.findall('^A message from .*@([^ ]*)', s)
    print(fnum)   
    print('Found:', gd) 
    print('EMAILS:', emails)
    print('Domains:', dom) 

def networking_section():
    ne = dict()
# get_number('78')
# get_number('yt y')
# print_smallest()
# loop_exercise()
# strings_details()
# reading_files()
# list_section()
# dictionaries()
# dictionaries_exercise()
# tuples_section()
regex_section()


print('All done!')

