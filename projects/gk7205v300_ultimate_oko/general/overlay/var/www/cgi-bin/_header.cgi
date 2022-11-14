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
    <a class="navbar-brand" href="/cgi-bin/status.cgi"><img src="/img/logo.svg" width="116" height="32" alt=""><%= "&nbsp;<b>gk300-$(gmnum)-$(getenv apname)</b>  $(date +%F) $(date +%H:%M)"%></a>
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
<main>
  <div class="container p-0">
