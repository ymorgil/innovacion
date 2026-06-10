# 🎬 OBS Studio
> **OBS Studio** (Open Broadcaster Software) es software gratuito y open source para grabación de vídeo y streaming en directo.

---

## Primeros pasos

### 1. Instalar OBS
Descarga desde [obsproject.com](https://obsproject.com){target="_blank"} → instala → al abrirlo por primera vez el **Asistente de configuración automática** te preguntará si quieres optimizar para *streaming* o *grabación*. **Déjalo hacer su trabajo.**

![obs](../assets/img/ate/obs-01.png){ width="900" }

| Concepto | Qué es |
|---|---|
| **Canvas** | La pantalla grande de previsualización en tiempo real. Lo que aparece ahí es exactamente lo que saldrá en tu vídeo. Puedes arrastrar y redimensionar las fuentes directamente sobre él. |
| **Escena** | Una "pantalla" completa con su propio conjunto de fuentes. Puedes tener varias y cambiar entre ellas. |
| **Fuente** | Cada elemento dentro de una escena: pantalla, webcam, imagen, texto, audio... |
| **Mezcla de audio** | Panel donde controlas los niveles de cada fuente de sonido. |
| **Transiciones de escenas** | Efecto visual al cambiar de una escena a otra (corte, fundido, etc.). |
| **Controles** | Panel con los botones principales: iniciar/parar streaming y grabación, modo estudio, y acceso a configuración. |
| **Perfil** | Configuración de salida guardada (útil para tener uno para streaming y otro para grabación). |


### 2. Crear tu primera escena
En el panel **Escenas** → clic en `+` y dar un nombre descriptivo, ej: `Escena 01`

![obs](../assets/img/ate/obs-02.png)

### 3. Añadir fuentes a la escena
En el panel **Fuentes** → clic en `+` y elegir el tipo:
![obs](../assets/img/ate/obs-03.png)

| Tipo de fuente | Para qué sirve |
|---|---|
| `Captura de pantalla` | Captura todo el monitor |
| `Captura de ventana` | Solo una aplicación concreta |
| `Dispositivo de captura de vídeo` | Webcam |
| `Fuente multimedia` | Vídeo/audio de un archivo |
| `Texto (GDI+)` | Añadir texto sobre la escena |
| `Imagen` | Logos, overlays, marcos |
| `Captura del juego` | Modo optimizado para videojuegos |

### 4. Ajustar audio  y salida
En **Mezclador de audio** verás tus micrófonos y audio del escritorio. Las barras deben quedarse en **verde/amarillo**, nunca en rojo. Clic en el engranaje ⚙️ de cada canal para filtros (reducción de ruido, compresión, etc.).

`Archivo` → `Ajustes` → sección **Salida**:

- **Modo simple** para empezar
- Codificador: `x264` (CPU) o `NVENC/AMF` si tienes GPU Nvidia/AMD
- Calidad de grabación: `Alta calidad, tamaño de archivo mediano`

![obs](../assets/img/ate/obs-04.png)

### 5. ¡Grabar o hacer streaming!
- **Iniciar grabación** → graba en tu disco
- **Iniciar streaming** → necesitas configurar antes la plataforma (Twitch, YouTube, etc.) en `Configuración → Emisión`

---

## Trucos y Atajos

- **Bloquear fuentes** — clic derecho sobre una fuente → `Bloquear` para que no la muevas sin querer.
- **Orden de fuentes importa** — las fuentes de arriba tapan a las de abajo (como capas en Photoshop).
- **Previsualización** — lo que ves en el canvas NO es lo que se graba hasta que das a grabar. Usa `Estudio` para ver ambas cosas a la vez.
- **Modo Estudio** — botón abajo a la derecha, permite preparar la siguiente escena antes de cambiar.
- **Filtros de vídeo** — clic derecho en una fuente → `Filtros` → puedes añadir corrección de color, máscara, recorte, etc.
- Ve a `Configuración → Atajos de teclado` y asigna teclas a las acciones que más uses. Por ejemplo: Iniciar/parar grabación, Iniciar/parar streaming, Silenciar micrófono, Cambiar de escena 






## 📁 Dónde se guardan las grabaciones

Por defecto en la **carpeta de vídeos** del sistema. Para cambiarlo:
`Configuración → Salida → Grabación → Ruta de grabación`



## 🔧 Configuración recomendada para empezar (grabación local)

```
Resolución base:    1920x1080
Resolución de salida: 1920x1080
FPS:                30 (o 60 si tu PC lo soporta)
Codificador:        x264 (o NVENC si tienes Nvidia)
Tasa de bits:       6000-8000 kbps (para alta calidad)
Formato de archivo: MKV (más seguro ante cortes de luz) → luego remuxear a MP4
```

> 💡 Graba en **MKV** y convierte a MP4 después con `Archivo → Remuxear grabaciones`. Si OBS se cierra inesperadamente, el MKV se puede recuperar; el MP4 no.

---

## 📚 Recursos para seguir aprendiendo

- 📖 Documentación oficial: [obsproject.com/wiki](https://obsproject.com/wiki)
- 💬 Foro oficial: [obsproject.com/forum](https://obsproject.com/forum)
- 🎥 Canal YouTube recomendado: busca **"OBS Studio tutorial español"**

---

*Generado como punto de partida para el curso de OBS · Actualiza esta hoja conforme avances* 🚀