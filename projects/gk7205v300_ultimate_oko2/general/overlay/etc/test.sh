#!/bin/sh

echo "start connect";
sleep 5s;
uqmi -s -d /dev/cdc-wdm0 --start-network internet --autoconnect &
echo "connect";
echo "set wwan"
ip link set wwan0 down
echo 'Y' | tee /sys/class/net/wwan0/qmi/raw_ip
ip link set wwan0 up
echo "get ip"
udhcpc -i wwan0


