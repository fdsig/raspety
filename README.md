# Learning Kubernetes using Rarasperry Pi 4  cluster 
instructions on for Linux os (ubuntu)

includes a python script to automate the laborious processes and across whole cluster and terminal runnable instructions - there are various ways some of which include using the disk writer util for in ubuntu GUI to manually write over a

## Use case:

Automate set up of raspberry pi cluster with any number of raspberry pi's to verticalise (literally) the process of creating a raspberry pi cluster. This is a useful learning tool for cluster computing more generally, automation of tasks and learning amazing tools such as Kubernetes. 

## Contents

> -formatting sd
> -installing ubuntu server of x'n Raspberry Pi 4 (4gb)
> -setting up login on all via ssh.

## 1  Formatting SD card.

insert sd card and find its acces path.

```bash
df | grep sd
```
 
here sd is the characters likely to be an sd card this may change depending on media 

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

```bash
wget https://cdimage.ubuntu.com/releases/20.04.4/release/ubuntu-20.04.4-preinstalled-server-arm64+raspi.img.xz
```

#3 creating a disk image from compressed

uzing xz to decompress and then pipe into dd, /dev/sda is the location of unmounted sd card on see 'Filesystem' column above.

```bash
xzcat ubuntu-20.04.4-preinstalled-server-arm64+raspi.img.xz | sudo dd of=/dev/sda bs=32M status=progress
```
further details on this can be found [here](https://askubuntu.com/questions/1193232/how-do-i-use-an-img-xz-file-or-get-an-img-file-from-it)


UI Install:

This might be simpler that using the above, and satisfactory if like me you enjoy repetition.

- [ ] dowload ubuntu server image
- [ ] use belina etcher to flash image
- [ ] watch this video while your flashing [here](https://www.youtube.com/watch?v=GVgMM_TFeOw)
- [ ] follow instructions for seeting up microk8s [here](https://ubuntu.com/tutorials/how-to-kubernetes-cluster-on-raspberry-pi#1-overview)
- [ ]  set up images for use with kubernetes

## To Do:

- [ ] add actual bash commands
- [ ] set up mysql
- [ ] create tar file of image and deploy with wandb image 

```bash
docker save mynginx > myimage.tar
microk8s ctr image import myimage.tar
```