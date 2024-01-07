#!/bin/bash

# Initialize a flag to track overall success
success=true

# Printing Node version and checking if Node.js is functioning properly
echo "Checking Node.js version..."
if node -v; then
    echo "Node.js is functioning properly."
else
    echo "Smoke test failed: There might be an issue with Node.js."
    success=false
fi

# Printing npm version and checking if npm is functioning properly
echo "Checking npm version..."
if npm -v; then
    echo "npm is functioning properly."
else
    echo "Smoke test failed: There might be an issue with npm."
    success=false
fi

# Final message based on success of all checks
if $success ; then
    echo "Smoke test was successful!"
else
    echo "Smoke test completed with errors."
fi
