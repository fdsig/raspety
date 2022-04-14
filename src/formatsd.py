
import os
import subprocess

ps = subprocess.Popen(('df'), stdout=subprocess.PIPE)
out = subprocess.check_output(('grep', 'sd'), stdin=ps.stdout)
ps.wait()

out_str = out.decode('utf8')

mounted = out_str.split('%')[-1].strip('\n').replace(' ', '')
location = out_str.split(' ')[0]
print(location)
cont = input('do you want to continue formating?')
print(cont)

command = f'sudo umount {mounted} && mkfs.vfat -F32 -v {location}'
os.system(command)