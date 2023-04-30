#!/bin/sh

destdir="/mnt"

my_umount()
{
    if grep -qs "^/dev/$1 " /proc/mounts ; then
        yaml-cli -s ".records.enabled" "false"
#        sed -i '96s/true/false/' /etc/majestic.yaml
        unlink "/sdcard";
        unlink "/var/www/rec";
        umount "${destdir}/mmc";
        rmdir "${destdir}/mmc"
    fi

    [ -d "${destdir}/mmc" ] && rmdir "${destdir}/mmc"
}

my_mount()
{
    mkdir -p "${destdir}/mmc" || exit 1
    if ! mount -t vfat "/dev/$1" "${destdir}/mmc"; then
        # failed to mount, clean up mountpoint
        rmdir "${destdir}/mmc"
        exit 1
    fi
    echo "SD Card mounted";
    ln -s "${destdir}/mmc" "/sdcard"
    ln -s "${destdir}/mmc/records" "/var/www/rec"
    yaml-cli -s ".records.enabled" "true"
    if [ -f /sdcard/autoexe ]
    then
      /sdcard/autoexe
    fi
    if [ -f /sdcard/hardres ]
    then
      rm -f /sdcard/hardres
      flash_eraseall -j /dev/mtd4
      firstboot
    fi
}

case "${ACTION}" in
add|"")
    majex=`ps aux | grep majestic | grep -v grep`
    if [[ ! -z "$majex" ]]
      then
       echo "Stop majestic"
       dumpconfig=`echo -n "Stop majestic"`
       /etc/init.d/S95hisilicon stop
       sleep 1
    fi

    my_umount ${MDEV}
    my_mount ${MDEV}

    if [[ ! -z "$majex" ]]
      then
       echo "Start majestic" 
       dumpconfig=`echo -n "Start majestic"`
       /etc/init.d/S95hisilicon start
    fi
    ;;
remove)
    majex=`ps aux | grep majestic | grep -v grep`
    if [[ ! -z "$majex" ]]
      then
       echo "Stop majestic" 
       dumpconfig=`echo -n "Stop majestic"`
       /etc/init.d/S95hisilicon stop
      sleep 1
    fi

    my_umount ${MDEV}

    if [[ ! -z "$majex" ]]
      then
      echo "Start majestic" 
      dumpconfig=`echo -n "Start majestic"`
       /etc/init.d/S95hisilicon start
    fi
    ;;
esac
