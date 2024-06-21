#!/bin/bash

# Enable exit on error
set -e

# Define the URL and output path
MINICONDA_URL="https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh"
OUTPUT_PATH="$HOME/miniconda.sh"
INSTALL_PATH="$HOME/miniconda"

# Download Miniconda installer
echo "Downloading Miniconda installer..."
wget "$MINICONDA_URL" -O "$OUTPUT_PATH"

# Install Miniconda
echo "Installing Miniconda..."
bash "$OUTPUT_PATH" -b -p "$INSTALL_PATH"

# Check if the installation directory exists
if [ ! -d "$INSTALL_PATH" ]; then
  echo "Error: Installation directory $INSTALL_PATH does not exist."
  exit 1
fi

# Initialize conda
echo "Initializing conda..."
"$INSTALL_PATH/bin/conda" init "$(echo $SHELL | awk -F '/' '{print $NF}')"

# Verify conda installation
if ! "$INSTALL_PATH/bin/conda" --version; then
  echo "Error: Conda installation failed."
  exit 1
fi

echo 'Successfully installed miniconda...'
echo -n 'Conda version: '
"$INSTALL_PATH/bin/conda" --version

echo -e '\n'
exec bash