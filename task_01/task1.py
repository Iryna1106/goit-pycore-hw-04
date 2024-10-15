def total_salary(path):
    # with open ("test.txt", "w") as file:
    #     file.write (" Alex Korp,3000\n Nikita Borisenko,2000\n Sitarama Raju,1000")
    try:
        total = 0
        count = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                _, salary = line.strip().split(',')
                total += int(salary)
                count += 1

        if count == 0:
            return (0, 0) 
            
        average = total / count
        return (total, average)

    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return (0, 0)
    except ValueError:
        print("Error: Incorrect file format.")
        return (0, 0)
    except Exception as e:
        print(f"An error occurred: {e}")
        return (0, 0)
total, average = total_salary('task_01/test.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

