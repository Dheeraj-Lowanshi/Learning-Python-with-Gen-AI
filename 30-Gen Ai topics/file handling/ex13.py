def read_nums(filename):
    f=None
    try:
        f=open(filename,"r")
        lines=f.readlines()
        if not lines:
            raise ValueError("File is empty")
        numbers=[]
        for value in lines:
            values=value.strip()
            try:
                numbers.append(int(values))
            except ValueError:
                print(f"Skipping {values}")
        if not numbers:
            raise ValueError("No valid numbers found")
        for n in numbers:
            print(n)
        total=sum(numbers)
        avg=total/len(numbers)
        print(f"Sum is: {total}")
        print(f"Average is: {avg}")
    except (ValueError) as ex1:
        print("Error:",ex1)
    except (FileNotFoundError) as ex2:
        print("Error:",ex2)
    except (OSError) as ex3:
        print("Error in reading:",ex3)
    except (Exception) as ex4:
        print("Unexpected error:",ex4)
    finally:
        if f is not None:
            f.close()
            print("File closed successfully")


read_nums("d:/Python/30-Gen Ai topics/file handling/files/data.txt")
