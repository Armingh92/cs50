x = input('What is the Answer to the Great Question of life, the Universe, and Everything? ').strip().lower()
if x == '42':
    print('yes')
elif x == 'forty-two':
    print('yes')
elif x == 'forty two':
    print('yes')
else:
    print('no')