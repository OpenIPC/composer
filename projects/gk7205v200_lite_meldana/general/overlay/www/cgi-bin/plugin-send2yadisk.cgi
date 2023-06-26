#!/usr/bin/haserl
<%in p/common.cgi %>
<%
plugin="yadisk"
plugin_name="Отправить на Яндекс.Диск"
page_title="Отправить на Яндекс.Диск"
params="enabled username password path socks5_enabled"

tmp_file=/tmp/${plugin}.conf

config_file="${ui_config_dir}/${plugin}.conf"
[ ! -f "$config_file" ] && touch $config_file

if [ "POST" = "$REQUEST_METHOD" ]; then
  # parse values from parameters
  for _p in $params; do
    eval ${plugin}_${_p}=\$POST_${plugin}_${_p}
    sanitize "${plugin}_${_p}"
  done; unset _p

  ### Validation
  if [ "true" = "$email_enabled" ]; then
    [ -z "$yadisk_username" ] && flash_append "danger" "Имя пользователя Яндекс.Диска не может быть пустым." && error=11
    [ -z "$yadisk_password" ] && flash_append "danger" "Пароль Яндекс.Диска не может быть пустым." && error=12
  fi

  if [ -z "$error" ]; then
    # create temp config file
    :>$tmp_file
    for _p in $params; do
      echo "${plugin}_${_p}=\"$(eval echo \$${plugin}_${_p})\"" >>$tmp_file
    done; unset _p
    mv $tmp_file $config_file

    update_caminfo
    redirect_back "success" "Конфигарция ${plugin_name} обновлена."
  fi

  redirect_to $SCRIPT_NAME
else
  include $config_file
fi
%>
<%in p/header.cgi %>

<div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4 mb-4">
  <div class="col">
    <form action="<%= $SCRIPT_NAME %>" method="post">
      <% field_switch "yadisk_enabled" "Включить бота Яндекс.Диска" %>
      <% field_text "yadisk_username" "Имя пользователя Яндекс.Диска" %>
      <% field_password "yadisk_password" "Пароль от Яндекс.Диска" "Специальный пароль для приложения. <a href=\"https://yandex.com/support/id/authorization/app-passwords.html\">Создайте его здесь</a>." %>
      <% field_text "yadisk_path" "Путь к Яндекс.Диску" %>
      <% field_switch "yadisk_socks5_enabled" "Использовать SOCKS5" "<a href=\"network-socks5.cgi\">Конфигурация</a> доступа SOCKS5" %>
      <% button_submit %>
    </form>
  </div>
</div>

<%in p/footer.cgi %>
