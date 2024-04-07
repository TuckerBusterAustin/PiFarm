#!/bin/bash

SSHPASS='password' # Replace with your actual password

# Directory where the git repository is cloned
REPO_DIR="/home/tucker/PiFarm/"

# Subdirectory within the repository to sync
SUB_DIR="piweb"

# Destination directory on linuxmachine2
DEST_DIR="pifarm@<IP>:/var/www/html/piweb/piweb"

# Navigate to the repository directory
cd "$REPO_DIR" || exit

# Pull the latest changes
git pull

# Navigate to the subdirectory
cd "$SUB_DIR" || exit

# Push the changes to linuxmachine2
# Note: the trailing slash after '.' specifies to sync the contents of the current directory, not the directory itself
sshpass -p "$SSHPASS" rsync -avz --delete -e "ssh -o StrictHostKeyChecking=no" . "$DEST_DIR"
