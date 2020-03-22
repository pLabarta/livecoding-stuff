# Como streamear usando OBS

~esta guía es una traducción adaptada de la guía para streamear creada para el Equinoxio de Euleroom~

---

## Instrucciones

Lo primero es descargar e iniciar **Open Broadcaster Software** u **OBS** para les amigues, un programa gratuito y open-source para streamear y grabar video. Se consigue [acá](https://obsproject.com/ ).

Vamos a tener que tocar la configuración para que todo funcione correctamente. Deberías ver un boton que dice "Settings", tocalo y vas a ver una pantalla como esta:

![obs-1](/home/pablitx/Documents/Textos Clic/guia-OBS/img/obs-1.png)

---

## Stream

Tocá al costado izquierdo donde dice **"Stream"** y seleccioná a dónde queres streamear. Acá hay varias opciones, YouTube, Twitch, etc, e incluso la posibilidad de streamear a una URL personalizada. Para conocer cómo configurar esta parte, podés visitar la documentación de cada plataforma.

- YouTube: [https://support.google.com/youtube/answer/2907883?hl=es](https://support.google.com/youtube/answer/2907883?hl=es)
- Twitch: [https://help.twitch.tv/s/article/creator-dashboard?language=es_MX](https://help.twitch.tv/s/article/creator-dashboard?language=es_MX)

---

## Output

Luego de configurar a dónde va a ir el video, tenemos que configurar cómo va a salir ese video. Entonces vamos a la pestaña **"Output"**. Lo conveniente y a prueba de toda conexión es configurar el `video bitrate` en `500` y el `audio bitrate` en 128.

![obs-2](/home/pablitx/Documents/Textos Clic/guia-OBS/img/obs-2.png)

Esto es bastante bajo, especialmente si est[as trabajando con gráficos más allá de sonido. Sin embargo, mucha gente suele tener conexión de subida lenta. Podés tener una conexión de descarga muy rápida, pero la mayoría de los proveedores son bastante ratones y la subida, que usamos para transmitir el video, es lenta. Podés verificar tu velocidad acá: [http://www.speedtest.net/](http://www.speedtest.net/)

Si estás segura de que contás con una conexión rápida, podés probar configurando el `video bitrate` m[as alto, digamos en `1500`.

---

## Audio

En la parte de **"Audio"**, no hace falta configurar nada, pero se ve así:

![obs-3](/home/pablitx/Documents/Textos Clic/guia-OBS/img/obs-3.png)

---

## Video

![obs-4](/home/pablitx/Documents/Textos Clic/guia-OBS/img/obs-4.png)

Acá vamos a configurar los **FPS** (frames per second/cuadros por segundo) en `10` y el `Output (Scaled) Resolution` en **854x480**. Si tu conexión es rápida, sentite libre de ponerle una resolución mayor, como **1280x720** y subir los FPS a **20** o más. Andá probando distintas combinaciones de bitrate, resolución y FPS hasta encontrar una que se vea y funcione bien.

Estas son las redomendaciones de YouTube: [https://support.google.com/youtube/answer/2853702?hl=es-419](https://support.google.com/youtube/answer/2853702?hl=es-419)

---

## ¿Qué querés transmitir?

Dale aplicar y OK a la configuración para volver a la patalla principal. Ahora vamos a configurar la transmisión en si misma, lo que queremos que se vea y se escuche.

![obs-5](/home/pablitx/Documents/Textos Clic/guia-OBS/img/obs-5.png)

OBS tiene cuatro columnas en la parte inferior: Scenes, Sources, Mixer y Scene Transitions.

Vas a tener que agregar fuentes en la parte de Sources para capturar video de tus ventanas o toda tu pantalla. También podés agregar imágenes, textos y otras cosas lindas. En **Linux** podemos agregar entradas de Jack para enviarle el audio a OBS directo desde nuestro motor de sonido, sea SuperCollider u otro.

Podés experimentar agregando fuentes de **webcams**, implementando **filtros** y otras **cosas divertidas**. OBS permite hacer un monton de cosas. **¡A explorar!**

### macOS

La mejor opción para enviar sonido desde otra aplicación a OBS es usar [Blackhole](https://github.com/ExistentialAudio/BlackHole). Acá hay una guía para hacerlo con SuperCollider que debería funcionar también para TidalCycles: [https://jsimonvanderwalt.com/2020/03/14/sound-from-supercollider-to-obs-on-macos](https://jsimonvanderwalt.com/2020/03/14/sound-from-supercollider-to-obs-on-macos) (está en inglés). 

Otra opción es [Loopback](https://rogueamoeba.com/loopback/).

### Güindous (Windows)

Si estás usando Windows, probá usando cables de audio virtuales ([http://vb-audio.pagesperso-orange.fr/Cable/index.htm](http://vb-audio.pagesperso-orange.fr/Cable/index.htm)).

### Linux

Si estás usando Linux, probablemente tengas que configurar un cable usando [**Qjackctrl**](https://qjackctl.sourceforge.io/), que también puede sr instalado desde tu administrador de paquetes. Si lográs mandarle el cable a OBS, vas a ver que los indicadores de sonido para esa entrada se mueven. Fijate que no sea la del microfono de la computadora, tiene que ser la entrada que configuraste para Jack.

**Linux users:** In linux based systems, you may need to set up a patch (wire) in qjackctrl (https://qjackctl.sourceforge.io/, install it via your package manager), and start the jack server, even if you don’t need to use it for everyday playing anymore.

---

## Mandale cumbia

Ahora podes tocar el boton Start Streaming para empezar a transmitir o Start Recording para empezar a grabar. Si queres hacer ambas, tocá los dos.

---

**Hecho con <3 por [CLiC](https://colectivo-de-livecoders.gitlab.io/)**







