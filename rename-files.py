# This program rename files in the inputed directory by removing all the numbers in the file names

import os

# Get path of files to rename
directory = raw_input('Enter the full directory path:')

# Rename function
def rename_files(directory):
  file_list = os.listdir(directory)
  print(file_list)
  # Save the current path to come back to after the rename is complete
  saved_path = os.getcwd()
  # Change to the directory where the files are located
  os.chdir(directory)

  for file_name in file_list:
    print("Old Name - "+file_name)
    print("New Name - "+file_name.translate(None, "0123456789"))
    os.rename(file_name, file_name.translate(None, "0123456789"))
  os.chdir(saved_path)

rename_files(directory)
