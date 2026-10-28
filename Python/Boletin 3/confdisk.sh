#!/bin/bash
##Script de configuración disco /dev/sdb de 200GB
##Particionado
/bin/echo -e "o\nn\np\n1\n\n+100G\nn\ne\n2\n\n\nn\n\n+60G\nn\n\n\nt\n6\nc\nw\n" | /sbin/fdisk /dev/sdb
##Instalamos herramientas necesarias para xfs y FAT32
/bin/apt update && /bin/apt install xfsprogs dosfstools -y
##Instalar los FS
/sbin/mkfs.ext4 /dev/sdb1
/sbin/mkfs.xfs /dev/sdb5
/sbin/mkfs.vfat /dev/sdb6
##Configuramos las etiquetas a los FS
/sbin/e2label /dev/sdb1 DATOS
/sbin/xfs_admin -L ALMACEN /dev/sdb5
/sbin/fatlabel /dev/sdb6 INTERCAMBIO
##Crear directorios para montar FS
/bin/mkdir /mnt/datos
/bin/chmod 777 /mnt/datos
/bin/mkdir /mnt/almacen
/bin/chmod 777 /mnt/almacen
/bin/mkdir /media/cosas
/bin/chmod 777 /media/cosas
##Modificar archivo /etc/fstab para montar los FS al inicio
/bin/echo -e "/dev/sdb1\t/mnt/datos\text4\tdefaults\t0\t0" | tee -a /etc/fstab
/bin/echo -e "/dev/sdb5\t/mnt/almacen\txfs\tdefaults\t0\t0" | tee -a /etc/fstab
/bin/echo -e "/dev/sdb6\t/media/cosas\tvfat\tdefaults,rw,umask=0\t0\t0" | tee -a /etc/fstab
#Y las montamos ahora
/bin/mount -a
systemctl daemon-reload