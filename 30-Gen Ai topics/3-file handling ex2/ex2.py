

fin=None
fout=None
try:
    fin=open("d:/Python/30-Gen Ai topics/file handling ex2/files/travel.png","rb")
    fout=open("d:/Python/30-Gen Ai topics/file handling ex2/files/newfile.png","wb")
    data=fin.read()
    fout.write(data)
except(FileNotFoundError)as ex1:
    print("Cannot create the file:",ex1)
except(OSError)as ex2:
    print("Error in creating the file:",ex2)
finally:
    if fin is not None:
        fin.close()
        print("File closed successfully")
    if fout is not None:
        print("File copied!")
        fout.close()
        print("File closed successfully")