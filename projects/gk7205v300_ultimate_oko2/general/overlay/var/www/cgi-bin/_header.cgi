<% http_header_html %>
<% reus=$(printenv REMOTE_USER) %>
<!DOCTYPE html>
<html lang="en">
<head>
<% if [ $reus = "oper" ]; then %><meta http-equiv="refresh" content="0;URL=/cgi-bin/opreview.cgi" /><% fi %>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title><% html_title "$page_title" %></title>
<link rel="shortcut icon" href="/favicon.png">
<link href="/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="/css/bootstrap.override.css">
<% if [ $HTTP_MODE = "development" ]; then %><link rel="stylesheet" href="/css/debug.css"><% fi %>
<script src="/js/bootstrap.bundle.min.js"></script>
<script src="/js/main.js"></script>
<script  type="text/javascript" language="javascript">
function fullscreen3(element) {
if(element.requestFullScreen) {
element.requestFullScreen();
} else if(element.mozRequestFullScreen) {
    element.mozRequestFullScreen();
} else if(element.webkitRequestFullScreen) {
    element.webkitRequestFullScreen();
}
}
function formatDate(date) {
  var hours = date.getHours();
  var minutes = date.getMinutes();
//  var ampm = hours >= 12 ? 'pm' : 'am';
//  hours = hours % 12;
//  hours = hours ? hours : 12;
  minutes = minutes < 10 ? '0'+minutes : minutes;
  var strTime = hours + ':' + minutes;
  return ( date.getFullYear() + "-" + (date.getMonth()+1) + "-" + date.getDate() + " " + strTime ) ;
}
fullscreen3(document.documentElement);
</script>
</head>

<body id="top" onLoad="load(); fullscreen3(document.documentElement);return false;">
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
<main>
  <div class="container p-0">
