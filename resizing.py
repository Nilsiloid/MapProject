# # Define the input and output file paths
# input_file_path = "sorted_class0.txt"  # Replace with the path to your input file
# output_file_path = "boundingboxes_dataset.txt"  # Replace with the desired path for the output file

# # Read the lines from the input file into a list
# with open(input_file_path, 'r') as input_file:
#     lines = input_file.readlines()

# # Create a dictionary to store the modified lines, keyed by map number
# modified_lines = {}

# # Multiply each numeric value by 640 and store the modified lines in the dictionary
# for line in lines:
#     parts = line.split()
#     if len(parts) >= 5:
#         map_number = parts[0]
#         values = [str(640 * float(value)) for value in parts[1:]]
#         modified_lines[map_number] = values

# # Sort the modified lines by map number
# sorted_lines = sorted(modified_lines.items(), key=lambda x: int(x[0].split('_')[1]))

# # Write the sorted modified lines to the output file
# with open(output_file_path, 'w') as output_file:
#     for map_number, values in sorted_lines:
#         output_file.write(f"{map_number} {' '.join(values)}\n")


input_file = "sorted_class2_new.txt"
output_file = "sorted_resized_class2_new.txt"

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        parts = line.split()
        if len(parts) >= 6:
            outfile.write(f"{parts[0]} {parts[1]} "
                          f"{float(parts[2]) * 700} {float(parts[3]) * 500} "
                          f"{float(parts[4]) * 700} {float(parts[5]) * 500}\n")
