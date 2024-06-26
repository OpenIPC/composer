#!/usr/bin/haserl
<%in p/common.cgi %>
<%
[ ! -f "/rom/${mj_bin_file}" ] && redirect_to '/' "danger" "Majestic не поддерживается в этой системе."

update_meta() {
  # re-download metafile if older than 1 hour
  mj_meta_url="http://openipc.s3-eu-west-1.amazonaws.com/majestic.${soc_family}.${fw_variant}.master.tar.meta"

  if [ -f "$mj_meta_file" ]; then
    mj_meta_file_timestamp=$(time_epoch "$(ls -lc --full-time $mj_meta_file | xargs | cut -d' ' -f6,7)")
    mj_meta_file_expiration=$(( $(time_epoch) + 3600 ))
    [ "$mj_meta_file_timestamp" -le "$mj_meta_file_expiration" ] && return
    rm $mj_meta_file
  fi

  [ "200" = $(curl $mj_meta_url -s -f -w %{http_code} -o /dev/null) ] && curl -s $mj_meta_url -o $mj_meta_file
}

page_title="Majestic"
mj_meta_file=/tmp/mj_meta.txt

# NB! sizes are in allocated blocks.
mj_filesize_fw=$(ls -s $mj_bin_file | xargs | cut -d' ' -f1)

mj_bin_file_ol="${overlay_root}${mj_bin_file}"
[ -f "$mj_bin_file_ol" ] && mj_filesize_ol=$(ls -s $mj_bin_file_ol | xargs | cut -d' ' -f1)

free_space=$(df | grep /overlay | xargs | cut -d' ' -f4)
available_space=$(( ${free_space:=0} + ${mj_filesize_ol:=0} - 1 ))

if [ "POST" = "$REQUEST_METHOD" ]; then
  case "$POST_action" in
  rmmj)
    [ -f "$mj_bin_file_ol" ] && rm $mj_bin_file_ol && mount -oremount /
    redirect_back "success" "Majestic вернулся к базовой версии."
    ;;
  update)
    [ -z "$network_gateway" ] && redirect_to "danger" "Для обновления требуется подключение к интернету!"

    update_meta
    mj_filesize_new=$(( ($(cat $mj_meta_file | sed -n 2p) + 1024) / 1024 ))
    [ "$mj_filesize_new" -gt "$available_space" ] && redirect_back "danger" "Недостаточно места для обновления Majestic. ${mj_filesize_new} КБ > ${available_space} КБ."

    curl --silent --insecure --location -o - http://openipc.s3-eu-west-1.amazonaws.com/majestic.${soc_family}.${fw_variant}.master.tar.bz2 | bunzip2 | tar -x ./majestic -C /usr/bin/
    [ $? -ne 0 ] && redirect_back "error" "Недостаточно места для обновления Majestic."
    redirect_to "reboot.cgi"
    ;;
  esac
fi

mj_version_fw=$(/rom${mj_bin_file} -v)
mj_version_ol="<span class=\"text-secondary\">- не устанавливается в оверлее -</span>"
[ -f "$mj_bin_file_ol" ] && mj_version_ol=$($mj_bin_file_ol -v)

if [ -n "$network_gateway" ]; then
  update_meta
  if [ -f "$mj_meta_file" ]; then
    # parse version, date and file size
    if [ "$(wc -l $mj_meta_file | cut -d' ' -f1)" = "1" ]; then
      mj_filesize_new=$(sed -n 1p $mj_meta_file)
    else
      mj_version_new=$(sed -n 1p $mj_meta_file)
      mj_filesize_new=$(sed -n 2p $mj_meta_file)
    fi
    # NB! size in bytes, but since blocks are 1024 bytes each, we are safe here for now.
    mj_filesize_new=$(( ($mj_filesize_new + 1024) / 1024 )) # Rounding up by priming, since $(()) sucks at floats.
  else
    mj_version_new="unavailable"
  fi
else
  mj_version_new="<span class=\"text-danger\">- нет доступа к сегменту S3 -</span>"
fi
%>
<%in p/header.cgi %>

<div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4 mb-4">
  <div class="col">
    <h3>Version</h3>
    <dl class="list small">
      <dt>Bundled</dt>
      <dd><%= $mj_version_fw %></dd>
      <dt>In overlay</dt>
      <dd><%= $mj_version_ol %></dd>
      <dt>On GitHub</dt>
      <dd><%= $mj_version_new %></dd>
    </dl>
  </div>
  <div class="col">
    <h3>Конфигурация</h3>
    <% if [ -z "$(diff /rom/etc/majestic.yaml /etc/majestic.yaml)" ]; then %>
      <p>Majestic использует оригинальную конфигурацию.</p>
      <p><a href="majestic-settings.cgi">Внести изменения.</a></p>
    <% else %>
      <p>Majestic использует индивидуальную конфигурацию.</p>
      <p><a href="majestic-config-compare.cgi" class="btn btn-primary">Показать различия</a></p>
    <% fi %>
  </div>
  <div class="col">
  <% if [ -n "$network_gateway" ]; then %>
    <h3>Update</h3>
    <% if [ "$mj_version_new" = "$mj_version_ol" ] || [ -z "$mj_version_ol" -a "$mj_version_new" = "$mj_version_fw" ]; then %>
      <div class="alert alert-success">
        <p class="mb-1"><b>Нечего обновлять.</b></p>
        <p class="mb-0">Последняя версия уже установлена.</p>
      </div>
    <% else %>
      <% if [ -f "$mj_meta_file" ]; then %>
        <% if [ "$mj_filesize_new" -le "$available_space" ]; then %>
          <form action="<%= $SCRIPT_NAME %>" method="post">
            <% field_hidden "action" "Обновление" %>
            <% button_submit "Установить обновление" "warning" %>
          </form>
        <% else %>
          <div class="alert alert-danger">
            <p class="mb-1"><b>Недостаточно места для обновления Majestic!</b></p>
            <p class="mb-0">Обновление требует <%= $mj_filesize_new %>KБ, но только <%= $available_space %>KБ доступно
            <% if [ "$mj_filesize_ol" -ge "1" ]; then %>
            (<%= $free_space %>KБ нераспределенного пространства плюс <%= ${mj_filesize_ol:=0} %>KБ размер Majestic, установленного в оверлее)
            <% fi %>
            .</p>
          </div>
        <% fi %>
      <% fi %>
    <% fi %>
  <% else %>
    <p class="alert alert-danger">Для обновления требуется доступ к Amazon S3.</p>
  <% fi %>
  <% if [ -f "$mj_bin_file_ol" ]; then %>
    <div class="alert alert-warning">
      <p>Более поздняя версия Majestic найдена в разделе оверлея. Занимает <%= $mj_filesize_ol %> KБ места на диске.</p>
      <form action="<%= $SCRIPT_NAME %>" method="post">
        <% field_hidden "action" "rmmj" %>
        <% button_submit "Вернуться к базовой версии" "warning" %>
      </form>
    </div>
  <% fi %>
  </div>
</div>

<%in p/footer.cgi %>
