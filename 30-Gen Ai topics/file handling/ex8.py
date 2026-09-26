f=None
try:
    f=open("d:/Python/30-Gen Ai topics/file handling/files/message.txt","w")
    print("Tyepe something and to stop press ENTER:")
    lines=0
    while True:
        text=input()
        if text=="":
            break
        f.write(text+"\n")
        lines+=1
    print("Total lines saved in file:",lines)
except(FileNotFoundError)as ex1:
    print("Cannot create the file:",ex1)
except(OSError)as ex2:
    print("Cannot write the data:",ex2)
finally:
    if f is not None:
        f.close()
        print("File closed successfully")