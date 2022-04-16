
from subprocess import Popen,PIPE, check_output
from pathlib import Path
from sys import stdout
from xml.etree.ElementTree import PI
ps = Popen(('df'), stdout=PIPE)
out = Popen(('grep','sd'), stdin=ps.stdout,stdout=PIPE,stderr=PIPE)
#ps.wait()
out_str, err = out.communicate()
out_str = out_str.decode('utf8')

while 'sd' in out_str:
    ps = Popen(('df'), stdout=PIPE)
    out = Popen(('grep','sd'), stdin=ps.stdout,stdout=PIPE,stderr=PIPE)
    #ps.wait()
    out_str, err = out.communicate()
    out_str = out_str.decode('utf8')
    mounted = out_str.split('%')[-1].strip('\n').replace(' ', '')
    location = out_str.split(' ')[0]
    print(location)

get, url = 'wget','https://cdimage.ubuntu.com/releases/20.04.4/release/ubuntu-20.04.4-preinstalled-server-arm64+raspi.img.xz'

if 'mounted' in globals():
    unmount = check_output(['umount',mounted])

    print(unmount)

#3 cretating a disk image from compressed
if not Path(url.split('/')[-1]).exists:
    get = check_output([get,url], stdin=ps.stdout)

unpack = 'xzcat' , 'ubuntu-20.04.4-preinstalled-server-arm64+raspi.img.xz'

imager = 'dd', 'of=/dev/sda bs=32M status=progress'

img_un = Popen(unpack,stdout=PIPE,stderr=PIPE)
imager = Popen(imager,stdin=img_un.stdout, stdout=PIPE)

imager.communicate()


#cont = input('do you want to continue formating?')


#command = f'sudo umount {mounted} && mkfs.vfat -F32 -v {location}'
#os.system(command)