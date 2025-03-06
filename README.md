# Setting up a new VM
To begin, run the following bash command to update the package list.
```bash
sudo apt update
```
## Set up Git credentials
Run the following to set up the git username and email. 
```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```
After that, verify the configuration.
```bash
git config --global --list
```
## Generate a SSH key
This command will generate a SSH key
```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```
When prompted to chose a file location, press Enter to accept the default location "~/.ssh/id_ed25519".

Then it will ask for a passphrase, and pressing enter will bypass this step.

## Add the SSH key
This will then be used to add the SSH key to the agent.
```bash
ssh-add ~/.ssh/id_ed25519
```
## Add SSH key to github
To display the key, 
```bash
cat ~/.ssh/id_ed25519.pub
```
And then to the settings in your github go to the "SSH and GPG Keys" section and press add key. Paste the key and save.

To test the connection, run:
```bash
ssh -T git@github.com
```
If it worked the following message should appear: Hi your-username! You've successfully authenticated,...

## Clone this repository
Clone this repsository to run scripts directly.
```bash
git clone git@github.com:ycv3fh/SP25_DS5111_ycv3fh.git
cd your-repo
```
# Run Initialization Script
Run the initilization script to finish set up.
```bash
./init.sh
```
## Install a Chrome Headless Browser
First, navigate to the project directory.
If the file has not already beeen created then create it now by using the following:
```bash
nano install_chrome.sh
```
This will create the file so that now the following script can be added inside:
```bash
#!/bin/bash
set -e

# Update system package list
sudo apt update

# Install dependencies
sudo apt install -y wget curl unzip

# Download and install Chrome headless
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb || sudo apt-get -f install -y
rm google-chrome-stable_current_amd64.deb

# Verify installation
google-chrome --version
```
Make the created script executable by running:
```bash
chmod +x install_chrome.sh
```
Finally run the script
```bash
./install_chrome.sh
```
To test to ensure the script was installed correctly use the website "example.com".
```bash
google-chrome --headless --disable-gpu --dump-dom https://example.com
```
A successful output would display the website's simple html.

## Requirements

The required dependencies are already in the requirements.txt file and include pandas and lxml. To install the dependecies run the following:
```bash
pip install -r requirements.txt
```

## Set up your virtual environment with make update
To initilize the virtual environment, run
```bash
make update
```
and this will run the makefile.txt that will create the the virtual environment and install the dependencies from requirements. txt

## Test the headless browser by running job in makefile
Run the headless browser using 
```bash
make ygainers.csv
```
and this should run the headless browser, get the example.com, and save the output to a text file named "test_output.html"
To open and view the contents of the file, run
```bash
cat test_output.html
```

To view the project's structure, run
```bash
tree project_repo -I env
```
The output should like like this:
```bash
your-project-repo
├── install_chrome.sh
├── Makefile
├── requirements.txt
├── test_output.html
```
## Github Action

![Build Status](https://github.com/ycv3fh/SP25_DS5111_ycv3fh/actions/workflows/validations.yml/badge.svg)


