#!/usr/bin/haserl
<%in _common.cgi %>
<%
qauto_focus=0;
qlight_control=0;
qfocus_in=0;
qalways_on=0;
qsim7600=0;
qfocus_port=0;
qfirst_step=0;
qircut_inv=0;
qfocus_control=0;
qec200t=0;
qsave_zf=0;
qfocus_threshold=0;
qauto_light=0;
qlight_port=0;
qlight_tr_on=0;
qlight_tr_off=0;
qdelay_tr=0;
qdelay_lt=0;
qapmode=0;
qbbsw=0;
qapname="00";
qcmid="0";
qcmkey="00000000";
qamkey="00000000";

data="$(printenv|grep POST_)"
IFS=$'\n' # make newlines the only separator
for name in $data; do
  key="$(echo $name | sed 's/^POST_//' | cut -d= -f1 )"
  value="$(echo $name | cut -d= -f2)"
if [ "$value" == "true" ]; then
  value="1";
fi
if [ "$value" == "on" ]; then
  value="1";
fi
if [ "$value" == "false" ]; then
  value="0";
fi
if [ "$key" == "focus-port" ]; then
  if [ "$value" == "" ]; then
    value="0";
  fi
fi
if [ "$key" == "first-step" ]; then
  if [ "$value" == "" ]; then
    value="0";
  fi
fi
if [ "$key" == "light-port" ]; then
  if [ "$value" == "" ]; then
    value="0";
  fi
fi
if [ "$key" == "light-tr-on" ]; then
  if [ "$value" == "" ]; then
    value="70";
  fi
fi
if [ "$key" == "light-tr-off" ]; then
  if [ "$value" == "" ]; then
    value="40";
  fi
fi

if [ "$key" == "focus-threshold" ]; then
  if [ "$value" == "" ]; then
    value="110";
  fi
fi
if [ "$key" == "apmode" ]; then
  if [ "$value" == "" ]; then
    value="0";
  fi
fi
if [ "$key" == "bbsw" ]; then
  if [ "$value" == "" ]; then
    value="0";
  fi
fi
if [ "$key" == "apname" ]; then
  if [ "$value" == "" ]; then
    value="00";
  fi
fi
if [ "$key" == "cmid" ]; then
  if [ "$value" == "" ]; then
    value="swit";
  fi
fi
if [ "$key" == "cmkey" ]; then
  if [ "$value" == "" ]; then
    value="swit.737";
  fi
fi
if [ "$key" == "amkey" ]; then
  if [ "$value" == "" ]; then
    value="10923874";
  fi
fi
if [ "$key" == "delay-tr" ]; then
  if [ "$value" == "" ]; then
    value="6";
  fi
fi
if [ "$key" == "delay-lt" ]; then
  if [ "$value" == "" ]; then
    value="10";
  fi
fi
if [ "$value" == "" ]; then
  value="0";
fi
if [ "$key" == "auto-focus" ]; then 
   qauto_focus="$value"; fi
if [ "$key" == "light-control" ]; then
   qlight_control="$value"; fi
if [ "$key" == "focus-in" ]; then
   qfocus_in="$value"; fi
if [ "$key" == "always-on" ]; then
   qalways_on="$value"; fi
if [ "$key" == "sim7600" ]; then
   qsim7600="$value"; fi
if [ "$key" == "focus-port" ]; then
   qfocus_port="$value"; fi
if [ "$key" == "first-step" ]; then
   qfirst_step="$value"; fi
if [ "$key" == "ircut-inv" ]; then
   qircut_inv="$value"; fi
if [ "$key" == "focus-control" ]; then
   qfocus_control="$value"; fi
if [ "$key" == "ec200t" ]; then
   qec200t="$value"; fi
if [ "$key" == "save-zf" ]; then
   qsave_zf="$value"; fi
if [ "$key" == "focus-threshold" ]; then
   qfocus_threshold="$value"; fi
if [ "$key" == "auto-light" ]; then
   qauto_light="$value"; fi
if [ "$key" == "light-port" ]; then
   qlight_port="$value"; fi
if [ "$key" == "light-tr-on" ]; then
   qlight_tr_on="$value"; fi
if [ "$key" == "light-tr-off" ]; then
   qlight_tr_off="$value"; fi
if [ "$key" == "apmode" ]; then
   qapmode="$value"; fi
if [ "$key" == "bbsw" ]; then
   qbbsw="$value"; fi
if [ "$key" == "apname" ]; then
   qapname="$value"; fi
if [ "$key" == "cmid" ]; then
   qcmid="$value"; fi
if [ "$key" == "cmkey" ]; then
   qcmkey="$value"; fi
if [ "$key" == "amkey" ]; then
   qamkey="$value"; fi
if [ "$key" == "delay-tr" ]; then
   qdelay_tr="$value"; fi
if [ "$key" == "delay-lt" ]; then
   qdelay_lt="$value"; fi
if [ "$key" == "newdat" ]; then
   qnewdat="$value"; fi
done
if [ "$qauto_focus" != "$(getenv auto-focus)" ]; then
  fw_setenv auto-focus $qauto_focus; fi
if [ "$qfirst_step" != "$(getenv first-step)" ]; then
  fw_setenv first-step $qfirst_step; fi

if [ "$qlight_control" != "$(getenv light-control)" ]; then
  fw_setenv light-control $qlight_control; fi
if [ "$qfocus_in" != "$(getenv focus-in)" ]; then
  fw_setenv focus-in $qfocus_in; fi
if [ "$qalways_on" != "$(getenv always-on)" ]; then
  fw_setenv always-on $qalways_on; fi

  fw_setenv sim7600 $qsim7600; 
  if [[ "$qsim7600" == "1" ]]
  then
    sed -i '27s/manual/auto/' /etc/network/interfaces
  else
    sed -i '27s/auto/manual/' /etc/network/interfaces
  fi

if [ "$qfocus_port" != "$(getenv focus-port)" ]; then
  fw_setenv focus-port $qfocus_port; fi
if [ "$qircut_inv" != "$(getenv ircut-inv)" ]; then
  fw_setenv ircut-inv $qircut_inv; fi
if [ "$qfocus_control" != "$(getenv focus-control)" ]; then
  fw_setenv focus-control $qfocus_control; fi

  fw_setenv ec200t $qec200t; 
  if [[ "$qec200t" == "1" ]]
  then
    sed -i '6s/manual/auto/' /etc/network/interfaces
  else
    sed -i '6s/auto/manual/' /etc/network/interfaces
  fi

if [ "$qsave_zf" != "$(getenv save-zf)" ]; then
  fw_setenv save-zf $qsave_zf; fi
if [ "$qfocus_threshold" != "$(getenv focus-threshold)" ]; then
  fw_setenv focus-threshold $qfocus_threshold; fi
if [ "$qauto_light" != "$(getenv auto-light)" ]; then
  fw_setenv auto-light $qauto_light; fi
if [ "$qlight_port" != "$(getenv light-port)" ]; then
  fw_setenv light-port $qlight_port; fi
if [ "$qlight_tr_on" != "$(getenv light-tr-on)" ]; then
  fw_setenv light-tr-on $qlight_tr_on; fi
if [ "$qlight_tr_off" != "$(getenv light-tr-off)" ]; then
  fw_setenv light-tr-off $qlight_tr_off; fi
snap=0;
if [ "$qapmode" != "$(getenv apmode)" ]; then
  fw_setenv apmode $qapmode; snap=1;
fi

  fw_setenv bbsw $qbbsw; 
  if [[ "$qbbsw" == "1" ]]
  then
    sed -i '56s/manual/auto/' /etc/network/interfaces
  else
    sed -i '56s/auto/manual/' /etc/network/interfaces
  fi
if [ "$qapname" != "$(getenv apname)" ]; then
  fw_setenv apname $qapname; snap=1; fi
if [ "$qcmid" != "$(getenv cmid)" ]; then
  fw_setenv cmid $qcmid; fi
if [ "$qcmkey" != "$(getenv cmkey)" ]; then
  fw_setenv cmkey $qcmkey; fi
if [ "$qamkey" != "$(getenv amkey)" ]; then
  fw_setenv amkey $qamkey;
  npsk="psk=\"$qamkey\"";
  sed -i '8d' /etc/wpa_supplicant.conf
  sed -i "8i \\$npsk" /etc/wpa_supplicant.conf
fi
if [ "$qdelay_tr" != "$(getenv delay-tr)" ]; then
  fw_setenv delay-tr $qdelay_tr; fi
if [ "$qdelay_lt" != "$(getenv delay-lt)" ]; then
  fw_setenv delay-lt $qdelay_lt; fi

if [ "$snap" == "1" ]; then
  cssid="gk300-$(gmnum)-$(getenv apname)";
  nssid="ssid=\"$cssid\"";
  sed -i '5d' /etc/wpa_supplicant.conf
  sed -i "5i \\$nssid" /etc/wpa_supplicant.conf
  echo $cssid > /etc/hostname
fi
date -s "$qnewdat" > /dev/null 
hwclock -w > /dev/null
#echo "$qauto_focus <br>";
#echo "$qlight_control<br>";
#echo "$qfocus_in<br>";
#echo "$qalways_on<br>";
#echo "$qsim7600<br>";
#echo "$qfocus_port<br>";
#echo "$qircut_inv<br>";
#echo "$qfocus_control<br>";
#echo "$qec200t<br>";
#echo "$qsave_zf<br>";
#echo "$qfocus_threshold<br>";
#echo "$qauto_light<br>";
#echo "$qlight_port<br>";
#echo "$qlight_threshold<br>";
#echo "$qnewdat<br>";
redirect_to "/cgi-bin/fl-settings.cgi"
%>

