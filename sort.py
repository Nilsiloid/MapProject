# Define the file path
file_path = "output1.txt"

# Read the file into a list of lines
with open(file_path, 'r') as file:
    lines = file.readlines()

# Extract the prefixes from each line and create a list of tuples (prefix, original line)
lines = [(line.split(': ', 1)[0], line) for line in lines]

# Sort the lines based on the extracted prefixes
lines = sorted(lines, key=lambda pair: pair[0])

# Extract the original lines after sorting
sorted_lines = [line for _, line in lines]

# Define the output file path
output_file_path = "sorted_class1_new.txt"

# Write the sorted data to a new file
with open(output_file_path, 'w') as output_file:
    output_file.writelines(sorted_lines)


# Define the file path for input and output
# input_file_path = "output2.txt"
# output_file_path = "output2_sorted.txt"

# # Function to convert and rewrite lines
# def convert_line(line):
#     parts = line.split(': ')
#     prefix_parts = parts[0].split('_')
#     new_line = prefix_parts[0] + '_' + prefix_parts[1] + ' ' + parts[1]
#     return new_line

# # Read lines from the input file and convert them
# with open(input_file_path, 'r') as input_file:
#     lines = input_file.readlines()

# converted_lines = [convert_line(line) for line in lines]

# # Write the converted lines to the output file
# with open(output_file_path, 'w') as output_file:
#     output_file.writelines(converted_lines)
