

import os
for f in os.listdir():
    try:
        if os.path.isfile(f) and f.endswith(".txt"):
            os.remove(f)
            print(f"{f} deleted successfully")
        else:
            print(f"skipping {f}")
    except PermissionError as e1:
        print(f"Could not delete {f} because {e1}")
        