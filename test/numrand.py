import random

# while(1):
#     num = random.randrange(1,6)

#     data = "%d\n" % num

#     if num == 5:
#         break
#     f.write(data)

num = random.randrange(1,6)

redata = "%d\n" % num
with open('myfile.txt', "r+") as myfile:
    myfile.read()
    myfile.seek(0)
    myfile.write(redata)
    myfile.truncate()

myfile.close()


