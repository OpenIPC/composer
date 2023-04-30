#!/usr/bin/haserl
<% http_header_html %>
<% ipaddr=$(printenv | grep HTTP_HOST | cut -d= -f2 | cut -d: -f1) %>
<% reus=$(printenv REMOTE_USER) %>
<!DOCTYPE html>
<html lang="en">
<head>
<% if [ $reus = "oper" ]; then %><meta http-equiv="refresh" content="0;URL=/cgi-bin/opreview.cgi" /><% fi %>
<meta charset="utf-8">
<meta http-equiv="Cache-Control" content="no-cache" />
<meta name="viewport" content="width=device-width,initial-scale=1">
<title><% html_title "$page_title" %></title>
<link rel="shortcut icon" href="/favicon.png">
<link href="/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="/css/bootstrap.override.css">
<% if [ $HTTP_MODE = "development" ]; then %><link rel="stylesheet" href="/css/debug.css"><% fi %>
<script src="/js/bootstrap.bundle.min.js"></script>
<script src="/js/jquery.js"></script>
  <script type="text/javascript" language="javascript">
    var img = new Image();
    var imgObj;
    var webcam = "http://<%= $ipaddr %>/image.jpg?width=640&height=360&qfactor=73&color2gray=0"
    function preload()
    {
      img.src= webcam + new Date;
    }
    function changesrc()
    {
      img1.src=img.src;
      preload();
      setTimeout(changesrc,3500);
    }
    function update()
    {
      imgObj = document.getElementById('img1');
      imgObj.src = img.src;
      img.src = webcam + (new Date()).getTime();
    }
    function takeError()
    {
      img.src = webcam + (new Date()).getTime();
    }
    function startonload()
    {
      img.src = webcam + (new Date()).getTime();
      img.onerror=takeError;
      img.onload=update;
    }
    function load()
    {
      if (navigator.appName.indexOf("Microsoft IE Mobile") != -1)
        {
          preload();
          changesrc();
          return;
        }
      startonload();
    }
    function zoom_in()
    {
    $.ajax({
        url: '/cgi-bin/z_in.cgi',
        method: 'get',
        cache: false
    });
    }
    function zoom_out()
        {
        $.ajax({
                url: '/cgi-bin/z_out.cgi',
                method: 'get',
                cache: false
        });
        }
    function zoom_ins()
        {
        $.ajax({
                url: '/cgi-bin/sz_in.cgi',
                method: 'get',
                cache: false
        });
        }
    function zoom_outs()
        {
        $.ajax({
                url: '/cgi-bin/sz_out.cgi',
                method: 'get',
                cache: false
        });
        }
    function stop()
        {
        $.ajax({
                url: '/cgi-bin/c_stop.cgi',
                method: 'get',
                cache: false
        });
        }
    function focus_auto()
        {
        $.ajax({
                url: '/cgi-bin/af.cgi',
                method: 'get',
                cache: false
        });
        }
    function focus_plus()
        {
        $.ajax({
                url: '/cgi-bin/f_plus.cgi',
                method: 'get',
                cache: false
        });
        }
    function focus_minus()
        {
        $.ajax({
                url: '/cgi-bin/f_minus.cgi',
                method: 'get',
                cache: false
        });
        }
    function focus_pluss()
        {
        $.ajax({
                url: '/cgi-bin/sf_plus.cgi',
                method: 'get',
                cache: false
        });
        }
    function focus_minuss()
        {
        $.ajax({
                url: '/cgi-bin/sf_minus.cgi',
                method: 'get',
                cache: false
        });
        }

    function light()
        {
        $.ajax({
                url: '/cgi-bin/light.cgi',
                method: 'get',
                cache: false
        });
        }

function getserv() {
$(function(){
    $.getJSON('/cgi-bin/flajax.cgi', function(data) {
    document.getElementById("GF").innerHTML = data.gf;
    document.getElementById("LST").innerHTML = data.lst;
    document.getElementById("LEXP").innerHTML = data.lexp;

            document.getElementById("STF").innerHTML = data.stf;

        if ( data.ld == 1 ) 
          {
            document.getElementById("light").src="/img/lt-on.svg";
          } else {
            document.getElementById("light").src="/img/lt-off.svg";
          }
        if ( data.ff == 1 ) 
          {
            document.getElementById("GF").className="meves";
          } else {
            document.getElementById("GF").className="meven";
          }

    });
});
 setTimeout("getserv()", 500);
}

function fullscreen3(element) {
if(element.requestFullScreen) {
element.requestFullScreen();
} else if(element.mozRequestFullScreen) {
    element.mozRequestFullScreen();
} else if(element.webkitRequestFullScreen) {
    element.webkitRequestFullScreen();
}
}
fullscreen3(document.documentElement);
  </script>
  <style type="text/css">
   .b1 TABLE { position: relative; }
   .b2 { left: 0px; top: -160px; z-index: 2}
   .b3 {    
    position: fixed;
    left: 0; bottom: 0;
    padding: 2px;
    width: 100%;
    gap: 0rem;
    margin: 0rem auto;
    z-index: 2}
   .b4 {    
    position: fixed;
    left: 0; top: 90;
    padding: 2px;
    width: 100%;
    gap: 0rem;
    margin: 0rem auto;
    z-index: 2}
   .meves {
        padding: 4px;
        background: #2222FF;
    color: #FFFFFF;
    font-weight: bold;
        align: center;
        }
   .meven {
        padding: 4px;
        background: #222222;
    color: #FFFFFF;
    font-weight: bold;
        align: center;
        }


.parent {
    width: 100%;
    height: 100%;
    background-color: #000000;
    position: fixed;
    top: 0;
    left: 0;
    display: flex;
    align-items: center;
    align-content: center;
    justify-content: center;
    overflow: auto;
}
.block {
    width: 100%;
    img {
        display: block;
        border: none;
    }
}
  </style>
</head>

<body id="top" onLoad="load(); fullscreen3(document.documentElement);return false;" class="sss">
<nav class="navbar navbar-expand-lg navbar-dark sticky-top">
  <div class="container p-0">
    <a class="navbar-brand" href="/cgi-bin/status.cgi"><img src="/img/logo.svg" width="116" height="32" alt=""><%= "&nbsp;<b>gk300-$(gmnum)-$(getenv apname)</b> $(date +%F) $(date +%H:%M) $reus "; %></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
      aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" id="dropdownInformation" href="#"
            role="button" data-bs-toggle="dropdown" aria-expanded="false">&#1048;&#1085;&#1092;&#1086;&#1088;&#1084;&#1072;&#1094;&#1080;&#1103;</a>
          <ul class="dropdown-menu" aria-labelledby="dropdownInformation">
            <li><a class="dropdown-item" href="/cgi-bin/status.cgi">&#1054;&#1073;&#1079;&#1086;&#1088;</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/info-cron.cgi">&#1050;&#1086;&#1085;&#1092;&#1080;&#1075;&#1091;&#1088;&#1072;&#1094;&#1080;&#1103; Cron</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/info-dmesg.cgi">&#1044;&#1080;&#1072;&#1075;&#1085;&#1086;&#1089;&#1090;&#1080;&#1095;&#1077;&#1089;&#1082;&#1080;&#1077; &#1089;&#1086;&#1086;&#1073;&#1097;&#1077;&#1085;&#1080;&#1103;</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/info-httpd.cgi">&#1057;&#1088;&#1077;&#1076;&#1072; HTTPd</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/info-log.cgi">&#1063;&#1090;&#1077;&#1085;&#1080;&#1077; &#1078;&#1091;&#1088;&#1085;&#1072;&#1083;&#1072;</a></li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link" href="/cgi-bin/firmware.cgi">&#1055;&#1088;&#1086;&#1096;&#1080;&#1074;&#1082;&#1072;</a></li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" id="dropdownNetwork" href="#"
            role="button" data-bs-toggle="dropdown" aria-expanded="false">&#1053;&#1072;&#1089;&#1090;&#1088;&#1086;&#1081;&#1082;&#1080;</a>
          <ul class="dropdown-menu" aria-labelledby="dropdownNetwork">
            <li><a class="dropdown-item" href="/cgi-bin/network.cgi">&#1057;&#1077;&#1090;&#1077;&#1074;&#1099;&#1081; &#1085;&#1072;&#1089;&#1090;&#1088;&#1086;&#1081;&#1082;&#1080;</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/network-ntp.cgi">&#1053;&#1072;&#1089;&#1090;&#1088;&#1086;&#1081;&#1082;&#1080; NTP</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/fl-settings.cgi">&#1056;&#1072;&#1089;&#1096;&#1080;&#1088;&#1077;&#1085;&#1085;&#1099;&#1077; &#1085;&#1072;&#1089;&#1090;&#1088;&#1086;&#1081;&#1082;&#1080;</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/webui-settings.cgi">&#1055;&#1072;&#1088;&#1086;&#1083;&#1100; &#1074;&#1077;&#1073;-&#1080;&#1085;&#1090;&#1077;&#1088;&#1092;&#1077;&#1081;&#1089;&#1072;</a></li>
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" id="dropdownMajestic" href="#"
            role="button" data-bs-toggle="dropdown" aria-expanded="false">&#1042;&#1080;&#1076;&#1077;&#1086;&#1089;&#1077;&#1088;&#1074;&#1077;&#1088; Majestic</a>
          <ul class="dropdown-menu" aria-labelledby="dropdownMajestic">
            <li><a class="dropdown-item" href="/cgi-bin/majestic-settings-general.cgi">&#1053;&#1072;&#1089;&#1090;&#1088;&#1086;&#1081;&#1082;&#1080;</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/majestic-settings-services.cgi">&#1057;&#1077;&#1088;&#1074;&#1080;&#1089;&#1099;</a></li>
           <li><a class="dropdown-item" href="/cgi-bin/majestic-config-actions.cgi">&#1058;&#1077;&#1093;&#1085;&#1080;&#1095;&#1077;&#1089;&#1082;&#1086;&#1077; &#1086;&#1073;&#1089;&#1083;&#1091;&#1078;&#1080;&#1074;&#1072;&#1085;&#1080;&#1077;</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/preview-help.cgi">&#1048;&#1085;&#1092;&#1086;&#1088;&#1084;&#1072;&#1094;&#1080;&#1103;</a></li>
          </ul>
        </li>
        <li class="nav-item  dropdown">
          <a class="nav-link dropdown-toggle" id="dropdownTools" href="#"
            role="button" data-bs-toggle="dropdown" aria-expanded="false">&#1048;&#1085;&#1089;&#1090;&#1088;&#1091;&#1084;&#1077;&#1085;&#1099;</a>
          <ul class="dropdown-menu" aria-labelledby="dropdownTools">
            <li><a class="dropdown-item" href="/cgi-bin/tools.cgi">&#1055;&#1086;&#1080;&#1089;&#1082; &#1080; &#1090;&#1088;&#1072;&#1089;&#1089;&#1080;&#1088;&#1086;&#1074;&#1082;&#1072; &#1084;&#1072;&#1088;&#1096;&#1088;&#1091;&#1090;&#1072;</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/console.cgi">&#1042;&#1077;&#1073;-&#1082;&#1086;&#1085;&#1089;&#1086;&#1083;&#1100;</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/format.cgi">&#1060;&#1086;&#1088;&#1084;&#1072;&#1090;&#1080;&#1088;&#1086;&#1074;&#1072;&#1085;&#1080;&#1077; SD &#1080; &#1087;&#1077;&#1088;&#1077;&#1079;&#1072;&#1075;&#1088;&#1091;&#1079;&#1082;&#1072;</a></li>
          </ul>
        </li>
        <li class="nav-item  dropdown">
          <a class="nav-link dropdown-toggle" id="dropdownPreview" href="#"
            role="button" data-bs-toggle="dropdown" aria-expanded="false">&#1055;&#1088;&#1086;&#1089;&#1084;&#1086;&#1090;&#1088;</a>
          <ul class="dropdown-menu" aria-labelledby="dropdownPreview">
            <li><a class="dropdown-item" href="/cgi-bin/preview-video.cgi">&#1042;&#1080;&#1076;&#1077;&#1086;</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/mpreview.cgi">&#1055;&#1088;&#1086;&#1089;&#1084;&#1086;&#1090;&#1088; &#1080; &#1085;&#1072;&#1089;&#1090;&#1088;&#1086;&#1081;&#1082;&#1072;</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>
<%
button() {
  id=$(echo "${2// /_}" | tr '[:upper:]' '[:lower:]')
  echo "<img id=\"$id\" src=\"/img/${1}\" Onclick=\"$id();\" title=\"${2}\">"
}
tbutton() {
  id=$(echo "${2// /_}" | tr '[:upper:]' '[:lower:]')
  echo "<img id=\"$id\" src=\"/img/${1}\" Onmousedown=\"$id();\" onmouseup=\"stop();\" title=\"${2}\">"
}


ttbuttonn() {
  id=$(echo "${2// /_}" | tr '[:upper:]' '[:lower:]')
  echo "<img id=\"$id\" src=\"/img/${1}\" Onmousedown=\"$id();\" onmouseup=\"focus_minuss();stop();\" title=\"${2}\">"
}



%>
<table border="0" cellpadding="2" cellspacing="2" width="100%" class= "b4">
  <tr>
    <td width=50>
    <div id="GF" class="meven" align="center">
    &nbsp;
    </div>
    </td>
   <td width=50>
    <div id="LEXP" class="meven"  align="center">
    &nbsp;
    </div>
    </td>
   <td width=35>
    <div id="STF" class="meven"  align="center">
    &nbsp;
    </div>
    </td>
   <td width=35>
    <div id="LST" class="meven"  align="center">
    &nbsp;
    </div>
    </td>
    <td align=center onClick="fullscreen3(document.documentElement);return false;">&nbsp;</td>
    <td width=60 align="right" class="contr" id="BL">
    <% button "lt-off.svg" "light" %>
   </td>
  </tr>
</table>

<main>
  <div class="container p-0">
