#!/bin/bash
#
# Example for download U-Boot: https://github.com/OpenIPC/firmware/releases/download/latest/u-boot-gk7205v200-universal.bin


if [ -n "$1" ]; then
    PROJECT=$1
else
    echo -e "\n\nPlease select you project in command line:\n"
    ls archive | tr ' ' '\n'
    exit 0
fi


UBOOT=$(find ~/composer/archive/${PROJECT} -name "u-boot-*.bin")
KERNEL=$(find ~/composer/archive/${PROJECT} -name "uImage.*" | sort | tail -n 1)
ROOTFS=$(find ~/composer/archive/${PROJECT} -name "rootfs.squashfs.*" | sort | tail -n 1)


echo -e "\n\nCreate fullflash dump for ${PROJECT} project\n\nUsed components:\n"
echo -e "${UBOOT}\n${KERNEL}\n${ROOTFS}\n"

openipc/general/scripts/compile4programmer.sh ${UBOOT} ${KERNEL} ${ROOTFS} 16
