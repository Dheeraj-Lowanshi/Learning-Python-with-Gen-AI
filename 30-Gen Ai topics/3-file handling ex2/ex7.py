

f=None
try:
    f=open("d:/Python/30-Gen Ai topics/file handling ex2/files/msg.txt","w+")
    data=f.read()
    print("Initial data")
    print(data)
    f.write("Gen AI\n")
    f.write("is an essential skill today")
    f.seek(0)
    data=f.read()
    print("After changing:")
    print(data)
except FileNotFoundError:
    print("Cannot create the file:")
except OSError as ex:
    print("Error in creating the file:",ex)
finally:
    if f is not None:
        f.close()
        print("File closed successfully")
