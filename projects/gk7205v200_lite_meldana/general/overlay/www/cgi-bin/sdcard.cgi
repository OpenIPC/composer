#!/usr/bin/haserl
<%in p/common.cgi %>
<% page_title="SD-карта" %>
<%in p/header.cgi %>
<%
ls /dev/mmc* >/dev/null 2>&1
if [ $? -ne 0 ]; then
%>
<div class="alert alert-danger">
  <h4>Эта камера поддерживает SD-карту?</h4>
  <p>В вашей камере нет слота для SD-карты или SD-карта не вставлена.</p>
</div>
<%
else
  card_device="/dev/mmcblk0"
  card_partition="${card_device}p1"
  mount_point="${card_partition//dev/mnt}"
  error=""
  _o=""

  if [ -n "$POST_doFormatCard" ]; then
%>
<div class="alert alert-danger">
  <h4>ВНИМАНИЕ! Форматирование SD-карты требует времени.</h4>
  <p>Пожалуйста, не обновляйте эту страницу. Дождитесь завершения форматирования раздела!</p>
</div>
<%
    if [ "$(grep $card_partition /etc/mtab)" ]; then
      _c="umount $card_partition"
      _o="${_o}\n${_c}\n$($_c 2>&1)"
      [ $? -ne 0 ] && error="Не удается размонтировать раздел SD-карты."
    fi

    if [ -z "$error" ]; then
      _c="echo -e 'o\nn\np\n1\n\n\nw'|fdisk $card_device"
      _o="${_o}\n${_c}\n$($_c 2>&1)"
      [ $? -ne 0 ] && error="Не удается создать раздел SD-карты."
    fi

    if [ -z "$error" ]; then
      _c="mkfs.vfat -v -n OpenIPC $card_partition"
      _o="${_o}\n${_c}\n$($_c 2>&1)"
      [ $? -ne 0 ] && error="Не удается отформатировать раздел SD-карты."
    fi

    if [ -z "$error" ] && [ ! -d "$mount_point" ]; then
      _c="mkdir -p $mount_point"
      _o="${_o}\n${_c}\n$($_c 2>&1)"
      [ $? -ne 0 ] && error="Не удается создать точку монтирования SD-карты."
    fi

    if [ -z "$error" ]; then
      _c="mount $card_partition $mount_point"
      _o="${_o}\n${_c}\n$($_c 2>&1)"
      [ $? -ne 0 ] && error="Не удается перемонтировать раздел SD-карты."
    fi

    if [ -n "$error" ]; then
      report_error "$error"
      [ -n "$_c" ] && report_command_info "$_c" "$_o"
    else
      report_log "$_o"
    fi
%>
<a class="btn btn-primary" href="/">DВернуться на главную</a>
<% else %>
<h4>Разделы SD-карты</h4>
<%
partitions=$(df -h | grep 'dev/mmc')
echo "<pre class=\"small\">${partitions}</pre>"

if [ -n "$partitions" ]; then
%>
<h4>Просмотр файлов на этих разделах</h4>
<div class="mb-4">
<%
IFS=$'\n'
for i in $partitions; do
#  _mount="${i##* }"
  _mount=$(echo $i | awk '{print $6}')
 echo "<a href=\"file-manager.cgi?cd=${_mount}\" class=\"btn btn-primary\">${_mount}</a>"
 unset _mount
done
IFS=$IFS_ORIG
unset _partitions
%>
</div>
<% fi %>

<h4>Отформатировать SD-карту</h4>
<div class="alert alert-danger">
  <h4>ВНИМАНИЕ! Форматирование уничтожит все данные на SD-карте.</h4>
  <p>Убедитесь, что у вас есть резервная копия, если вы собираетесь использовать данные в будущем.</p>
  <form action="<%= $SCRIPT_NAME %>" method="post">
    <% field_hidden "doFormatCard" "true" %>
    <% button_submit "Форматировать SD-карту" "danger" %>
  </form>
</div>
<%
  fi
fi
%>
<%in p/footer.cgi %>
