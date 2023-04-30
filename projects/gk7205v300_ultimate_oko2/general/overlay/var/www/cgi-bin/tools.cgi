#!/usr/bin/haserl
<%in _common.cgi %>
<%
get_system_info
page_title="$tPageTitleTools"
%>
<%in _header.cgi %>
<div class="row row-cols-1 row-cols-xl-2 g-4 mb-4">
  <div class="col">
    <div class="card h-100 mb-3">
      <h5 class="card-header">&#1050;&#1072;&#1095;&#1077;&#1089;&#1090;&#1074;&#1086; &#1087;&#1080;&#1085;&#1075;&#1072;</h5>
      <div class="card-body">
        <form action="/cgi-bin/tools-do.cgi" method="post">
          <div class="row mb-2">
            <label class="form-label col-md-6" for="action">&#1044;&#1077;&#1081;&#1089;&#1090;&#1074;&#1080;&#1077;</label>
            <div class="col-md-6">
              <select class="form-select" name="action" id="action">
                <% for i in ping trace; do echo -n "<option>${i}</option>"; done %>
              </select>
            </div>
          </div>
          <div class="row mb-2">
            <label class="col-md-6 form-label" for="target">&#1062;&#1077;&#1083;&#1077;&#1074;&#1086;&#1077; &#1087;&#1086;&#1083;&#1085;&#1086;&#1077; &#1076;&#1086;&#1084;&#1077;&#1085;&#1085;&#1086;&#1077; &#1080;&#1084;&#1103; &#1080;&#1083;&#1080; IP-&#1072;&#1076;&#1088;&#1077;&#1089;</label>
            <div class="col-md-6">
              <input class="form-control pat-host-ip" type="text" name="target" id="target" value="4.2.2.1" placeholder="FQDN or IP address" required>
            </div>
          </div>
          <div class="row mb-2">
            <label class="col-md-6 form-label" for="iface">&#1048;&#1089;&#1087;&#1086;&#1083;&#1100;&#1079;&#1086;&#1074;&#1072;&#1090;&#1100; &#1089;&#1077;&#1090;&#1077;&#1074;&#1086;&#1081; &#1080;&#1085;&#1090;&#1077;&#1088;&#1092;&#1077;&#1081;&#1089;</label>
            <div class="col-md-6">
              <select class="form-select" name="iface" id="iface">
                <option>auto</option>
                <% for i in $interfaces; do echo -n "<option>${i}</option>"; done %>
              </select>
            </div>
          </div>
          <div class="row mb-2">
            <label class="col-md-6 form-label" for="size">&#1056;&#1072;&#1079;&#1084;&#1077;&#1088; &#1087;&#1072;&#1082;&#1077;&#1090;&#1072;</label>
            <div class="col-md-6">
              <div class="input-group">
                <span class="input-group-text">
                  <label><input type="checkbox" class="form-check-input auto-value" data-for="size" data-value=""> default</label>
                </span>
                <input class="form-control" type="number" min="56" max="1500" step="1" name="size" id="size" value="56">
              </div>
            </div>
          </div>
          <div class="row mb-2">
            <label class="col-md-6 form-label" for="duration">&#1050;&#1086;&#1083;&#1080;&#1095;&#1077;&#1089;&#1090;&#1074;&#1086; &#1087;&#1072;&#1082;&#1077;&#1090;&#1086;&#1074;</label>
            <div class="col-md-6">
              <input class="form-control" type="number" min="1" max="30" step="1" name="duration" id="duration" value="5">
            </div>
          </div>
          <button type="submit" class="btn btn-primary"><%= $tButtonRun %></button>
        </form>
      </div>
    </div>
  </div>
</div>
<%in _footer.cgi %>
