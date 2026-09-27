

f=None
lines=0
try:
    f=open("d:/Python/30-Gen Ai topics/file handling ex2/files/message2.txt","w+")
    print("Type your text and to stop press ENTER:")
    while True:
        str=input()
        if str=="":
            break
        f.write(str+"\n")
        lines+=1
    print(f"Total lines saved {lines}")
    print("Data saved in file")
    input("Press any key to read the files...")
    f.seek(0)
    lines=0
    while True:
        str=f.readline()
        if str=="":
            break
        print(str.strip())
        lines+=1
    print(f"Total lines read {lines}")
except FileNotFoundError:
    print("Cannot create the file:")
except OSError as ex:
    print("Error in creating the file:",ex)
finally:
    if f is not None:
        f.close()
        print("File closed successfully")
