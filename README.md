# Setting up a new VM
To begin, run the following bash command to update the package list.
$sudo apt update

## Set up Git credentials
Run the following to set up the git username and email. 

$git config --global user.name "Your Name"
$git config --global user.email "your-email@example.com"

After that, verify the configuration.
$git config --global --list

## Generate a SSH key
This command will generate a SSH key
$ssh-keygen -t ed25519 -C "your-email@example.com"

When prompted to chose a file location, press Enter to accept the default location "~/.ssh/id_ed25519".

Then it will ask for a passphrase, and pressing enter will bypass this step.

##Add the SSH key
This will then be used to add the SSH key to the agent.
$ssh-add ~/.ssh/id_ed25519

##Add SSH key to github
To display the key, 
$cat ~/.ssh/id_ed25519.pub

And then to the settings in your github go to the "SSH and GPG Keys" section and press add key. Paste the key and save.

To test the connection, run:
$ssh -T git@github.com

If it worked the following message should appear: Hi your-username! You've successfully authenticated,...

## Clone this repository
Clone this repsository to run scripts directly.

$git clone git@github.com:ycv3fh/SP25_DS5111_ycv3fh.git
$cd your-repo

# Run Initialization Script
Run the initilization script to finish set up.

$./init.sh
