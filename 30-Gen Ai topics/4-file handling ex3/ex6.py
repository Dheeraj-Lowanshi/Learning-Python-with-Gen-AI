

import os
import time

total_sec=os.path.getmtime("d:/Python/30-Gen Ai topics/4-file handling ex3/data.txt")
readable_time=time.ctime(total_sec)
print("File was last modified on:",readable_time)