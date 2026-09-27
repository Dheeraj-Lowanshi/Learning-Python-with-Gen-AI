f=None
try:
    f=open("d:/Python/30-Gen Ai topics/file handling/files/message.txt","r")
    my_list=f.readlines()
    for str in my_list:
        print(str.strip())
    print("Total lines read:",len(my_list))
except(FileNotFoundError)as ex1:
    print("Cannot create the file:",ex1)
except(OSError)as ex2:
    print("Cannot write the data:",ex2)
finally:
    if f is not None:
        f.close()
        print("File closed successfully")