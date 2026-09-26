
try:
    f=open("d:/Python/30-Gen Ai topics/file handling/files/message.txt","w")
    str=input("Type something:")
    f.write(str)
except(FileNotFoundError)as ex1:
    print("Cannot create the file:",ex1)
except(OSError)as ex2:
    print("Cannot write the data:",ex2)
finally:
    if 'f' in locals():
        f.close()
        print("File saved and closed successfully")