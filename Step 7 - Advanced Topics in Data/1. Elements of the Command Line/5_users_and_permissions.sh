# 1.Users
whoami
id

# 2.Groups
groups
cd
ls -l

# 3.Revisiting ls
cd /
ls -l
mkdir oops
cd root


# 4.Permissions
# 5.Changing Permissions: Symbolic Notation
cd
chmod a+rwx mistery_file
chmod g+wx,o+w Trash
chmod g+x config_file_1
chmod g+x,o=r config_file_2
chmod a=rwx,o-x d*

# 6.The File Status Command
stat /home/dq/Trash
answer 0776

# 7.Changing Permissions: Octal Notation
answer 602 171 ---r--r-x
chmod 222 /home/dq/Trash


# 8.The Superuser
cal
sudo cal


# 9.Changing Ownership