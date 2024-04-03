import os
# Define the directory containing the .txt files
directory = '/home/nilay/IIITB/SEM5/Data Vis Project/dataset/accuracy_values/data_new/test/labels'

# Creating the output files
output_file0 = 'output0.txt'
output_file1 = 'output1.txt'
output_file2 = 'output2.txt'

# Opening output files for writing
with open(output_file0, 'w') as out0, open(output_file1, 'w') as out1, open(output_file2, 'w') as out2:
    # Iterating over all .txt files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)

            # Open the current file for reading
            with open(file_path, 'r') as file:
                # Read all lines in the file
                lines = file.readlines()

            for line in lines:
                line = line.strip()  # Remove leading/trailing whitespace
                if not line:
                    continue  # Skip empty lines

                # Split the line and get the first number
                parts = line.split()
                if parts:
                    try:
                        first_number = int(parts[0])
                        # Write the line to the appropriate output file based on the first number
                        if first_number == 0:
                            out0.write(f'{filename}: {line}\n')
                        elif first_number == 1:
                            out1.write(f'{filename}: {line}\n')
                        elif first_number == 2:
                            out2.write(f'{filename}: {line}\n')
                    except ValueError:
                        print(f"Skipping line: {line} in file {filename} (Not a valid integer)")

print("Segregation complete.")