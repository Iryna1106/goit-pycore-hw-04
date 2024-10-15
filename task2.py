

def get_cats_info(path):
    cats_info = []

    with open ("test2.txt", "w") as file:
        file.write ("60b90c1c13067a15887e1ae1,Tayson,3\n 60b90c2413067a15887e1ae2,Vika,1\n 60b90c2e13067a15887e1ae3,Barsik,2\n 60b90c3b13067a15887e1ae4,Simon,12\n 60b90c4613067a15887e1ae5,Tessi,5")
    
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_dict = {"id": cat_id, "name": name, "age": age}
                cats_info.append(cat_dict)

        return cats_info

    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return []
    except ValueError:
        print("Error: Incorrect file format.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
cats_info = get_cats_info("test2.txt")
print(cats_info)

