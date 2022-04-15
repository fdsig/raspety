# Learning Kubernetes using Rarasperry Pi 4  cluster 
instructions on for Linux os (ubuntu)

includes a python script to automate the labouriouse processes and across whole cluster and terminal runnable instructions - there are various ways some of which include using the disk writter util for in unubut GUI to manually write over a

## Use case:

Automate settup of rasberry pi cluster with any number of rasberry pi's to verticalise (litterally) the process of creating a rasberry pi cluster. This is a usfull learning tool for cluster computing more generallly, automation of tasks and learning amazing tools such as Kubernetes. 

## Contents

> -formatting sd
> -installing ubuntu server of x'n Rasperry Pi 4 (4gb)
> -setting up login on all via ssh.

## 1  Formatting SD card.

insert sd card and find its acces path.

```bash
df | grep sd
```
 
here sd is the charachters likely to be an sd card this may change depending on media 

output will look something like

```bash
Filesystem      1k-blocks     used Available  Use% Mounted
/dev/sda        62571552       32  62571520   1% /media/frida/5360-3F30
```

then unmount using umount:

```bash
sudo umount /media/frida/5360-3f30
```

format card using mkfs

```bash
sudo mkfs.vfat -F32 -v /dev/sda
```
#2 getting ubuntu server or other raspberry py compatible os.

you can choose your falvours [here](https://ubuntu.com/download/raspberry-pi)



#3 cretating a disk image from compressed

uzing xz to decompress and then pipe into dd, /dev/sda is the location of unmounted sd card on see 'Filesystem' column above.

```bash
xzcat ubuntu-20.04.4-preinstalled-server-arm64+raspi.img.xz | sudo dd of=/dev/sda bs=32M status=progress
```
further details on this can be found [here](https://askubuntu.com/questions/1193232/how-do-i-use-an-img-xz-file-or-get-an-img-file-from-it)
