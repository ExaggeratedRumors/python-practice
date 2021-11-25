# 'r'
#
# open for reading (default)
#
# 'w'
#
# open for writing, truncating the file first
#
# 'x'
#
# open for exclusive creation, failing if the file already exists
#
# 'a'
#
# open for writing, appending to the end of file if it exists
#
# 'b'
#
# binary mode
#
# 't'
#
# text mode (default)
#
# '+'
#
# open for updating (reading and writing)



zoo = ["lion", "elephant", "monkey"]

if __name__ == "__main__":
    f = open("output.txt", 'a')  #'add modifier a'



    for i in zoo:
        f.write(i+'\n')          #add the whole zoo to the output.txt

    f.close()                    #close the file