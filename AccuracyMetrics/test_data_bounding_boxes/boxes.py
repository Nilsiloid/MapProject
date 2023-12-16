# Read data from the file
with open('sorted_resized_class2_new.txt', 'r') as file:
    lines = file.readlines()

# Process and modify the data
modified_lines = []
i=0
for line in lines:
    i+=1
    # Split the line into individual elements
    elements = line.split()

    # Extract values
    label = elements[0]
    value1 = int(elements[1])
    value2 = int(float(elements[2]))
    value3 = int(float(elements[3]))
    value4 = int(float(elements[4]))
    value5 = int(float(elements[5]))

    if i==1:
        print(label)
        print(value1)
        print(value2)
        print(value3)
        print(value4)
        print(value5)

    # Perform modifications
    # modified_value1 = value2 - (value4//2)
    # if i==1:
    #     print(value2)
    #     print(value4)
    #     print(modified_value1)
    # modified_value2 = value3 - (value5//2)

    # Create the modified line
    modified_line = f"{label} {value1} {value2} {value3} {value4} {value5}\n"
    modified_lines.append(modified_line)

# Save the modified data back to the file
with open('box2.txt', 'w') as file:
    file.writelines(modified_lines)
