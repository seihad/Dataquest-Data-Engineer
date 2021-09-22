# # 2.The * Wildcard
# cd ~/brats
# ls v*

# # 3.The ? Wildcard
# cd /home/dq/brats
# ls ????

# # 4.Escaping Characters
# cd ~/brats
# cp augustus a\*
# cp tv 't?'
# ls 'a*' 't?'

# # 5.The Wildcard []
# cd /home/dq/brats
# ls *[!aiueo]

# # 6.Other Wildcards
# ls *[[:alnum:]]

# # 7.Summary and Practice
# cd /home/dq/practice/wildcards
# ls
# mkdir html_files archive data
# mv *l html_files
# mv 201[!9]* archive
# mv 2019* dat

# # 8.Searching for Files
# find / -name '*.b64'
# mv /sqlite-autoconf-3210000/tea/win/you_found_it.b64 ~