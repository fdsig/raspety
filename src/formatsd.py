
from subprocess import CalledProcessError, Popen,PIPE, check_output
from pathlib import Path
from sys import stdout
from xml.etree.ElementTree import PI


cont = 'y'

while cont=='y':
    ps = Popen(('df'), stdout=PIPE)
    out = Popen(('grep','sd'), stdin=ps.stdout,stdout=PIPE,stderr=PIPE)
    #ps.wait()
    out_str, err = out.communicate()
    out_str = out_str.decode('utf8')
    location = out_str.split(' ')[0]
    print(location)

    while 'sd' in location:
        mounted = out_str.split('%')[-1].strip('\n').replace(' ', '')
        location = out_str.split(' ')[0]
        try:
            unmount = check_output(['umount',mounted])
            ps = Popen(('df'), stdout=PIPE)
            out = Popen(('grep','sd'), stdin=ps.stdout,stdout=PIPE,stderr=PIPE)
            #ps.wait()
            out_str, err = out.communicate()
            out_str = out_str.decode('utf8')
        except CalledProcessError:
            print('nothing to unmount')
            
        print(location)

    get, url = 'wget','https://cdimage.ubuntu.com/releases/20.04.4/release/ubuntu-20.04.4-preinstalled-server-arm64+raspi.img.xz'

    #3 cretating a disk image from compressed
    if not Path(url.split('/')[-1]).exists:
        get = check_output([get,url], stdin=ps.stdout)

    unpack = 'xzcat','ubuntu-20.04.4-preinstalled-server-arm64+raspi.img.xz'

    imager = 'dd', 'of=/dev/sda bs=32M status=progress'

    img_un = Popen(unpack,stdout=PIPE,stderr=PIPE)
    imager = Popen(imager,stdin=img_un.stdout, stdout=PIPE)

    print(imager.communicate())

    mnt = 'mount', '/dev/sda1', 'sd'

    cont = input('do you want to continue formating? (y,n)')


#command = f'sudo umount {mounted} && mkfs.vfat -F32 -v {location}'
#os.system(command)