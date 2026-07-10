# 🪪 Certificado Digital: guía completa de obtención y uso

> El **certificado digital** (o certificado electrónico) es un documento digital que acredita tu identidad en internet y te permite firmar y realizar trámites con la Administración Pública (AEAT, Seguridad Social, Sede electrónica del Gobierno de Canarias, sede de tu ayuntamiento, etc.) sin tener que desplazarte. Esta guía recoge las distintas vías para obtenerlo, las apps móviles disponibles, cómo funciona la plataforma **Cl@ve** y una recomendación práctica del autor sobre el método más cómodo hoy en día.

## 1. Formas de obtener el certificado digital

Existen varias vías oficiales, con distinto nivel de comodidad y requisitos. Todas terminan en el mismo resultado: un certificado válido para identificarte ante las administraciones.

| Método | Dónde se solicita | Necesitas | Presencialidad |
|---|---|---|---|
| **FNMT — Certificado software (web + oficina)** | [sede.fnmt.gob.es](https://www.sede.fnmt.gob.es/certificados/persona-fisica){target="_blank"} | DNI/NIE, correo electrónico | Sí, una vez en una Oficina de Acreditación de Identidad |
| **FNMT — App móvil con NFC (DNIe 3.0)** | App *Certificado digital FNMT* (Android/iOS) | DNI electrónico con NFC activo, CAN y PIN del DNIe | No, se hace desde el móvil |
| **Cl@ve PIN / Cl@ve Permanente** | [clave.gob.es](https://clave.gob.es){target="_blank"} o en una oficina de registro Cl@ve | DNIe/certificado o carta de invitación | Depende del método de alta elegido |
| **DNIe (DNI electrónico) directo** | Se expide junto con el DNI en la comisaría | Lector de tarjetas con chip o móvil NFC + PIN del DNIe | Sí, para expedir/renovar el DNI |

### 1.1 Certificado FNMT clásico (software)

El proceso oficial tiene tres fases obligatorias:

1. **Solicitud vía web**: entra en [sede.fnmt.gob.es → Certificados → Persona física](https://www.sede.fnmt.gob.es/certificados/persona-fisica){target="_blank"} y solicita el certificado con tu DNI/NIE y un correo electrónico. Al terminar recibirás un **código de solicitud**.
2. **Acreditación de identidad presencial**: con ese código y tu DNI/NIE/pasaporte original, acude a una [Oficina de Acreditación de Identidad](https://www.sede.fnmt.gob.es/certificados/persona-fisica/obtener-certificado-software/acreditar-identidad){target="_blank"} (delegaciones de la AEAT, ayuntamientos, etc. — hay un buscador de oficinas en la propia web).
3. **Descarga del certificado**: de vuelta en el **mismo ordenador y navegador** donde hiciste la solicitud, descarga el certificado con el código de solicitud.

[captura pendiente: pantalla de inicio de sede.fnmt.gob.es con las opciones "Solicitar certificado", "Acreditar identidad" y "Descargar certificado"]

> ⚠️ Debe ser el mismo equipo y navegador en los tres pasos, porque el proceso genera una clave privada local en ese navegador que se necesita para completar la descarga.

### 1.2 FNMT mediante la app móvil (sin oficina)

Desde 2023 la FNMT permite obtener el certificado **sin acudir a ninguna oficina**, leyendo el chip NFC del DNI electrónico con el móvil. Se explica en detalle en el punto 2.

### 1.3 A través de Cl@ve

**Cl@ve** no es exactamente un certificado digital, sino un sistema de identificación alternativo (usuario/contraseña o app) que muchas sedes electrónicas aceptan igual que un certificado. Se explica en el punto 3.

## 2. App de móvil para obtener y usar certificados

Hay dos apps oficiales que conviene distinguir, porque tienen usos distintos:

| App | Qué hace | Descarga |
|---|---|---|
| **Certificado digital FNMT** | Solicita y genera el certificado leyendo el DNIe por NFC. Es la que sustituye a ir a una oficina. | [Google Play](https://play.google.com/store/apps/details?id=es.fnmtrcm.ceres.certificadoDigitalFNMT){target="_blank"} · [App Store](https://apps.apple.com/es/app/certificado-digital-fnmt/id6449721772){target="_blank"} |
| **Cl@ve** | Sirve para **usar** Cl@ve Móvil (autenticarte escaneando un QR o confirmando una notificación push), no para generar certificados. | Buscar "Cl@ve" en la tienda de tu móvil |

### 2.1 Pasos para obtener el certificado con la app FNMT (NFC)

1. Instala la app **Certificado digital FNMT** en un móvil con NFC.
2. Abre la app → **Solicitud Certificado Digital** → **Lectura DNIe**.
3. Introduce tu correo electrónico, el **CAN** (número de 6 dígitos que aparece en la parte inferior del DNI, junto a la firma) y el **PIN del DNIe** (el que te entregó la Policía Nacional al recogerlo).
4. Coloca el DNI en la parte trasera superior del móvil (zona de la antena NFC) y pulsa **Leer DNIe**. Es recomendable apoyar el móvil y el DNI sobre una mesa para que la lectura no falle.
5. En unos segundos recibes el certificado en formato `.p12`, listo para instalar en el ordenador.

[captura pendiente: pasos de la app "Certificado digital FNMT" — pantalla de introducción de CAN/PIN y pantalla de lectura NFC del DNIe]

> Requisito imprescindible: el **PIN del DNIe** debe conocerse y estar activo. Si no lo recuerdas, consulta el punto 4.

## 3. La plataforma Cl@ve y sus métodos de acceso

La imagen que suele aparecer al entrar en cualquier sede electrónica (AEAT, Seguridad Social, Sede Electrónica de Canarias, etc.) es el **selector de identificación de Cl@ve**, con tres tarjetas:

[captura pendiente: pantalla del selector "Plataforma de identificación para las Administraciones" con las tres tarjetas Cl@ve Móvil, DNIe/Certificado electrónico y Cl@ve permanente]

### 3.1 Cl@ve Móvil *(la opción "NOVEDAD")*

- Sistema sin contraseñas: te identificas **escaneando un código QR** o **confirmando la notificación push** que llega a la app Cl@ve.
- Si no puedes usar la app, te ofrece como alternativa un **PIN por SMS**.
- Incluye **Cl@ve PIN**: una contraseña de un solo uso y validez muy limitada (pensada para trámites puntuales, sin necesidad de recordar contraseñas permanentes).
- Requiere estar **registrado previamente** en el sistema Cl@ve (por videollamada desde la propia app, con certificado electrónico, o con carta de invitación).

### 3.2 DNIe / Certificado electrónico

- Vale **cualquier certificado electrónico cualificado**: el de la FNMT, el del propio DNIe, o certificados de otras entidades como la Fábrica Nacional de Moneda y Timbre (FNMT–RCM), Camerfirma, ANF, etc.
- Para usarlo con el DNIe físico hace falta un **lector de tarjetas con chip** conectado al ordenador (o, si es un DNIe 3.0, lectura por NFC desde el móvil con **AutoFirma**/app compatible).
- Es la opción más habitual una vez ya tienes el certificado instalado en tu equipo (ver puntos 1 y 2).

### 3.3 Cl@ve permanente

- Sistema de **usuario y contraseña**, reforzado con un código de un solo uso enviado por SMS para los trámites de nivel alto.
- Pensado para quien accede **con frecuencia**, ya que la contraseña no caduca tan rápido como en Cl@ve PIN.
- Es necesario **registrarse** antes de poder usarla (botón "Registrarse" en la propia pantalla de selección).

### 3.4 ¿Cuál elegir?

- Si ya tienes el certificado instalado en tu ordenador o móvil → **DNIe / Certificado electrónico**.
- Si solo tienes el DNI físico y el móvil a mano, sin certificado instalado → **Cl@ve Móvil**.
- Si vas a hacer trámites con mucha frecuencia (por ejemplo, gestión diaria de la web del centro o de nóminas) → merece la pena registrarse en **Cl@ve permanente**.

## 4. Consejo del autor: la vía más práctica

Mi recomendación personal, la que suelo aplicar y aconsejar, es la siguiente:

1. **Verifica o actualiza el PIN de tu DNIe.** Acude con el móvil a la comisaría más cercana (a la zona de expedición del DNI) y busca los **Puntos de Actualización del DNI (PAD)**: son unos terminales tipo cajero automático donde introduces el DNI y estableces un PIN nuevo que tú puedas recordar (entre 8 y 16 caracteres alfanuméricos). No hace falta cita previa. Si no recuerdas el PIN actual, el propio terminal puede verificarte por huella dactilar para permitirte establecer uno nuevo.
2. **Descarga la app "Certificado digital FNMT"** en el móvil (ver punto 2.1).
3. Con el DNI actualizado y el móvil con NFC, **genera el certificado** siguiendo los pasos de lectura NFC (CAN + PIN nuevo + lectura del chip).
4. **Guarda el certificado** (`.p12`) enviándotelo por correo electrónico o subiéndolo a tu Drive.
5. En el ordenador donde lo vayas a usar, descarga ese archivo desde el correo/Drive e **instálalo haciendo doble clic** sobre él (se añade automáticamente al almacén de certificados del navegador/sistema).
6. A partir de ahí, ya puedes usar la opción **DNIe / Certificado electrónico** en cualquier sede electrónica sin pasos adicionales.

Es, en mi opinión, el camino más rápido: evita pedir cita, evita desplazarte a una oficina de acreditación y todo el proceso (renovar PIN + generar certificado) se hace en una sola visita a comisaría más unos minutos desde el móvil.

## 5. Alternativa: solicitud clásica en la FNMT

Si prefieres el método tradicional, o el DNIe no admite lectura NFC (modelos antiguos), la otra vía es la explicada en el punto 1.1:

1. Entra en la [sede de la FNMT](https://www.sede.fnmt.gob.es/certificados/persona-fisica){target="_blank"} y **solicita el certificado digital** con tu DNI/NIE y correo electrónico. Guarda el código de solicitud que te envían.
2. Acude **físicamente a una entidad de registro** (Oficina de Acreditación de Identidad) para que verifiquen que eres tú quien lo ha solicitado, presentando el DNI/NIE/pasaporte original.
3. Vuelve al **mismo ordenador y navegador** donde hiciste la solicitud inicial y **descarga el certificado** con el código recibido.

> ⚠️ **Importante — seguridad**: si descargas el certificado en un ordenador que **no es tuyo** (por ejemplo, un equipo compartido del centro o de un ciber), debes **eliminarlo** del almacén de certificados en cuanto termines el trámite. Un certificado digital equivale a tu firma; dejarlo instalado en un equipo ajeno permite que cualquiera con acceso a ese ordenador se identifique como tú.

## 📚 Recursos

- 🌐 Sede electrónica FNMT — Persona física: [sede.fnmt.gob.es/certificados/persona-fisica](https://www.sede.fnmt.gob.es/certificados/persona-fisica){target="_blank"}
- 📱 App Certificado digital FNMT: [Google Play](https://play.google.com/store/apps/details?id=es.fnmtrcm.ceres.certificadoDigitalFNMT){target="_blank"} · [App Store](https://apps.apple.com/es/app/certificado-digital-fnmt/id6449721772){target="_blank"}
- 🔑 Plataforma Cl@ve: [clave.gob.es](https://clave.gob.es){target="_blank"}
- 📱 App Cl@ve (para Cl@ve Móvil): buscar "Cl@ve" en Google Play / App Store
- 🪪 Portal del DNI electrónico (cambio de PIN, PAD): [dnielectronico.es](https://www.dnielectronico.es){target="_blank"}
- ✍️ AutoFirma (firma electrónica en escritorio): [firmaelectronica.gob.es/Home/Descargas.html](https://firmaelectronica.gob.es/Home/Descargas.html){target="_blank"}
