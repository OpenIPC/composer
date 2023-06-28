#!/usr/bin/haserl
<%in p/common.cgi %>
<%
if [ "POST" = "$REQUEST_METHOD" ]; then
  editor_file="$POST_editor_file"
  editor_text="$POST_editor_text"
  editor_backup="$POST_editor_backup"

  # strip carriage return (\u000D) characters
  editor_text=$(echo "$editor_text" | sed s/\\r//g)

  case "$POST_action" in
  restore)
    if [ ! -f "$editor_file" ]; then
      redirect_to "${SCRIPT_NAME}?f=${editor_file}" "danger" "Файл не найден!"
    elif [ ! -f "$editor_file.backup" ]; then
      redirect_to "${SCRIPT_NAME}?f=${editor_file}" "danger" "Файл не найден!"
    else
      mv "$editor_file.backup" "$editor_file"
      redirect_to "${SCRIPT_NAME}?f=${editor_file}" "success" "Файл восстановлен из резервной копии."
    fi
    ;;
  save)
    if [ -z "$editor_text" ]; then
      flash_save "warning" "Пустая полезная нагрузка.  Файл не сохранен!"
    else
      if [ -n "$editor_backup" ]; then
        cp "$editor_file" "${editor_file}.backup"
      else
        [ -f "${editor_file}.backup" ] && rm "${editor_file}.backup"
      fi
      echo "$editor_text" >"$editor_file"
      redirect_to "${SCRIPT_NAME}?f=${editor_file}" "success" "Файл сохранён."
    fi
    ;;
  *)
    flash_save "danger" "UNKNOWN ACTION: $POST_action"
    ;;
  esac
else
  editor_file="$GET_f"
  if [ ! -f "$editor_file" ]; then
    flash_save "danger" "Файл не найден!"
  elif [ -n "$editor_file" ]; then
    if [ "b" = "$( (cat -v "$editor_file" | grep -q "\^@") && echo "b" )" ]; then
      flash_save "danger" "Не текстовый файл!"
    elif [ "$(stat -c%s $editor_file)" -gt "102400" ]; then
      flash_save "danger" "Загруженный файл слишком большой!"
    else
      editor_text="$(cat $editor_file | sed "s/&/\&amp;/g;s/</\&lt;/g;s/>/\&gt;/g;s/\"/\&quot;/g")"
    fi
  fi
fi

page_title="Текстовый редактор"
%>
<%in p/header.cgi %>

<ul class="nav nav-tabs" role="tablist">
  <% tab_lap "edit" "Редактор" %>
  <% tab_lap "file" "Файл" %>
<% if [ -f "${editor_file}.backup" ]; then %>
  <% tab_lap "back" "Восстановление" %>
  <% tab_lap "diff" "Различие" %>
<% fi %>
</ul>

<div class="tab-content p-2" id="tab-content">
  <div id="edit-tab-pane" role="tabpanel" class="tab-pane fade show active" aria-labelledby="edit-tab" tabindex="0">
    <form action="<%= $SCRIPT_NAME %>" method="post" class="mb-4">
      <% field_hidden "action" "Сохранить" %>
      <% field_hidden "editor_file" "$editor_file" %>
      <% field_textarea "editor_text" "Содержимое файла" %>
      <p class="boolean"><span class="form-check form-switch">
        <input type="checkbox" id="editor_backup" name="editor_backup" value="true" class="form-check-input" role="switch">
        <label for="editor_backup" class="form-label form-check-label">Создать резервный файл</label>
      </span></p>
      <% button_submit %>
    </form>
  </div>

  <div id="file-tab-pane" role="tabpanel" class="tab-pane fade" aria-labelledby="file-tab" tabindex="0">
    <% ex "cat -t $editor_file" %>
  </div>

  <% if [ -f "${editor_file}.backup" ]; then %>
    <div id="back-tab-pane" role="tabpanel" class="tab-pane fade" aria-labelledby="back-tab" tabindex="0">
      <% ex "cat -t ${editor_file}.backup" %>
      <form action="<%= $SCRIPT_NAME %>" method="post">
        <% field_hidden "action" "Перезагрузка" %>
        <% field_hidden "editor_file" "$editor_file" %>
        <% button_submit "Восстановить" "danger" %>
      </form>
    </div>
    <div id="diff-tab-pane" role="tabpanel" class="tab-pane fade" aria-labelledby="diff-tab" tabindex="0">
      <h4>Изменения по сравнению с предыдущей версией</h4>
<%
# it's ugly but shows non-printed characters (^M/^I)
_n=$(basename $editor_file)
cat -t $editor_file >/tmp/${_n}.np
cat -t ${editor_file}.backup >/tmp/${_n}.backup.np
pre "$(diff -s -d -U0 /tmp/${_n}.backup.np -L ${editor_file}.backup /tmp/${_n}.np -L $editor_file)"
rm /tmp/${_n}.np /tmp/${_n}.backup.np
unset _n
%>
    </div>
  <% fi %>
</div>

<%in p/footer.cgi %>
