#!/bin/bash

# Prompt user to enter file to make executable
read -p "Enter the name of the file you want to make executable: " file_name

# Check if file exists
if [ ! -e $file_name ]; then
  echo "Error: File does not exist"
  exit 1
fi

# Make file executable
chmod u+x $file_name

echo "File $file_name is now executable"
