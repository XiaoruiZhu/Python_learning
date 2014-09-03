#!/usr/bin/python
# Filename: backup_ver1.py

import os
import time

# 1. the files and directories to be backed are specified in a list
source = ['/home/jmz/python','/home/jmz/R']
# If you are using Windows, use source = [r'C:\Documents',r'D:\Work'] or something like that

# 2. The backup must be stored in a main backup directory
target_dir = '/home/jmz/python/doc/'

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current data and time.
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. We use the zip command (in Unix/Linux) to put the file in a zip archive.
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'
