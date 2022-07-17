input_file = r"surface_data_final.dat"
limit = 10
counter = 0

with open(input_file, 'r') as file:
    for line in file:
        if counter == limit:
            break
        else:
            print(f"[{counter+1}]: {line}")
        counter += 1