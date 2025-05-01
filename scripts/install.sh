#!/bin/bash

set -e # Exit on any error

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

# Install directory
INSTALL_DIR="$HOME/.local/bin"


# Create installation directory if it doesn't exist
mkdir -p "$INSTALL_DIR"

# Copy the main script files
cp "$PARENT_DIR/main.py" "$INSTALL_DIR"
cp "$PARENT_DIR/organizer.py" "$INSTALL_DIR"
cp "$PARENT_DIR/file_utils.py" "$INSTALL_DIR"
cp "$PARENT_DIR/reports.py" "$INSTALL_DIR"

# Create the organize script in the installation directory
cat > "$INSTALL_DIR/organize" << 'EOF' || { echo "Failed to create organize script"; exit 1; }
#!/bin/bash
python3 "$HOME/.local/bin/main.py" "$@"
EOF

# Make the script executable
chmod +x "$INSTALL_DIR/organize" || { echo "Failed to make script executable"; exit 1; }

# Add to PATH if not already present
if ! grep -q "export PATH=\"\$PATH:\$HOME/.local/bin\"" "$HOME/.bashrc"; then
    echo 'export PATH="$PATH:$HOME/.local/bin"' >> "$HOME/.bashrc" || { echo "Failed to update PATH"; exit 1; }
    echo "Added $INSTALL_DIR to PATH in $HOME/.bashrc."
else
    echo "$INSTALL_DIR is already in your PATH."
fi

echo "Installation complete! Please restart your terminal or run:"
echo "source ~/.bashrc"

