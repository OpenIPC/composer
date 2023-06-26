# line format: parameter|label|units|type|o,p,t,i,o,n,s|placeholder|hint
# line format: parameter|type
mj_retired="
.system.sensorConfigDir|Путь к каталогу конфигурации датчиков||string||/etc/sensors|
.system.updateChannel|Канал для обновлений||select|testing,beta,stable,none|stable|
.isp.alignWidth|Выровнять ширину||number||8|
.isp.threadStackSize|Размер стека потоков|KB|number|1-32|16|
.motionDetect.profile|Профиль обнаружения движения||select|outdoor,indoor|indoor|i||
.raw.enabled|Включить поддержку необработанных фидов||boolean|true,false|false|
.raw.mode|Режим сырой подачи||select|slow,fast,none|slow|
"

# line format: parameter|label|units|type|o,p,t,i,o,n,s|placeholder|hint
# number options: min,max,step
# range options: min,max,step[,button]
# select options: value2,value2,value3...
mj="
.image.mirror|Перевернуть изображение по горизонтали||boolean|true,false|false|
.image.flip|Отразить изображение по вертикали||boolean|true,false|false|
.image.rotate|Повернуть изображение по часовой стрелке, °||select|0,90,270|0|
.image.contrast|Контраст изображения|%|range|1,100,1,auto|auto|
.image.hue|Оттенок изображения|%|range|1,100,1|50|
.image.saturation|Насыщенность изображения|%|range|1,100,1|50|
.image.luminance|Яркость изображения|%|range|1,100,1,auto|auto|
.osd.enabled|Включить экранное меню (OSD)||boolean|true,false|false|
.osd.font|Путь к файлу шрифта, используемому в экранного меню||string||/usr/share/fonts/truetype/UbuntuMono-Regular.ttf|
.osd.template|Шаблон экранного меню||string||%a %e %B %Y %H:%M:%S %Z|Поддержка формата <a href=\"https://man7.org/linux/man-pages/man3/strftime.3.html \" target=\"_blank\">strftime()</a>.
.osd.corner|Предустановленное положение экранного меню||select|tl:Сверху слева,tr:Сверху справа,bl:Снизу слева,br:Снизу справа|br|
.osd.posX|Горизонтальное положение экранного меню|px|number|-2000,2000,2|-100|
.osd.posY|Вертикальное положение экранного меню|px|number|-2000,2000,2|-100|
.osd.privacyMasks|Маски конфиденциальности|px|string||0x0x234x640,2124x0x468x1300|Координаты маскируемых областей через запятую.
.nightMode.enabled|Включить ночной режим||boolean|true,false|false|
.records.enabled|Включить сохранение записей||boolean|true,false|false|
.records.path|Шаблон для сохранения видеозаписей||string||/mnt/mmc/%Y/%m/%d/%H.mp4|Поддержка формата <a href=\"https://man7.org/linux/man-pages/man3/strftime.3.html \" target=\"_blank\">strftime()</a>.
.records.maxUsage|Ограничение использования доступного пространства|%|range|1,100,1|95|
.records.timelapseInterval|Интервал захвата ускоренной съемки|sec|number|1,65355,1|5|В секундах
.records.timelapseFrameRate|Частота кадров выходного файла ускоренной съемки|fps|number|1,100,1|2|В кадрах в секунду
.video0.enabled|Включить основной видеопоток||boolean|true,false|true|
.video0.codec|Кодек основного видеопотока||select|h264,h265|h264|
.video0.size|разрешение видео|px|string|1920x1080,1280x720,704x576|1920x1080|
.video0.fps|Частота кадров видео|fps|number|1,60,1|25|
.video0.bitrate|Битрейт видео|kbps|number|1,68000,1|4096|
.video0.gopSize|Отправка I-кадров каждую секунду||number|0.1,20,0.1|1|
.video0.gopMode|Режим групповых снимков (GOP)||select|normal,dual,smart|normal|
.video0.rcMode|режим дистанционного управления||select|avbr,cbr,vbr|avbr|
.video0.crop|Обрезать видео по размеру|px|string||0x0x960x540|
.video0.sliceUnits|Количество фрагментов на кадр||number|1,10,1|4
.video1.enabled|Включить дополнительный видеопоток||boolean|true,false|false|
.video1.codec|Кодек дополнительного видеопотока||select|h264,h265|h264|
.video1.size|Разрешение видео|px|string|1920x1080,1280x720,704x576|704x576|
.video1.fps|Частота кадров видео|fps|number|1,60,1|15|
.video1.bitrate|Битрейт видео|kbps|number|1,68000,1|2048|
.video1.gopSize|Отправка I-кадров каждую секунду||number|1,20,1|1|
.video1.gopMode|Режим групповых снимков (GOP)||select|normal,dual,smart|normal|
.video1.rcMode|режим дистанционного управления||select|avbr|avbr|
.video1.crop|Обрезать видео по размеру|px|string||0x0x960x540|
.video1.sliceUnits|Количество фрагментов на кадр||number|1,10,1|4
.jpeg.enabled|Включить поддержку JPEG||boolean|true,false|true|
.jpeg.size|Размер снимка|px|string||1920x1080|
.jpeg.qfactor|Уровень качества JPEG|%|range|1,100,1|50|
.jpeg.toProgressive|Progressive JPEG||boolean|true,false|false|
.audio.enabled|Включить звук||boolean|true,false|false|
.audio.volume|Уровень громкости звука|%|range|1,100,1,auto|auto|
.audio.srate|Частота дискретизации звука|kHz|number|1,96000,1|8000|
.audio.codec|Кодек для кодирования RTSP и MP4||select|mp3,opus,aac,pcm,alaw,ulaw|opus|
.audio.device|Аудио карта||string||hw:2|
.audio.outputEnabled|Включить аудиовыход||boolean|true,false|false|
.audio.outputGain|Выходное усиление||range|0,31,1|15|
.audio.outputVolume|Громкость динамика|%|range|0,100,1|0|
.audio.voiceEqualizer|Аудио эквалайзер||select|disabled,common,music,noisy|disabled|
.audio.speakerPin|Контакт GPIO аудиодинамика||number|1,255,1|32|
.audio.speakerPinInvert|Сигнал динамика инвертирован||boolean|true,false|false|
.rtsp.enabled|Включить вывод||boolean|true,false|true|
.rtsp.port|Порт для протокола RTSP||number|1,65535,1|554|rtsp://user:pass@${network_address}:[port]/stream={0,1}
.hls.enabled|Включить прямую трансляцию HTTP(HLS)||boolean|true,false|true|
.youtube.enabled|Включить поддержку Youtube||boolean|true,false|false|
.youtube.key|API-ключ Youtube||string||xxxx-xxxx-xxxx-xxxx-xxxx|
.motionDetect.enabled|Включить обнаружение движения||boolean|true,false|false|
.motionDetect.visualize|Визуализация обнаружения движения||boolean|true,false|true|
.motionDetect.debug|Включить отладку||boolean|true,false|true|
.motionDetect.roi|Области интереса (ROI) для обнаружения движения.|px|string||0x0x1296x760|
.motionDetect.skipIn|Регионы, исключенные из ROI.|px|string||20x20x200x300,510x330x40x15|
.ipeye.enabled|Включить поддержку IPEYE||boolean|true,false|false|
.onvif.enabled|Включить поддержку протокола ONVIF||boolean|true,false|false|
.cloud.enabled|Enable cloud supportВключить облачную поддержку||boolean|true,false|false|
"

# hide these settings unless in debug mode
mj_hide_unless_debug="audio_device isp_aGain isp_dGain isp_ispGain isp_exposure"

# conditional settings limiters
mj_show_audio_voiceEqualizer="gk7205v200 hi3516cv300 hi3516cv500 hi3516ev300 hi3519v101"
mj_show_mjpeg_vendor="goke hisilicon"
mj_show_isp_slowShutter_vendor="goke hisilicon"
mj_hide_isp_sensorConfig_vendor="ingenic"
mj_hide_video0_codec="hi3516cv200 hi3516cv100"
mj_hide_video1_codec="hi3516cv200 hi3516cv100"
mj_hide_motionDetect="hi3516cv100 hi3516av100"
