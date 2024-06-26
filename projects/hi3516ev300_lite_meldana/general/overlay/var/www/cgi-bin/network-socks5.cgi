#!/usr/bin/haserl
<%in p/common.cgi %>
<%
plugin="socks5"
page_title="SOCKS5 proxy"

config_file="${ui_config_dir}/${plugin}.conf"
[ ! -f "$config_file" ] && touch $config_file

if [ "POST" = "$REQUEST_METHOD" ]; then
  tmp_file=/tmp/${plugin}.conf
  :>$tmp_file
  for v in enabled server port username password; do
    eval echo "${plugin}_${v}=\\\"\$POST_${plugin}_${v}\\\"" >>$tmp_file
  done
  mv $tmp_file $config_file
  redirect_to $SCRIPT_NAME
fi

include $config_file
%>

<%in p/header.cgi %>

<div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4 mb-4">
  <div class="col">
    <form action="<%= $SCRIPT_NAME %>" method="post">
      <% field_hidden "action" "update" %>
      <% field_text "socks5_host" "Хост SOCKS5" %>
      <% field_number "socks5_port" "Порт SOCKS5 " "1080" %>
      <% field_text "socks5_username" "Имя пользователя SOCKS5" %>
      <% field_password "socks5_password" "Пароль SOCKS5" %>
      <% button_submit %>
    </form>
  </div>
</div>

<%in p/footer.cgi %>
