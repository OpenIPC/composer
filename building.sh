#!/bin/bash
#
# OpenIPC | version 2023.11.11

# Autoupdate COMPOSER repo
# Remove old building folder (for full rebuild)
# Download OpenIPC repo
# Copy files from Project Overlay
# Build Firmware
# Copy Kernel and Rootfs to Archive
# Copy Kernel and Rootfs to TFTP server


RELEASE=""
PROJECT="$1"

TFTP_STORAGE="root@172.17.32.17:/mnt/bigger-2tb/Rotator/TFTP"

COMPOSER_DIR=$(pwd)
FIRMWARE_DIR="${COMPOSER_DIR}/openipc"
TIMESTAMP=$(date +"%Y%m%d%H%M")
VERSION=$(stat -c"%Y" $0)

echo_c() {
    # 30 grey, 31 red, 32 green, 33 yellow, 34 blue, 35 magenta, 36 cyan, 37 white
    t="\e[1;$1m$2\e[0m" || t="$2"
    echo -e "$t"
}

copy_to_archive() {
    echo_c 32 "Copying files to local archive"
    mkdir -p "${COMPOSER_DIR}/archive/${PROJECT}/${TIMESTAMP}"
    cp -a \
        ${FIRMWARE_DIR}/output/images/rootfs.squashfs.* \
        ${FIRMWARE_DIR}/output/images/uImage.* \
        ${FIRMWARE_DIR}/output/images/*.tar \
        ${FIRMWARE_DIR}/output/images/openipc.*.tgz \
        ${COMPOSER_DIR}/archive/${PROJECT}/${TIMESTAMP}

    if [ -f "${FIRMWARE_DIR}/output/images/autoupdate-kernel.img" ] ; then
        cp -a ${FIRMWARE_DIR}/output/images/autoupdate* ${COMPOSER_DIR}/archive/${PROJECT}/${TIMESTAMP}
    fi

    echo_c 35 "\nAssembled firmware available in:"
    tree -C "${COMPOSER_DIR}/archive/${PROJECT}/${TIMESTAMP}"
}

copy_to_tftp() {
    echo_c 32 "\nCopying files to a TFTP server using SCP protocol"
    scp -r \
        ${FIRMWARE_DIR}/output/images/rootfs.squashfs.* \
        ${FIRMWARE_DIR}/output/images/uImage.* \
        ${FIRMWARE_DIR}/output/images/openipc.*.tgz \
        ${TFTP_STORAGE}

    if [ -f "${FIRMWARE_DIR}/output/images/autoupdate-kernel.img" ] ; then
        scp -r ${FIRMWARE_DIR}/output/images/autoupdate* ${TFTP_STORAGE}
    fi
}

select_project() {
    AVAILABLE_PROJECTS=$(ls -1 ${COMPOSER_DIR}/projects | grep '_')
    cmd="whiptail --title \"Available projects\" --menu \"Please select a project from the list below:\" 25 78 16"
    for p in $AVAILABLE_PROJECTS; do cmd="${cmd} \"$p\" \"\""; done
    PROJECT=$(eval "${cmd} 3>&1 1>&2 2>&3")
    if [ $? != 0 ]; then
        echo_c 31 "Cancelled."
        exit 1
    fi
}

copy_extra_packages() {
    extra_packages=${COMPOSER_DIR}/packages
    firmware_packages=${FIRMWARE_DIR}/general/package
    cp -afv $extra_packages/* $firmware_packages
    packages_list_file=$firmware_packages/Config.in
    for f in "$extra_packages"/*
    do
        package_name=$(basename $f)
        if ! grep -Fq "$package_name" $packages_list_file
        then
            printf 'source "$BR2_EXTERNAL_GENERAL_PATH/package/%s/Config.in"\n' $package_name >> $packages_list_file
        fi
    done
}

echo_c 37 "COMPOSER - custom OpenIPC firmware builder"
echo_c 30 "https://openipc.org/"
echo_c 30 "Version: ${VERSION}"

while [ -z "${PROJECT}" ]; do select_project; done

echo_c 31 "\nStarting a project for ${PROJECT}"
tree -C ${COMPOSER_DIR}/projects/${PROJECT}

sleep 3

echo_c 33 "\nUpdating Composer"
git pull

rm -rf openipc  # Weed work with this command
if [ ! -d "$FIRMWARE_DIR" ]; then
    echo_c 33 "\nDownloading Firmware"
    git clone --depth=1 https://github.com/OpenIPC/firmware.git "$FIRMWARE_DIR"
    cd "$FIRMWARE_DIR"
else
    echo_c 33 "\nUpdating Firmware"
    cd "$FIRMWARE_DIR"
    # git reset HEAD --hard
    # git pull --rebase
fi

echo_c 33 "\nCopying extra packages"
# cp -afv ${COMPOSER_DIR}/packages/* ${FIRMWARE_DIR}/general/package
copy_extra_packages


echo_c 33 "\nCopying project files"
cp -afv ${COMPOSER_DIR}/projects/${PROJECT}/*  ${FIRMWARE_DIR}

echo_c 33 "\nBuilding the project"
./building.sh ${PROJECT}

copy_to_archive
# copy_to_tftp
echo_c 35 "\nDone"
cd "$COMPOSER_DIR"
