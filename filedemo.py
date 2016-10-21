import os
# fout = open('output.txt', 'w')
# line_1= "how many roads must a man walk down \n"

# fout.write(line_1)

# line_2="before you cal him a man?"
# fout.write(line_2)

# fout.close()


# print(os.path.exists('output.txt'))

# print(os.path.isdir('exercises'))

# def walk2(dirname):
#     """Prints the names of all files in 
#     dirname and its subdirectories.

#     dirname: string name of directory
#     """

#     count= 0
#     for root, dirs, files in os.walk(dirname):
#         for filename in files:
#             print(os.path.join(root, filename))
#             count +=1
#     print(count)

# walk2(os.getcwd())

try:
    fin = open('bad_file')
except: 
    print('something went wrong')

print('still works here.')

