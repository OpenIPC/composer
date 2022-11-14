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
<h2>Extended settings</h2>
<div class="container p-3">
<form action="/cgi-bin/ext-settings-update.cgi" method="POST" autocomplete="off"> 
<div class="row row-cols-1 row-cols-xl-2 row-cols-xxl-3 g-4 mb-3"> 
<!-- ------------------------------------------------------------------------------------------------------------------------- --->
<div class="col">
 <div class="card h-100">
  <div class="card-header">Light</div>
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
       <label class="form-check-label" for="auto-light">Auto light</label>
     </div>
    </div>
   </div>

   <div class="row mb-2 number"> 
    <div class="col-md-7">
      <label class="form-label" for="light-tr-on">Lighting threshold turn-on</label>
    </div>
    <div class="col-md-5">
     <div class="input-group">
       <input class="form-control text-end" type="text" name="light-tr-on" id="light-tr-on" value="<%= `getenv light-tr-on` %>" placeholder="70">
     </div>
    </div>
   </div>
   <div class="row mb-2 number">
    <div class="col-md-7">
      <label class="form-label" for="light-tr-off">Lighting threshold turn-off</label>
    </div>
    <div class="col-md-5">
     <div class="input-group">
       <input class="form-control text-end" type="text" name="light-tr-off" id="light-tr-off" value="<%= `getenv light-tr-off` %>" placeholder="40">
     </div>
    </div>
   </div>
   <div class="row mb-2 number">
    <div class="col-md-7">
      <label class="form-label" for="delay-lt">Turn-off delay</label>
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
       <label class='form-check-label' for='always-on'>Always on</label>        
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
       <label class="form-check-label" for="light-control">Light control gpio/uart</label>
     </div>
    </div>
   </div>
   <div class="row mb-2 number"> 
    <div class="col-md-7"> 
      <label class="form-label" for="light-port">Uart/GPIO № for control</label>
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
       <label class="form-check-label" for="ircut-inv">IRCUT normal/inverse</label>
     </div>
    </div>
   </div>
  </div>
 </div>
</div>
<!-- ------------------------------------------------------------------------------------------------------------------------- --->
<div class="col">
 <div class="card h-100">
  <div class="card-header">Focus</div>
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
       <label class="form-check-label" for="auto-focus">Auto focus</label>
     </div>
    </div>
   </div>
   <div class="row mb-2 number"> 
    <div class="col-md-7">
      <label class="form-label" for="focus-threshold">Autofocus threshold</label>
    </div>
    <div class="col-md-5">
     <div class="input-group">
       <input class="form-control text-end" type="text" name="focus-threshold" id="focus-threshold" value="<%= `getenv focus-threshold` %>" placeholder="120">
     </div>
    </div>
   </div>
   <div class="row mb-2 number">
    <div class="col-md-7">
      <label class="form-label" for="delay-tr">Delay for triggered</label>
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
       <label class="form-check-label" for="focus-in">Autofocus incoming/outgoing</label>
     </div>
    </div>
   </div>
   <div class="row mb-2 boolean">
    <div class="col">
     <div class="form-check form-switch">
       <% if [[ "$(getenv focus-control)" == "1" ]]
        then
         echo "<input class='form-check-input' name='focus-control' id='focus-control' type='checkbox' checked='' role='switch'>";
        else
         echo "<input class='form-check-input' name='focus-control' id='focus-control' type='checkbox' role='switch'>";
       fi; %>
       <label class="form-check-label" for="focus-control">Focus control gpio/uart</label>
     </div>
    </div>
   </div>
   <div class="row mb-2 number"> 
    <div class="col-md-7"> 
      <label class="form-label" for="first-step">Initial number of scaling steps when</label>
    </div>
    <div class="col-md-5"> 
     <div class="input-group"> 
       <input class="form-control text-end" type="text" name="first-step" id="first-step" value="<%= `getenv first-step` %>" placeholder="4"> 
     </div> 
    </div> 
   </div> 
   <div class="row mb-2 number"> 
    <div class="col-md-7"> 
      <label class="form-label" for="focus-port">Uart № for control</label>
    </div>
    <div class="col-md-5"> 
     <div class="input-group"> 
       <input class="form-control text-end" type="text" name="focus-port" id="focus-port" value="<%= `getenv focus-port` %>" placeholder="0"> 
     </div> 
    </div> 
   </div> 
<!---   <div class="row mb-2 boolean">
    <div class="col">
     <div class="form-check form-switch">
       <% if [[ "$(getenv save-zf)" == "1" ]]
        then
         echo "<input class='form-check-input' name='save-zf' id='save-zf' type='checkbox' checked='' role='switch'>";
        else
         echo "<input class='form-check-input' name='save-zf' id='save-zf' type='checkbox' role='switch'>";
       fi; %>
       <label class="form-check-label" for="save-zf">Autosave manual zoom&focus</label>
     </div>
    </div> 
   </div>  -->
  </div>
 </div>
</div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
<div class="col">
 <div class="card h-100">
  <div class="card-header">LTE, Wifi, Interfnal network settings</div>
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

       <label class="form-check-label" for="sim7600">Sim7600</label>
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
       <label class="form-check-label" for="ec200t">EC200t-EU</label>
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
       <label class="form-check-label" for="bbsw">BBSW net enabled</label>
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
       <label class="form-check-label" for="apmode">AP Mode enabled</label>
     </div>
    </div>
   </div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
   <div class="row mb-2 number"> 
    <div class="col-md-7">
      <label class="form-label">AP Name: <b> gk300-<%= "$(gmnum)" %>-</b></label> 
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
      <label class="form-label">Key: </b></label> 
    </div>
    <div class="col-md-5">
     <div class="input-group">
       <input class="form-control" type="password" name="amkey" id="amkey" value="<%= `getenv amkey` %>">
     </div>
    </div>
   </div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
   <div class="alert alert"><b>Client mode settings.</b></div>
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
      <label class="form-label">Key: </b></label> 
    </div>
    <div class="col-md-5">
     <div class="input-group">
       <input class="form-control" type="password" name="cmkey" id="cmkey" value="<%= `getenv cmkey` %>">
     </div>
    </div>
   </div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
  </div>
 </div>
</div>
<!---   -----------------------------------------------------------------------------------------------------------   --->
</div>
  <input type="hidden" id="newdat" name="newdat" value="">
  <button type="submit" class="btn btn-primary">Save changes</button>
 </form>
</div>
<script type="text/javascript" language="javascript">
var d = new Date();
var e = formatDate(d);
document.getElementById('newdat').value = e;
</script>
<%in _footer.cgi %>

