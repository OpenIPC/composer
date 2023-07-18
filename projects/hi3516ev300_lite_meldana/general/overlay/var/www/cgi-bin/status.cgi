#!/usr/bin/haserl
<%in p/common.cgi %>
<% page_title="Статус устройства" %>
<%in p/header.cgi %>

<div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4 mb-4">
  <div class="col">
    <h3>Камера</h3>
    <h5>Система</h5>
    <dl class="small list">
      <dt>Процессор</dt>
      <dd><%= $soc %></dd>
      <dt>Семейство</dt>
      <dd><%= $soc_family %></dd>
      <dt>Тип сенсора</dt>
      <dd><%= $sensor_ini %></dd>
      <dt>Объём памяти</dt>
      <dd><%= $flash_size %> MB</dd>
    </dl>
  </div>

  <div class="col">
    <h3>Система</h3>
    <h5>Прошивка</h5>
    <dl class="small list">
      <dt>Версия</dt>
      <dd><%= "${fw_version}-${fw_variant}" %></dd>
      <dt>Билд</dt>
      <dd><%= $fw_build %></dd>
      <dt>Majestic</dt>
      <dd><%= $mj_version %></dd>
      <dt>Имя устройства</dt>
      <dd><%= $network_hostname %></dd>
    </dl>
  </div>
</div>
<%
_s=$(df | grep /overlay | xargs | cut -d' ' -f5)
%>
<div class="alert alert-primary">
  <h5>Раздел Оверлея заполнен на <%= $_s %>.</h5>
  <% progressbar "${_s/%/}" %>
</div>
<%in p/reset-firmware.cgi %>

<%in p/footer.cgi %>
