def count_a(text):
    '''
    get a string and returns the numbers thst characters repeat.
    '''
    count = 0
    for i in text:
        if i == 'a':
            count += 1
    return count

print(count_a('hello what are you doing?'))