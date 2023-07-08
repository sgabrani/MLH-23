#!/bin/bash

# Check if an argument is provided
if [ $# -eq 0 ]; then
  echo "Usage: say-hello-to.sh [name]"
  exit 1
fi

# Get all the arguments and join them into a single string
name="$*"

# Print the hello message
echo "Hello, $name!"
