

f=None
try:
    f=open("d:/Python/30-Gen Ai topics/file handling ex2/files/msg.txt","a+")
    f.seek(0)
    data=f.read()
    print("File data:",data)
    f.seek(-1,2)
except FileNotFoundError:
    print("Cannot create the file:")
except OSError as ex:
    print("Error in creating the file:",ex)
finally:
    if f is not None:
        f.close()
        print("File closed successfully")
