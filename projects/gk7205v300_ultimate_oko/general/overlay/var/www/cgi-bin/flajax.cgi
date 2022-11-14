#!/usr/bin/haserl
content-type: text/plain

<%

cf=$(gf);

echo  "{ \"gf\": $(gf), \"ld\": $(cat < /tmp/lt), \"lexp\": $(gexp),  \"stf\": $(cat < /tmp/st), \"lst\": $(cat < /tmp/lst) }";

%>
