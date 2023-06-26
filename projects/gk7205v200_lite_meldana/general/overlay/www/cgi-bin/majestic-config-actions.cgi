#!/usr/bin/haserl --upload-limit=20 --upload-dir=/tmp
<%in p/common.cgi %>
<%
config_file=/etc/majestic.yaml
config_file_fw=/rom/etc/majestic.yaml

if [ "POST" = "$REQUEST_METHOD" ]; then
  case "$POST_action" in
    backup)
      echo "HTTP/1.0 200 OK
Date: $(time_http)
Server: $SERVER_SOFTWARE
Content-type: text/plain
Content-Disposition: attachment; filename=majestic.yaml
Content-Length: $(stat -c%s $config_file)
Cache-Control: no-store
Pragma: no-cache
"
      cat $config_file
      ;;
    patch)
      patch_file=/tmp/majestic.patch
      diff $config_file_fw $config_file >$patch_file
      echo "HTTP/1.0 200 OK
Date: $(time_http)
Server: $SERVER_SOFTWARE
Content-type: text/plain
Content-Disposition: attachment; filename=majestic.$(time_epoch).patch
Content-Length: $(stat -c%s $patch_file)
Cache-Control: no-store
Pragma: no-cache
"
      cat $patch_file
      rm $patch_file
      ;;
    reset)
      /usr/sbin/sysreset.sh -m
      redirect_back
      ;;
    restore)
      magicnum="23206d616a6573746963"
      file="$POST_mj_restore_file"
      file_name="$POST_mj_restore_file_name"
      file_path="$POST_mj_restore_file_path"
      error=""
      [ -z "$file_name" ] && error="Файл не найден! Вы не забыли загрузить?"
      [ ! -r "$file" ] && error="Невозможно прочитать загруженный файл!"
      [ "$(stat -c%s $file)" -gt "$maxsize" ] && error="Загруженный файл слишком большой! $(stat -c%s $file) > ${maxsize}."
      #[ "$magicnum" -ne "$(xxd -p -l 10 $file)" ] && error="Магический номер файла не совпадает. Вы загрузили неправильный файл? $(xxd -p -l 10 $file) != $magicnum"
      if [ -z "$error" ]; then
        # yaml-cli -i $POST_upfile -o /tmp/majestic.yaml # FIXME: sanitize
        mv $file_path /etc/majestic.yaml
        redirect_to $SCRIPT_NAME
      fi
      ;;
  esac
fi
%>

<% page_title="Обслуживание Majestic" %>
<%in p/header.cgi %>

<div class="row row-cols-1 row-cols-lg-3 g-4 mb-4">
  <div class="col">
    <h3>Резервная копия конфигурации</h3>
    <p>Загрузите последний файл majestic.yaml, чтобы сохранить изменения, внесенные в конфигурацию по умолчанию.</p>
    <form action="<%= $SCRIPT_NAME %>" method="post">
      <% field_hidden "action" "Backup" %>
      <% button_submit "Скачать конфигурацию" %>
    </form>
  </div>
  <div class="col">
    <h3>Восстановить конфигурацию</h3>
    <p>Восстановите пользовательскую конфигурацию Majestic из сохраненной копии файла majestic.yaml.</p>
    <form action="<%= $SCRIPT_NAME %>" method="post" enctype="multipart/form-data">
      <% field_hidden "action" "Restore" %>
      <% field_file "mj_restore_file" "Файл резервного копирования" "majestic.yaml" %>
      <% button_submit "Загрузить конфигурацию" "warning" %>
    </form>
  </div>
  <div class="col">
    <h3>Посмотреть различия</h3>
    <p>Сравните свежий файл majestic.yaml с тем, что идет в комплекте с прошивкой.</p>
    <a class="btn btn-primary" href="majestic-config-compare.cgi">Проверить изменения</a>
  </div>
  <div class="col">
    <h3>Экспортировать как патч</h3>
    <p>Экспорт изменений, внесенных в majestic.yaml, в виде файла исправления.</p>
    <form action="<%= $SCRIPT_NAME %>" method="post">
      <% field_hidden "action" "Patch" %>
      <% button_submit "Скачать файл патча" %>
    </form>
  </div>
  <div class="col">
    <h3>Сброс</h3>
    <% if [ "$(diff -q $config_file_fw $config_file)" ]; then %>
      <p>Сбросьте конфигурацию Majestic в исходное состояние, которое поставляется с прошивкой.</p>
      <% button_mj_reset %>
    <% else %>
      <p>Сбрасывать нечего. Последняя конфигурация Majestic не отличается от поставляемой с прошивкой.</p>
    <% fi %>
  </div>
</div>

<%in p/footer.cgi %>
