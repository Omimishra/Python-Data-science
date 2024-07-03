kahani = ""
while True:
    data = input('enter a story')
    if len(data) == 0:
        print('khatam.. tata.. byebyeee!!!!')
        break
    kahani += data + "\n"
print ('meri kahani')
print (kahani)

