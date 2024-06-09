# start_project.sh
#!/bin/bash
cd $(PWD)||/path/to/my_project
direnv allow


# Check if .zshrc exists in the project directory
if [ -f .zshrc ]; then
    # Start a new zsh session with the project-specific .zshrc
    zsh --rcs .zshrc; then eval "$(direnv hook zsh)"

else
    echo "No .zshrc file found in the project directory."
fi
