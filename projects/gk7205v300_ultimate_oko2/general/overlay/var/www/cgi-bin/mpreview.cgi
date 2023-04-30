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
    <td width=60>
      <% tbutton "focus-plus.svg" "Focus pluss" %><br>
      <% tbutton "focus-auto.svg" "Focus auto" %><br>
      <% tbutton "focus-minus.svg" "Focus minuss" %></td>
    <td width="100%" align=center onClick="fullscreen3(document.documentElement);return false;">&nbsp;</td>
    <td width=60 align="right">
      <% tbutton "zoom-in.svg" "Zoom ins" %><br><br>
      <% tbutton "zoom-out.svg" "Zoom outs" %></td>
    <td width=20>&nbsp;</td>
  </tr>
</table>
<script type="text/javascript">
getserv();
</script>
</body>
</html>
