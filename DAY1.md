    Only needed the first time ever

When creating the environment for the first time:

cd /d
mkdir vagrant
cd vagrant
mkdir ubuntu
cd ubuntu
vagrant init ubuntu/jammy64
vagrant up
vagrant ssh

    Below is the complete command sequence from the beginning after opening Git Bash.

Step 1 — Go to the drive
cd /d
Step 2 — Go to the Vagrant folder
cd vagrant
Step 3 — Go to the Ubuntu project folder
cd ubuntu
Step 4 — Start the virtual machine
vagrant up

Wait until the VM starts.

Step 5 — Login to the Ubuntu VM
vagrant ssh

You will then see something like:

vagrant@ubuntu-jammy:~$

Now you are inside Ubuntu.

Step 6 — Run Linux commands (example)
ls

or

uname -a
Step 7 — Exit the VM
exit

This returns you to Git Bash.

Step 8 — Stop the VM when finished
vagrant halt

    Learn a few basic Linux commands

These are the first commands most people practice.

pwd
ls
cd /vagrant
mkdir test
cd test
touch file1.txt
ls
