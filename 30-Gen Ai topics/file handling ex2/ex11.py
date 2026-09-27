
def increment_salaries(filename):
    f=None
    try:
        f=open(filename,"r+")
        lines=f.readlines()
        if not lines:
            raise ValueError("File is empty")
        updated_list=[]
        for line in lines:
            line=line.strip()
            try:
                name,salary=line.split(",")
                salary=eval(salary)
                new_salary=salary*1.25
                updated_list.append(f"{name},{new_salary}\n")
            except ValueError:
                print(f"Skipping {line}")
        if not updated_list:
            raise ValueError("No valid record found")
        f.seek(0)
        f.writelines(updated_list)
        print("Salaries updated successfully")
    
    except (ValueError) as ex1:
        print("Error:",ex1)
    except (FileNotFoundError) as ex2:
        print("Cannot open file:",ex2)
    except (OSError) as ex3:
        print("Cannot update the file:",ex3)
    except (Exception) as ex4:
        print("Unexpected error:",ex4)
    finally:
        if f is not None:
            f.close()
            print("File closed successfully")



increment_salaries("d:/Python/30-Gen Ai topics/file handling ex2/files/emp.csv")
