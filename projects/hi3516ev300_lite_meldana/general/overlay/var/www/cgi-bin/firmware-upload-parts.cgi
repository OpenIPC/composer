#!/usr/bin/haserl --upload-limit=5120 --upload-dir=/tmp
<%in p/common.cgi %>
<%
sysupgrade_date=$(ls -lc --full-time /usr/sbin/sysupgrade | xargs | cut -d' ' -f6)
sysupgrade_date=$(time_epoch "$sysupgrade_date")

file="$POST_parts_file"
file_name="$POST_parts_file_name"
error=""

case "$POST_parts_type" in
kernel)
  maxsize=2097152
  magicnum="27051956"
  new_sysupgrade_date=$(time_epoch "2021-12-07")
  cmd="sysupgrade --kernel=/tmp/${file_name} --force_ver"
  ;;
rootfs)
  maxsize=5242880
  magicnum="68737173"
  new_sysupgrade_date=$(time_epoch "2022-02-22")
  cmd="sysupgrade --rootfs=/tmp/${file_name} --force_ver --force_all"
  ;;
*)
  error="Пожалуйста, выберите тип файла и загрузите его снова!"
  ;;
esac

[ -z "$file_name"  ] && error="Файл не найден! Вы не забыли загрузить?"
[ ! -r "$file" ] && error="Невозможно прочитать загруженный файл!"
[ "$(stat -c%s $file)" -gt "$maxsize" ] && error="Загруженный файл слишком большой! $(stat -c%s $file) > ${maxsize}."
[ "$magicnum" -ne "$(xxd -p -l 4 $file)" ] && error="Магический номер файла не совпадает. Вы загрузили неправильный файл? $(xxd -p -l 4 $file) != $magicnum"
[ "$sysupgrade_date" -lt "$new_sysupgrade_date" ] && error="Для этой функции требуется последняя версия инструмента sysupgrade. Сначала обновите прошивку."

if [ -n "$error" ]; then
  redirect_back "danger" "$error"
else %>
<%in p/header.cgi %>
<pre class="bg-light p-4 log-scroll">
<%
xl "mv $file /tmp/${file_name}"
$cmd
%>
</pre>
<a class="btn btn-primary" href="/">Вернуться на главную</a>
<% fi %>
<%in p/footer.cgi %>
