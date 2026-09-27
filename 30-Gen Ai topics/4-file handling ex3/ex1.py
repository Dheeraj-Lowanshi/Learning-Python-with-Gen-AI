

import os
file_name="d:/Python/30-Gen Ai topics/4-file handling ex3/data.txt"
if os.path.exists(file_name):
    print("File is present")
else:
    print("File is not present")