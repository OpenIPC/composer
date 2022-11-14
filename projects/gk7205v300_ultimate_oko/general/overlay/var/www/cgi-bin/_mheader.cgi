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
/*        if ( data.stf == 0 ) 
          {
            document.getElementById("STF").innerHTML = "&#1053;&#1086;&#1088;&#1084;&#1091;&#1083;&#1100;";
          };
        if ( data.stf == 1 )
          {
            document.getElementById("STF").innerHTML = "&#1041;&#1083;&#1103;";
          };
        if ( data.stf == 2 )
          {
            document.getElementById("STF").innerHTML = "&#1058;&#1072; &#1085;&#1091; &#1085;&#1072;&#1093;";
          };
        if ( data.stf == 3 )
          {
            document.getElementById("STF").innerHTML = "&#1058;&#1072; &#1096;&#1086; &#1090;&#1072;&#1082;&#1086;&#1077;";
          };
        if ( data.stf == 4 )
          {
            document.getElementById("STF").innerHTML = "&#1058;&#1072;&#1085;&#1091;&#1085;&#1080;&#1105;&#1087;&#1090;&#1099;&#1090;&#1100;";
          };
        if ( data.stf == 5 )
          {
            document.getElementById("STF").innerHTML = " &#1055;&#1080;&#1079;&#1076;&#1077;&#1094; ";
          };
        if ( data.stf == 6 )
          {
            document.getElementById("STF").innerHTML = "&#1051;&#1077;&#1095;&#1080;&#1084;";
          }; */

            document.getElementById("STF").innerHTML = data.stf;

        if ( data.ld == 1 ) 
          {
            document.getElementById("light").src="/img/lt-on.svg";
          } else {
            document.getElementById("light").src="/img/lt-off.svg";
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
            role="button" data-bs-toggle="dropdown" aria-expanded="false">Information</a>
          <ul class="dropdown-menu" aria-labelledby="dropdownInformation">
            <li><a class="dropdown-item" href="/cgi-bin/status.cgi">Overview</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/info-cron.cgi">Cron config</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/info-dmesg.cgi">Diagnostic message</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/info-httpd.cgi">HTTPd environment</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/info-log.cgi">Log read</a></li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link" href="/cgi-bin/firmware.cgi">Firmware</a></li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" id="dropdownNetwork" href="#"
            role="button" data-bs-toggle="dropdown" aria-expanded="false">Settings</a>
          <ul class="dropdown-menu" aria-labelledby="dropdownNetwork">
            <li><a class="dropdown-item" href="/cgi-bin/network.cgi">Network Settings</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/network-ntp.cgi">NTP Settings</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/fl-settings.cgi">Extended  settings</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/webui-settings.cgi">Web UI Password</a></li>
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" id="dropdownMajestic" href="#"
            role="button" data-bs-toggle="dropdown" aria-expanded="false">Majestic</a>
          <ul class="dropdown-menu" aria-labelledby="dropdownMajestic">
            <li><a class="dropdown-item" href="/cgi-bin/majestic-settings-general.cgi">Settings</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/majestic-settings-services.cgi">Services</a></li>
           <li><a class="dropdown-item" href="/cgi-bin/majestic-config-actions.cgi">Maintenance</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/preview-help.cgi">Information</a></li>
          </ul>
        </li>
        <li class="nav-item  dropdown">
          <a class="nav-link dropdown-toggle" id="dropdownTools" href="#"
            role="button" data-bs-toggle="dropdown" aria-expanded="false">Tools</a>
          <ul class="dropdown-menu" aria-labelledby="dropdownTools">
            <li><a class="dropdown-item" href="/cgi-bin/tools.cgi">Ping & Traceroute</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/console.cgi">Web Console</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/format.cgi">Format SD & reboot</a></li>
          </ul>
        </li>
        <li class="nav-item  dropdown">
          <a class="nav-link dropdown-toggle" id="dropdownPreview" href="#"
            role="button" data-bs-toggle="dropdown" aria-expanded="false"><%= $tMenuPreview %></a>
          <ul class="dropdown-menu" aria-labelledby="dropdownPreview">
            <li><a class="dropdown-item" href="/cgi-bin/preview.cgi">JPEG</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/preview-mjpeg.cgi">MJPEG</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/preview-video.cgi">Video</a></li>
            <li><a class="dropdown-item" href="/cgi-bin/mpreview.cgi">Preview</a></li>
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
