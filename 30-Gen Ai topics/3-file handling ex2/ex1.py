

f=None
try:
    f=open("d:/Python/30-Gen Ai topics/file handling ex2/files/travel.png","rb")
    data=f.read()
    print(data)
    print(type(data))
except(FileNotFoundError)as ex1:
    print("Cannot create the file:",ex1)
except(OSError)as ex2:
    print("Error in creating the file:",ex2)
finally:
    if f is not None:
        f.close()
        print("File closed successfully")