    INSIDE : vagrant@ubuntu-jammy:~$
  
1) create 5 files with same name - touch devtext {1..5} .txt
2) ls
3) copy files - cp file1.txt file2.txt
4) copy directories - cp -r source_folder destination_folder
5) To know more about any commands we use : command --help (example : cp --help , ls --help , )
6) move file command - mv devtext1 ops (premission denied if ops present else system interpreted it as renaming the file because there was no folder named ops)
7) pwd
8) uptime
9) free -m
10) ls
11) uptime
12) free -m > ops.txt (> used to overwrite the data && >> used to concat)
13) cat ops.txt 
14) uptime > ops.txt
15) cat ops.txt
16) free -m >> ops.txt
17) cat ops.txt
18)**Try this example**: echo "Start of file >> ops.txt then use echo "Start of file > ops.txt"
