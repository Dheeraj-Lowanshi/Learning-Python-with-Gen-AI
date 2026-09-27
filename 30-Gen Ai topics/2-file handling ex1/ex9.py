f=None
try:
    f=open("d:/Python/30-Gen Ai topics/file handling/files/message.txt","r")
    lines=0
    while True:
        text=f.readline()
        if text=="":
            break
        print(text,end="")
        lines+=1
    print("Total lines read:",lines)
except(FileNotFoundError)as ex1:
    print("Cannot create the file:",ex1)
except(OSError)as ex2:
    print("Cannot write the data:",ex2)
finally:
    if f is not None:
        f.close()
        print("File closed successfully")