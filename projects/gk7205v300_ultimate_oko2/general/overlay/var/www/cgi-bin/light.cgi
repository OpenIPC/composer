#!/usr/bin/haserl
<%in _common.cgi %>
<%
ll="";
while [[ -z "$ll" ]]
do
ll="$(cat /tmp/lt)"
done

if [[ "$ll" == "1" ]]
  then
   light 0
  else
   light 1
fi
%>