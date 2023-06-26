

### BARESIP

```
baresip2 -v -f /etc/baresip
```

### SYSUPGRADE

```
sysupgrade --rootfs=/tmp/rootfs.squashfs.gk7205v200 --force_all
```


### ROADMAP

1. Установить на плату CamHi с процессором GK7205V200 прошивку Ultimate по инструкции с сайта OpenIPC
2. Записать при помощи SCP рутовую систему с Baresip в каталог /tmp на камере
3. Выполнить команду sysupgrade --rootfs=/tmp/rootfs.squashfs.gk7205v200 --force_ver
4. После старта системы установить пароль и MAC в WEB интерфейсе (если этого не сделано ранее)
5. В файле /etc/baresip/accounts прописать свой SIP аккаунт (может быть несколько одновременно)
6. Запустить в консоли SIP агента baresip2 -v -f /etc/baresip
7. Для набора номера использовать комбинацию в консоли d 12345678



