    Only needed the first time ever

When creating the environment for the first time:

1) cd /d
2) mkdir vagrant
3) cd vagrant
4) mkdir ubuntu
5) cd ubuntu
6) vagrant init ubuntu/jammy64
7) vagrant up
8) vagrant ssh

    Below is the complete command sequence from the beginning after opening Git Bash.

    1) — Go to the drive : cd /d

    2) — Go to the Vagrant folder : cd vagrant
    3) — Go to the Ubuntu project folder : cd ubuntu
    4) — Start the virtual machine : vagrant up

Wait until the VM starts.

5) — Login to the Ubuntu VM : vagrant ssh

You will then see something like:

vagrant@ubuntu-jammy:~$

Now you are inside Ubuntu.

6) — Run Linux commands (example)
ls

or

uname -a
7) — Exit the VM
exit

This returns you to Git Bash.

8) — Stop the VM when finished
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
