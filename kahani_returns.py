
kahani = ""
while True:
    data = input('enter a story')
    if len(data) == 0:
        print('khatam.. tata.. byebyeee!!!!')
        break
    kahani += data + "\n"

with open('file.txt','w') as f:
    f.write(kahani)