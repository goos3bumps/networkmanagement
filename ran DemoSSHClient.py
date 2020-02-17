root@UbuntuDockerGuest-1:~# ./DemoSSHClient.py
ls -alh
date
cat newfilebyexeccommand.txt
Last login: Mon Feb 17 06:14:19 2020 from 192.168.122.172
root@UbuntuDockerGuest-2:~# ls -alh
total 36K
drwx------ 4 root root 4.0K Feb 17 06:13 .
drwxr-xr-x 1 root root 4.0K Feb 17 04:05 ..
-rw------- 1 root root  263 Feb 17 06:14 .bash_history
-rw-r--r-- 1 root root 3.1K Oct 22  2015 .bashrc
drwx------ 2 root root 4.0K Feb 17 04:20 .cache
-rw-r--r-- 1 root root   85 Feb 17 04:04 .gns3_perms
drwxr-xr-x 2 root root 4.0K Feb 17 04:19 .nano
-rw-r--r-- 1 root root  148 Aug 17  2015 .profile
-rw-r--r-- 1 root root    0 Feb 17 05:37 haha
-rw-r--r-- 1 root root  116 Feb 17 06:14 newfilebyexeccommand.txt
root@UbuntuDockerGuest-2:~# date
Mon Feb 17 06:14:37 UTC 2020
root@UbuntuDockerGuest-2:~# cat newfilebyexeccommand.txt
Mon Feb 17 06:13:58 UTC 2020
Mon Feb 17 06:14:13 UTC 2020
Mon Feb 17 06:14:19 UTC 2020
Mon Feb 17 06:14:37 UTC 2020
