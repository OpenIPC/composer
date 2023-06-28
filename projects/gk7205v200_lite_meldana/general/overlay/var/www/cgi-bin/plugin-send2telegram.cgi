#!/usr/bin/haserl
<%in p/common.cgi %>
<%
plugin="telegram"
plugin_name="Отправить в Телеграм"
page_title="Отправить в Телеграмm"
params="enabled token as_attachment as_photo channel caption socks5_enabled"

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
  if [ "true" = "$telegram_enabled" ]; then
    [ -z "$telegram_token"   ] && flash_append "danger" "Токен Telegram не может быть пустым." && error=11
    [ -z "$telegram_channel" ] && flash_append "danger" "Канал Telegram не может быть пустым." && error=12
  fi

  if [ -z "$error" ]; then
    # create temp config file
    :>$tmp_file
    for _p in $params; do
      echo "${plugin}_${_p}=\"$(eval echo \$${plugin}_${_p})\"" >>$tmp_file
    done; unset _p
    mv $tmp_file $config_file

    update_caminfo
    redirect_back "success" "Конфигурация ${plugin_name} обновлена."
  fi

  redirect_to $SCRIPT_NAME
else
  include $config_file

  # Default values
  [ -z "$telegram_caption" ] && telegram_caption="%hostname, %datetime"
fi
%>
<%in p/header.cgi %>

<div class="row row-cols-1 row-cols-md-2 g-4 mb-4">
  <div class="col">
    <form action="<%= $SCRIPT_NAME %>" method="post">
      <% field_switch "telegram_enabled" "Включить отправку в Telegram" %>
      <% field_text "telegram_token" "Token" "Ваш токен аутентификации Telegram Bot." %>
      <% field_text "telegram_channel" "Chat ID" "Числовой идентификатор канала, на который бот должен публиковать изображения.." %>
      <% field_switch "telegram_as_photo" "Отправить как фото." %>
      <% field_text "telegram_caption" "Подпись к фотографии" "Доступные переменные: %hostname, %datetime, %soctemp." %>
      <% field_switch "telegram_as_attachment" "Отправить как вложение." %>
      <% field_switch "telegram_socks5_enabled" "Использовать SOCKS5." "<a href=\"network-socks5.cgi\">Конфигурация</a> доступа SOCKS5" %>
      <% button_submit %>
    </form>
  </div>
</div>

<% if [ -z "$telegram_token" ]; then %>
<div class="alert alert-info mt-4">
  <h5>Чтобы создать канал для вашего бота Telegram:</h5>
  <ol>
    <li>Начните чат сh <a href=\"https://t.me/BotFather\">@BotFather</a></li>
    <li>Введите <code>/start</code> чтобы начать сеанс.</li>
    <li>Введите <code>/newbot</code> создать нового бота.</li>
    <li>Дайте вашему каналу бота имя, например: <i>cool_cam_bot</i>.</li>
    <li>Дайте вашему боту имя пользователя, например: <i>CoolCamBot</i>.</li>
    <li>Скопируйте токен, назначенный BotFather вашему новому боту, и вставьте его в форму.</li>
  </ol>
</div>
<% fi %>

<%in p/footer.cgi %>
