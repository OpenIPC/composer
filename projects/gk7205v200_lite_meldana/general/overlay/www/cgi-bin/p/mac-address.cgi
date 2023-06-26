<div class="alert alert-danger">
<h3>Эта камера использует MAC-адрес <b>00:00:23:34:45:66</b> который является заполнителем.</h3>
<p>Вам необходимо заменить его оригинальным MAC-адресом из резервной копии стоковой прошивки или <a href="#" id="generate-mac-address">сгенерировать случайный действительный MAC-адрес</a>.</p>
<form action="network.cgi" method="POST" class="row gy-2 gx-3 align-items-center mb-3">
<input type="hidden" name="action" value="changemac">
<div class="col-auto"><label class="form-label" for="mac_address">Новый MAC-адрес</label></div>
<div class="col-auto"><input class="form-control" id="mac_address" name="mac_address"type="text"></div>
<div class="col-auto"><input class="btn btn-danger" type="submit" value="Сменить MAC-адрес"></div>
</form>
<p class="mb-0">Обратите внимание, что новый MAC-адрес, скорее всего, даст камере новый IP-адрес, назначенный DHCP-сервером!</p>
</div>

<script>
function generateMacAddress(ev) {
    ev.preventDefault();
    const el = document.querySelector('#mac_address');
    if (el.value == "") {
        let mac = "";
        for (let i = 1; i <= 6; i++) {
            let b = ((Math.random() * 255) >>> 0);
            if (i === 1) {
                b = b | 2;
                b = b & ~1;
            }
            mac += b.toString(16).toUpperCase().padStart(2, '0');
            if (i < 6) mac += ":";
        }
        el.value = mac;
    } else {
        alert("В поле MAC-адреса есть значение. Пожалуйста, очистите поле и повторите попытку.");
    }
}

window.addEventListener('load', function() {
  document.querySelector('#generate-mac-address').addEventListener('click', generateMacAddress);
});
</script>
