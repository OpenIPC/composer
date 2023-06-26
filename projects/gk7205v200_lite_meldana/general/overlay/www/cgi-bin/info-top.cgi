#!/usr/bin/haserl
<%in p/common.cgi %>
<% page_title="Топ процессов" %>
<%in p/header.cgi %>
<% ex "top -n 1 -b" %>
<%in p/footer.cgi %>
