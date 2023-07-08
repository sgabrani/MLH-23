#!/bin/bash

# Check if an argument is provided
if [ $# -eq 0 ]; then
  echo "Usage: find-file.sh [filename]"
  exit 1
fi

# Get the filename argument
filename="$1"

# Search for matching files in the entire file system
matches=$(find / -name "$filename" 2>/dev/null)

# Count the number of matches
match_count=$(echo "$matches" | grep -c "$filename")

# Print the number of matches
echo "Found $match_count matches:"

# Print the list of file paths
echo "$matches"
