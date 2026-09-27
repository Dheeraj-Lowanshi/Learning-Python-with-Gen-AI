

f=None
try:
    f=open("d:/Python/30-Gen Ai topics/file handling ex2/files/stud.dat","rb")
    data=f.read()
    print(data)
except FileNotFoundError:
    print("Cannot create the file:")
except OSError:
    print("Error in creating the file:")
finally:
    if f is not None:
        f.close()
        print("File closed successfully")
