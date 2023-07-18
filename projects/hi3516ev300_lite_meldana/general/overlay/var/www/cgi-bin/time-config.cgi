#!/usr/bin/haserl
<%in p/common.cgi %>
<%
plugin="time"
page_title="Время"

config_file="${ui_config_dir}/${plugin}.conf"
[ ! -f "$config_file" ] && touch $config_file

if [ "POST" = "$REQUEST_METHOD" ]; then
  case "$POST_action" in
    reset)
      cp /rom/etc/ntp.conf /etc/ntp.conf
      redirect_back "success" "Конфигурация сброшена к заводским настройкам прошивки."
      ;;
    update)
      # check for mandatory data
      [ -z "$POST_tz_name" ] && redirect_to $SCRIPT_NAME "warning" "Пустое название часового пояса. Пропустить."
      [ -z "$POST_tz_data" ] && redirect_to $SCRIPT_NAME "warning" "Пустое значение часового пояса. Пропустить."

      [ "$tz_data" != "$POST_tz_data" ] && echo "${POST_tz_data}" >/etc/TZ
      [ "$tz_name" != "$POST_tz_name" ] && echo "${POST_tz_name}" >/etc/timezone

      tmp_file=/tmp/ntp.conf
      :>$tmp_file
      for _i in 0 1 2 3; do
        eval _s="\$POST_ntp_server_${_i}"
        [ -n "$_s" ] && echo "server ${_s} iburst" >>$tmp_file
      done
      unset _i; unset _s
      mv $tmp_file /etc/ntp.conf
      redirect_back "success" "Конфигурация обновлена."
      ;;
  esac

  update_caminfo
  redirect_to $SCRIPT_NAME "success" "Часовой пояс обновлен."
fi
%>

<%in p/header.cgi %>

<form action="<%= $SCRIPT_NAME %>" method="post">
  <% field_hidden "action" "Обновить" %>

<div class="row row-cols-1 row-cols-md-2 row-cols-lg-2 g-4 mb-4">
  <div class="col">
    <h4>Часовой пояс</h4>
    <datalist id="tz_list"></datalist>
    <p class="string">
      <label for="tz_name" class="form-label">Название часового пояса</label>
      <input type="text" id="tz_name" name="tz_name" value="<%= $tz_name %>" class="form-control" list="tz_list">
      <span class="hint text-secondary">Начните вводить название ближайшего крупного города в поле выше, затем выберите один из доступных вариантов.</span>
    </p>
    <p class="string">
      <label for="tz_data" class="form-label">Строка зоны</label>
      <input type="text" id="tz_data" name="tz_data" value="<%= $tz_data %>" class="form-control" readonly>
      <span class="hint text-secondary">Управляющая строка часового пояса, выбранного выше. Поле только для чтения, только для мониторинга.</span>
    </p>
    <p><a href="#" id="frombrowser">Получить часовой пояс из браузера</a></p>
  </div>
  <div class="col">
    <h4>Синхронизация времени</h4>
<%
for _i in 0 1 2 3; do
  _x=$(expr $_i + 1)
  eval ntp_server_${_i}="$(sed -n ${_x}p /etc/ntp.conf | cut -d' ' -f2)"
  field_text "ntp_server_${_i}" "NTP Server $(( _i + 1 ))"
done; unset _i; unset _x
%>
 <p id="sync-time-wrapper"><a href="#" id="sync-time">Синхронизировать время</a></p>
  </div>

  <div class="col">
  <% if [ "$(diff -q -- "/rom${config_file}" "$config_file")" ]; then %>
    <form action="<%= $SCRIPT_NAME %>" method="post" class="mt-4">
      <% field_hidden "action" "reset" %>
      <% button_submit "Восстановить настройки прошивки по умолчанию" "danger" %>
    </form>
  <% fi %>
  </div>
</div>

  <% button_submit %>
</form>

<script src="/a/tz.js"></script>
<script>
  $('#sync-time').addEventListener('click', event => {
    event.preventDefault();
    fetch('/cgi-bin/j/sync-time.cgi')
      .then((response) => response.json())
      .then((json) => {
        p = document.createElement('p');
        p.classList.add('alert', 'alert-' + json.result);
        p.textContent = json.message;
        $('#sync-time-wrapper').replaceWith(p);
      })
  });
</script>
<%in p/footer.cgi %>
