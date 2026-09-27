
try:
    with open("d:/Python/30-Gen Ai topics/file handling ex2/files/message4.txt","w") as f:
        f.write("I am learning File Handling")
except(FileNotFoundError)as ex1:
    print("Cannot create the file:",ex1)
except(OSError)as ex2:
    print("Cannot write the data:",ex2)