#!/usr/bin/haserl
<%in p/common.cgi %>
<%
[ -z "$GET_f" ] && append_flash "danger" "Нечего восстанавливать." && error=1

file=$GET_f
[ ! -f "/rom/${file}" ] && append_flash "danger" "Файл /rom/${file} не найден!" && error=1

[ -n "$error" ] && redirect_back

cp "/rom/${file}" "${file}"
if [ $? -eq 0 ]; then
  redirect_back "success" "Файл ${file} восстановлен до настроек по умолчанию."
else
  redirect_back "danger" "Невозможно восстановить ${file}!"
fi
%>
