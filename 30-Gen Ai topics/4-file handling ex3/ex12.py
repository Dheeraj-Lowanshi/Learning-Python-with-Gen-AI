

import os
if os.path.exists("d:/Python/30-Gen Ai topics/4-file handling ex3/data.txt"):
    if os.path.isfile("d:/Python/30-Gen Ai topics/4-file handling ex3/data.txt"):
        os.remove("d:/Python/30-Gen Ai topics/4-file handling ex3/data.txt")
        print("File deleted successfully")
    else:
        print("It is not a file")
else:
    print("File not present")