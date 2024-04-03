# with open('predictions-best.txt', 'r') as file:
#     lines = file.readlines()

# files = {'0': open('file_A.txt', 'w'), '1': open('file_B.txt', 'w'), '2': open('file_C.txt', 'w')}

# for line in lines:
#     words = line.split()
#     if len(words) > 1:
#         key = words[1]
#         files[key].write(line)

# # Close all files
# for file in files.values():
#     file.close()

# Specify your input and output file names
input_file = 'file_C.txt'
output_file = 'sorted_label2.txt'

# Read lines from the input file
with open(input_file, 'r') as file:
    lines = file.readlines()

# Sort lines by the first word of each line
lines.sort(key=lambda x: x.split()[0])

# Write the sorted lines to the output file
with open(output_file, 'w') as file:
    file.writelines(lines)

print(f"File '{input_file}' has been sorted and saved to '{output_file}'.")

