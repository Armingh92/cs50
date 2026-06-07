# a ,e ,i ,o ,u

# salam --> slm

vowls = ["a","e","i","o","u"]
word = input('input: ')
for i in word:
    if i.lower() in vowls:
        word = word.replace(i,'')

print('output:', word)