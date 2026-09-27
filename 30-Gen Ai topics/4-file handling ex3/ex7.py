

import os
import time

obj=os.stat("d:/Python/30-Gen Ai topics/4-file handling ex3/data.txt")
print("File size is:",obj.st_size,"bytes")
print("File was last modified on:",time.ctime(obj.st_mtime))