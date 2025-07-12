#!/bin/bash
set -e

# Create a directory for the build
mkdir -p build

# Zip the application files
zip -r build/ttbt1-framework.zip . -x ".git/*" ".github/*" "tests/*" "report.md"
