#!/usr/bin/haserl
<%in p/common.cgi %>
<% page_title="Перезагрузка устройства" %>
<%in p/header.cgi %>

<div class="row row-cols-md-3 g-4 mb-4">
  <div class="col">
    <div class="alert alert-danger">
      <h4>Перезагрузка камеры</h4>
      <p>Перезагрузите камеру, чтобы применить новые настройки. Это также удалит все данные о разделах, смонтированных в системной памяти, например. /tmp.</p>
      <% button_reboot %>
    </div>
  </div>
  <div class="col">
    <%in p/reset-firmware.cgi %>
  </div>
  <div class="col">
    <div class="alert alert-danger">
      <h4>Сбросить настройки Маджестик</h4>
      <p>Восстановить файл конфигурации Majestic <code>/etc/majestic.yaml</code> до своего первозданного состояния. Все изменения будут потеряны!
       Вы можете захотеть <a href="majestic-config-actions.cgi">сделать резервную копию последней конфигурации</a> перед сбросом.</p>
      <% button_mj_reset %>
    </div>
  </div>
</div>

<%in p/footer.cgi %>
