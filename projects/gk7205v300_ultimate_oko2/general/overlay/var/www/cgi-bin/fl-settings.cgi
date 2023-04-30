#!/usr/bin/haserl

<%in _common.cgi %>
<% page_title="Extended settings"
ipaddr=$(printenv | grep HTTP_HOST | cut -d= -f2 | cut -d: -f1)
button() {
  id=$(echo "${2// /_}" | tr '[:upper:]' '[:lower:]')
  echo "<img id=\"$id\" src=\"/img/${1}\" Onclick=\"$id();\" title=\"${2}\">"
}
%>
<%in _header.cgi %>
<h2>&#1056;&#1072;&#1089;&#1096;&#1080;&#1088;&#1077;&#1085;&#1085;&#1099;&#1077; &#1085;&#1072;&#1089;&#1090;&#1088;&#1086;&#1081;&#1082;&#1080;</h2>
<div class="container p-3">
<form action="/cgi-bin/ext-settings-update.cgi" method="POST" autocomplete="off"> 
<div class="row row-cols-1 row-cols-xl-2 row-cols-xxl-3 g-4 mb-3"> 
<!-- ------------------------------------------------------------------------------------------------------------------------- --->
<div class="col">
 <div class="card h-100">
  <div class="card-header">&#1055;&#1086;&#1076;&#1089;&#1074;&#1077;&#1090;&#1082;&#1072;</div>
  <div class="card-body">
   <div class="row mb-2 boolean">
    <div class="col">
      <div class="form-check form-switch">
      <% if [[ "$(getenv auto-light)" == "1" ]]
         then
          echo "<input class='form-check-input' name='auto-light' id='auto-light' type='checkbox' checked='' role='switch'>";
         else
          echo "<input class='form-check-input' name='auto-light' id='auto-light' type='checkbox' role='switch'>";
        fi; %>
       <label class="form-check-label" for="auto-light">&#1040;&#1074;&#1090;&#1086;-&#1087;&#1086;&#1076;&#1089;&#1074;&#1077;&#1090;&#1082;&#1072;</label>
     </div>
    </div>
   </div>

   <div class="row mb-2 number"> 
    <div class="col-md-7">
      <label class="form-label" for="light-tr-on">&#1055;&#1086;&#1088;&#1086;&#1075; &#1074;&#1082;&#1083;&#1102;&#1095;&#1077;&#1085;&#1080;&#1103;</label>
    </div>
    <div class="col-md-5">
     <div class="input-group">
       <input class="form-control text-end" type="text" name="light-tr-on" id="light-tr-on" value="<%= `getenv light-tr-on` %>" placeholder="70">
     </div>
    </div>
   </div>
   <div class="row mb-2 number">
    <div class="col-md-7">
      <label class="form-label" for="light-tr-off">&#1055;&#1086;&#1088;&#1086;&#1075; &#1086;&#1090;&#1082;&#1083;&#1102;&#1095;&#1077;&#1085;&#1080;&#1103;</label>
    </div>
    <div class="col-md-5">
     <div class="input-group">
       <input class="form-control text-end" type="text" name="light-tr-off" id="light-tr-off" value="<%= `getenv light-tr-off` %>" placeholder="40">
     </div>
    </div>
   </div>
   <div class="row mb-2 number">
    <div class="col-md-7">
      <label class="form-label" for="delay-lt">Задержка отключения</label>
    </div>
    <div class="col-md-5">
     <div class="input-group">
       <input class="form-control text-end" type="text" name="delay-lt" id="delay-lt" value="<%= `getenv delay-lt` %>" placeholder="10">
     </div>
    </div>
   </div>
   <div class="row mb-2 boolean">
    <div class="col">
      <div class="form-check form-switch">
       <% if [[ "$(getenv always-on)" == "1" ]]
         then
          echo "<input class='form-check-input' name='always-on' id='always-on' type='checkbox' checked=''  role='switch'>";
         else
          echo "<input class='form-check-input' name='always-on' id='always-on' type='checkbox' role='switch'>";
       fi; %>   
       <label class='form-check-label' for='always-on'>&#1042;&#1089;&#1077;&#1075;&#1076;&#1072; &#1074;&#1082;&#1083;&#1102;&#1095;&#1077;&#1085;&#1086;</label>        
     </div>
    </div>
   </div>
   <div class="row mb-2 boolean">
    <div class="col">
     <div class="form-check form-switch">
      <% if [[ "$(getenv light-control)" == "1" ]]
        then
          echo "<input class='form-check-input' name='light-control' id='light-control' type='checkbox' checked='' role='switch'>";
        else
          echo "<input class='form-check-input' name='light-control' id='light-control' type='checkbox' role='switch'>";
      fi; %>
       <label class="form-check-label" for="light-control">&#1059;&#1087;&#1088;&#1072;&#1074;&#1083;&#1077;&#1085;&#1080;&#1077; &#1095;&#1077;&#1088;&#1077;&#1079;  gpio/uart</label>
     </div>
    </div>
   </div>
   <div class="row mb-2 number"> 
    <div class="col-md-7"> 
      <label class="form-label" for="light-port">&#1053;&#1086;&#1084;&#1077;&#1088; &#1087;&#1086;&#1088;&#1090;&#1072; &#1091;&#1087;&#1088;&#1072;&#1074;&#1083;&#1077;&#1085;&#1080;&#1103; &#1076;&#1083;&#1103; Uart/GPIO</label>
    </div>
    <div class="col-md-5"> 
     <div class="input-group"> 
       <input class="form-control text-end" type="text" name="light-port" id="light-port" value="<%= `getenv light-port` %>" placeholder="4"> 
     </div> 
    </div> 
   </div> 
   <div class="row mb-2 boolean">
    <div class="col">
      <div class="form-check form-switch">
      <% if [[ "$(getenv ircut-inv)" == "1" ]]
        then
         echo "<input class='form-check-input' name='ircut-inv' id='ircut-inv' type='checkbox' checked='' role='switch'>";
        else
         echo "<input class='form-check-input' name='ircut-inv' id='ircut-inv' type='checkbox' role='switch'>";
      fi; %>
       <label class="form-check-label" for="ircut-inv">IRCUT &#1087;&#1088;&#1103;&#1084;&#1086;&#1081;/&#1080;&#1085;&#1074;&#1077;&#1088;&#1089;&#1085;&#1099;&#1081;</label>
     </div>
    </div>
   </div>
  </div>
 </div>
</div>
<!-- ------------------------------------------------------------------------------------------------------------------------- --->
<div class="col">
 <div class="card h-100">
  <div class="card-header">&#1059;&#1087;&#1088;&#1072;&#1074;&#1083;&#1077;&#1085;&#1080;&#1077; &#1092;&#1086;&#1082;&#1091;&#1089;&#1080;&#1088;&#1086;&#1074;&#1082;&#1086;&#1081;</div>
  <div class="card-body">
   <div class="row mb-2 boolean">
    <div class="col">
      <div class="form-check form-switch">
       <% if [[ "$(getenv auto-focus)" == "1" ]]
        then
         echo "<input class='form-check-input' name='auto-focus' id='auto-focus' type='checkbox' checked='' role='switch'>";
        else
         echo "<input class='form-check-input' name='auto-focus' id='auto-focus' type='checkbox' role='switch'>";
       fi; %>
       <label class="form-check-label" for="auto-focus">&#1040;&#1074;&#1090;&#1086;&#1092;&#1086;&#1082;&#1091;&#1089;</label>
     </div>
    </div>
   </div>
   <div class="row mb-2 number"> 
    <div class="col-md-7">
      <label class="form-label" for="focus-threshold">&#1055;&#1086;&#1088;&#1086;&#1075; &#1089;&#1088;&#1072;&#1073;&#1072;&#1090;&#1099;&#1074;&#1072;&#1085;&#1080;&#1103;</label>
    </div>
    <div class="col-md-5">
     <div class="input-group">
       <input class="form-control text-end" type="text" name="focus-threshold" id="focus-threshold" value="<%= `getenv focus-threshold` %>" placeholder="120">
     </div>
    </div>
   </div>
   <div class="row mb-2 number">
    <div class="col-md-5">
      <label class="form-label" for="delay-tr">&#1047;&#1072;&#1076;&#1077;&#1088;&#1078;&#1082;&#1072; &#1089;&#1088;&#1072;&#1073;&#1072;&#1090;&#1099;&#1074;&#1072;&#1085;&#1080;&#1103;</label>
    </div>
    <div class="col-md-5">
     <div class="input-group">
       <input class="form-control text-end" type="text" name="delay-tr" id="delay-tr" value="<%= `getenv delay-tr` %>" placeholder="6">
     </div>
    </div>
   </div>
   <div class="row mb-2 boolean">
    <div class="col">
      <div class="form-check form-switch">
       <% if [[ "$(getenv focus-in)" == "1" ]]
        then
         echo "<input class='form-check-input' name='focus-in' id='focus-in' type='checkbox' checked=''  role='switch'>";
        else
         echo "<input class='form-check-input' name='focus-in' id='focus-in' type='checkbox' role='switch'>";
       fi; %>
       <label class="form-check-label" for="focus-in">&#1055;&#1086;&#1080;&#1089;&#1082; &#1086;&#1090; &#1089;&#1077;&#1073;&#1103; / &#1082; &#1089;&#1077;&#1073;&#1077;</label>
     </div>
    </div>
   </div>
   <div class="row mb-2 boolean">
    <div class="col">
       <label class="form-label" for="focus-control">&#1059;&#1087;&#1088;&#1072;&#1074;&#1083;&#1077;&#1085;&#1080;&#1077; &#1087;&#1088;&#1080;&#1074;&#1086;&#1076;&#1072;&#1084;&#1080; &#1095;&#1077;&#1088;&#1077;&#1079;:</label><br />
     <div class="form-check form-switch">
       <% case "$(getenv focus-control)" in 
          0)
echo "<label><input name='focus-control' type='radio' value='0' checked='checked' />gpio</label><br />"
echo "<label><input type='radio' name='focus-control' value='1' />uart</label><br />"
echo "<label><input type='radio' name='focus-control' value='2' />i2c</label><br />"
                       ;;
          1)
echo "<label><input name='focus-control' type='radio' value='0' />gpio</label><br />"
echo "<label><input type='radio' name='focus-control' value='1' checked='checked' />uart</label><br />"
echo "<label><input type='radio' name='focus-control' value='2' />i2c</label><br />"
                       ;;
          2)
echo "<label><input name='focus-control' type='radio' value='0' />gpio</label><br />"
echo "<label><input type='radio' name='focus-control' value='1' />uart</label><br />"
echo "<label><input type='radio' name='focus-control' value='2' checked='checked' />i2c</label><br />"
                       ;;
          esac;
       %>
     </div>
    </div>
   </div>
   <div class="row mb-2 number"> 
    <div class="col-md-7"> 
      <label class="form-label" for="first-step">&#1050;-&#1074;&#1086; &#1096;&#1072;&#1075;&#1086;&#1074; &#1087;&#1088;&#1080;&#1073;&#1083;&#1080;&#1078;&#1077;&#1085;&#1080;&#1103; &#1087;&#1088;&#1080; &#1089;&#1090;&#1072;&#1088;&#1090;&#1077;</label>
    </div>
    <div class="col-md-5"> 
     <div class="input-group"> 
       <input class="form-control text-end" type="text" name="first-step" id="first-step" value="<%= `getenv first-step` %>" placeholder="4"> 
     </div> 
    </div> 
   </div> 
   <div class="row mb-2 number"> 
    <div class="col-md-7"> 
      <label class="form-label" for="focus-port">&#1053;&#1086;&#1084;&#1077;&#1088; &#1087;&#1086;&#1088;&#1090;&#1072; Uart &#1076;&#1083;&#1103; &#1091;&#1087;&#1088;&#1072;&#1074;&#1083;&#1077;&#1085;&#1080;&#1103;</label>
    </div>
    <div class="col-md-5"> 
     <div class="input-group"> 
       <input class="form-control text-end" type="text" name="focus-port" id="focus-port" value="<%= `getenv focus-port` %>" placeholder="0"> 
     </div> 
    </div> 
   </div> 
  </div>
 </div>
</div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
<div class="col">
 <div class="card h-100">
  <div class="card-header">&#1053;&#1072;&#1089;&#1090;&#1088;&#1086;&#1081;&#1082;&#1080; LTE, WiFi &#1080; &#1074;&#1085;&#1091;&#1090;&#1088;&#1077;&#1085;&#1085;&#1080;&#1093; &#1089;&#1077;&#1090;&#1077;&#1081;</div>
  <div class="card-body">
<div class="alert alert-danger"><b>&#1042;&#1085;&#1080;&#1084;&#1072;&#1085;&#1080;&#1077; &#1085;&#1077;&#1082;&#1086;&#1088;&#1088;&#1077;&#1082;&#1090;&#1085;&#1072;&#1103; &#1085;&#1072;&#1089;&#1090;&#1088;&#1086;&#1081;&#1082;&#1072; &#1084;&#1086;&#1078;&#1077;&#1090; &#1087;&#1088;&#1080;&#1074;&#1077;&#1089;&#1090;&#1080; &#1082; &#1087;&#1086;&#1083;&#1085;&#1086;&#1081; &#1087;&#1086;&#1090;&#1077;&#1088;&#1077; &#1089;&#1074;&#1103;&#1079;&#1080; &#1089; &#1082;&#1072;&#1084;&#1077;&#1088;&#1086;&#1081;.</b></div>
   <div class="row mb-2 boolean">
    <div class="col">
      <div class="form-check form-switch">
       <% if [[ "$(getenv sim7600)" == "1" ]]
        then
         echo "<input class='form-check-input' name='sim7600' id='sim7600' type='checkbox' checked='' role='switch'>";
        else
         echo "<input class='form-check-input' name='sim7600' id='sim7600' type='checkbox' role='switch'>";
       fi; %>

       <label class="form-check-label" for="sim7600">&#1052;&#1086;&#1076;&#1077;&#1084; Sim7600</label>
     </div>
    </div>
   </div>
   <div class="row mb-2 boolean">
    <div class="col">
      <div class="form-check form-switch">
       <% if [[ "$(getenv ec200t)" == "1" ]]
        then
         echo "<input class='form-check-input' name='ec200t' id='ec200t' type='checkbox' checked='' role='switch'>";
        else
         echo "<input class='form-check-input' name='ec200t' id='ec200t' type='checkbox' role='switch'>";
       fi; %>
       <label class="form-check-label" for="ec200t">&#1052;&#1086;&#1076;&#1077;&#1084; EC200t-EU</label>
     </div>
    </div>
   </div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
   <div class="row mb-2 boolean">
    <div class="col">
      <div class="form-check form-switch">
       <% if [[ "$(getenv bbsw)" == "1" ]]
        then
         echo "<input class='form-check-input' name='bbsw' id='bbsw' type='checkbox' checked='' role='switch'>";
        else
         echo "<input class='form-check-input' name='bbsw' id='bbsw' type='checkbox' role='switch'>";
       fi; %>
       <label class="form-check-label" for="bbsw">&#1057;&#1074;&#1103;&#1079;&#1100; &#1089; &#1088;&#1072;&#1079;&#1088;&#1072;&#1073;&#1086;&#1090;&#1095;&#1080;&#1082;&#1086;&#1084;</label>
     </div>
    </div>
   </div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
   <div class="row mb-2 boolean">
    <div class="col">
      <div class="form-check form-switch">
       <% if [[ "$(getenv apmode)" == "1" ]]
        then
         echo "<input class='form-check-input' name='apmode' id='apmode' type='checkbox' checked='' role='switch'>";
        else
         echo "<input class='form-check-input' name='apmode' id='apmode' type='checkbox' role='switch'>";
       fi; %>
       <label class="form-check-label" for="apmode">&#1056;&#1077;&#1078;&#1080;&#1084; &#1090;&#1086;&#1095;&#1082;&#1080; &#1076;&#1086;&#1089;&#1090;&#1091;&#1087;&#1072; &#1074;&#1082;&#1083;&#1102;&#1095;&#1077;&#1085;</label>
     </div>
    </div>
   </div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
   <div class="row mb-2 number"> 
    <div class="col-md-7">
      <label class="form-label">&#1048;&#1084;&#1103; &#1090;&#1086;&#1095;&#1082;&#1080; &#1076;&#1086;&#1089;&#1090;&#1091;&#1087;&#1072;: <b> gk300-<%= "$(gmnum)" %>-</b></label> 
    </div>
    <div class="col-md-5">
     <div class="input-group">
       <input class="form-control text-end" type="text" name="apname" id="apname" value="<%= `getenv apname` %>" placeholder="00">
     </div>
    </div>
   </div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
   <div class="row mb-2 number"> 
    <div class="col-md-7">
      <label class="form-label">&#1050;&#1083;&#1102;&#1095;: </b></label> 
    </div>
    <div class="col-md-5">
     <div class="input-group">
       <input class="form-control" type="password" name="amkey" id="amkey" value="<%= `getenv amkey` %>">
     </div>
    </div>
   </div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
   <div class="alert alert"><b>&#1055;&#1086;&#1076;&#1082;&#1083;&#1102;&#1095;&#1077;&#1085;&#1080;&#1077; &#1082; &#1089;&#1077;&#1090;&#1080; WiFi</b></div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
   <div class="row mb-2 number"> 
    <div class="col-md-7">
      <label class="form-label">SSID: </b></label> 
    </div>
    <div class="col-md-5">
     <div class="input-group">
       <input class="form-control" type="text" name="cmid" id="cmid" value="<%= `getenv cmid` %>" placeholder="ssid">
     </div>
    </div>
   </div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
   <div class="row mb-2 number"> 
    <div class="col-md-7">
      <label class="form-label">&#1050;&#1083;&#1102;&#1095;: </b></label> 
    </div>
    <div class="col-md-5">
     <div class="input-group">
       <input class="form-control" type="password" name="cmkey" id="cmkey" value="<%= `getenv cmkey` %>">
     </div>
    </div>
   </div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
   <div class="alert alert"><b>Wi-Fi 5GHz &#1084;&#1086;&#1076;&#1091;&#1083;&#1100;.</b></div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
   <div class="row mb-2 boolean">
    <div class="col">
      <div class="form-check form-switch">
       <% if [[ "$(getenv wifif)" == "1" ]]
        then
         echo "<input class='form-check-input' name='wifif' id='wifif' type='checkbox' checked='' role='switch'>";
        else
         echo "<input class='form-check-input' name='wifif' id='wifif' type='checkbox' role='switch'>";
       fi; %>
       <label class="form-check-label" for="wifif">Wi-Fi 5GHz &#1084;&#1086;&#1076;&#1091;&#1083;&#1100; &#1074;&#1082;&#1083;&#1102;&#1095;&#1077;&#1085;</label>
     </div>
    </div>
   </div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
   <div class="row mb-2 number">
    <div class="col-md-7">
      <label class="form-label">SSID: </b></label>
    </div>
    <div class="col-md-5">
     <div class="input-group">
       <input class="form-control" type="text" name="cmidf" id="cmidf" value="<%= `getenv cmidf` %>" placeholder="ssid">
     </div>
    </div>
   </div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
   <div class="row mb-2 number">
    <div class="col-md-7">
      <label class="form-label">&#1050;&#1083;&#1102;&#1095;: </b></label>
    </div>
    <div class="col-md-5">
     <div class="input-group">
       <input class="form-control" type="password" name="cmkeyf" id="cmkeyf" value="<%= `getenv cmkeyf` %>">
     </div>
    </div>
   </div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
<!---   -----------------------------------------------------------------------------------------------------------   --->
  </div>
 </div>
</div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
</div>
  <input type="hidden" id="newdat" name="newdat" value="">
  <button type="submit" class="btn btn-primary">&#1057;&#1086;&#1093;&#1088;&#1072;&#1085;&#1080;&#1090;&#1100; &#1080;&#1079;&#1084;&#1077;&#1085;&#1077;&#1085;&#1080;&#1103;</button>
 </form>
</div>
<script type="text/javascript" language="javascript">
var d = new Date();
var e = formatDate(d);
document.getElementById('newdat').value = e;
</script>
<%in _footer.cgi %>

