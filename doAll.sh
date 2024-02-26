#!/bin/bash

echo "Running smoke tests..."
echo "Checking Node.js version..."
if node -v; then
    echo "Node.js is functioning properly."
else
    echo "Smoke test failed: There might be an issue with Node.js."
    exit 1
fi

echo "Running experiments..."

if python3 scripts/main.py; then
    echo "Experiments ran successfully."
    echo "Generating report..."
    make clean
    make report
    if [ $? -eq 0 ]; then
        echo "Report generated successfully."
    else
        echo "Something went wrong with the report generation"
        exit 1
    fi
else
    echo "Something went wrong with the application. See the log error above."
    exit 1
fi


