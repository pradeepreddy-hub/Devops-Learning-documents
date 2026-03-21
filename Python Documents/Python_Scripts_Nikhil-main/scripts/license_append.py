import os

# Define the directory to search and the output file
search_directory = '/home/ubuntu/python/hadoop'
output_file = '/home/ubuntu/license_append.txt'

# Define the file patterns you want to search for (like LICENSE.txt, etc.)
license_file_patterns = ['LICENSE.txt']

# Open the output file in append mode
with open(output_file, 'a') as outfile:
    # Write the initial header to the output file (if needed)
    outfile.write("License files content:\n\n")

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(search_directory):
        for file in files:
            # Check if the file starts with "LICENSE" (case insensitive)
            if file.upper().startswith("LICENSE"):
                file_path = os.path.join(root, file)
                
                # Print to console in the required format
                print(f"Path of the license file is: {file_path}")
                print("---------------------------------------------")
                print("content of the license file is:")
                print("---------------------------------------------")              
                # Read and print the content of the license file
                with open(file_path, 'r') as license_file:
                    content = license_file.read()
                    print(content)
                    print("\n")  # Add a newline between different license files
                
                # Write to the output file in the required format
                outfile.write(f"Path of the license file is: {file_path}\n")
                outfile.write("content of the license file is:\n")
                outfile.write(content)
                outfile.write("\n\n")  # Add a newline between different license files

print(f"License contents have been appended to {output_file}.")

