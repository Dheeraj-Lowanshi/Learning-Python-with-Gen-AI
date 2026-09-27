

f=None
try:
    f=open("d:/Python/30-Gen Ai topics/file handling ex2/files/message3.txt","x+")
    f.write("New file created")
    f.seek(0)
    str=f.read()
    print(str)
except FileNotFoundError:
    print("Cannot create the file:")
except OSError as ex:
    print("Error in creating the file:",ex)
finally:
    if f is not None:
        f.close()
        print("File closed successfully")
