

f=None
try:
    f=open("d:/Python/30-Gen Ai topics/file handling ex2/files/msg.txt","r+")
    data=f.read()
    print(data)
    f.seek(0)
    f.write("Hello\n")
    f.write("From\n")
    f.seek(0)
    data=f.read()
    print(data)
except FileNotFoundError:
    print("Cannot create the file:")
except OSError as ex:
    print("Error in creating the file:",ex)
finally:
    if f is not None:
        f.close()
        print("File closed successfully")
