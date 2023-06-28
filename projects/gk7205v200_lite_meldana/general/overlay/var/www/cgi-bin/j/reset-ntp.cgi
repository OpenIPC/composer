#!/bin/sh
cp /rom/etc/ntp.conf /etc/ntp.conf
if [ $? -eq 0 ]; then
	payload='{"result":"success","message":"Конфигурация сброшена на настройки прошивки по умолчанию."}'
else
	payload='{"result":"danger","message":"Сброс настроек прошивки по умолчанию не удался!"}'
fi
echo "HTTP/1.1 200 OK
Content-type: application/json
Pragma: no-cache
Expires: $(TZ=GMT0 date +'%a, %d %b %Y %T %Z')
Etag: \"$(cat /proc/sys/kernel/random/uuid)\"

${payload}
"
