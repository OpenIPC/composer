#!/usr/bin/haserl
<%in _common.cgi %>
<% page_title="Camera Preview"
ipaddr=$(printenv | grep HTTP_HOST | cut -d= -f2 | cut -d: -f1)
%>
<%in _header.cgi %>
<div class="b1">
  <video border="" width="100%" onClick="fullscreen3(document.documentElement);return false;"  controls="controls" autoplay>
   <source src="/rec/2022/06/12/10.mp4" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
  </video>
</div>
</main>
</body>
</html>
