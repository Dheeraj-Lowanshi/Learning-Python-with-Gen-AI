def read_emp(filename):
    f=None
    try:
        f=open("d:/Python/30-Gen Ai topics/file handling/files/emp.csv","r")
        lines=f.readlines()
        if not lines:
            raise ValueError("File is empty")
        employees=[]
        salaries=[]
        for line in lines:
            values=line.strip().split(",")
            try:
                name,sal=line.split(",")
                sal=eval(sal)
                employees.append((name,sal))
                salaries.append(sal)
            except ValueError:
                print(f"Skipping {line}")
        if not employees:
            raise ValueError("No valid employees data found")
        print("\nEmployee Data")
        for emp in employees:
            print(f"Name: {emp[0]}, Salary: {emp[1]}")

        highest=max(salaries)
        lowest=min(salaries)
        avg=sum(salaries)/len(salaries)
        print(f"Highest salary: {highest}")
        print(f"Lowest salary: {lowest}")
        print(f"Average salary: {avg}")
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
        


read_emp("d:/Python/30-Gen Ai topics/file handling/files/emp.txt")