#!/usr/bin/haserl
<%in _common.cgi %>
<% page_title="Camera Preview"
ipaddr=$(printenv | grep HTTP_HOST | cut -d= -f2 | cut -d: -f1)
%>
<%in _mheader.cgi %>
<div class="b1 parent">
  <div class="block">
    <img id="img1" align="middle" border="" width="100%" src="/img/mycam.jpg" onClick="fullscreen3(document.documentElement);return false;">
  </div>
</div>
</main>
<table border="0" cellpadding="0" cellspacing="0" width="100%" class= "control b3">
  <tr>
    <td width=20>&nbsp;</td>
    <td width=60><% button "focus-plus.svg" "Focus plus" %><br>
      <% button "focus-auto.svg" "Focus auto" %><br>
      <% button "focus-minus.svg" "Focus minus" %></td>
    <td width="100%" align=center onClick="fullscreen3(document.documentElement);return false;">&nbsp;</td>
    <td width=60 align="right">
      <% button "zoom-in.svg" "Zoom in" %><br><br>
      <% button "zoom-out.svg" "Zoom out" %></td>
    <td width=20>&nbsp;</td>
  </tr>
</table>
<script type="text/javascript">
getserv();
</script>
</body>
</html>
