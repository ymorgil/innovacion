#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Descarga los documentos oficiales de la convocatoria de Proyectos de Innovación
en Formación Profesional de la Consejería de Educación de Canarias (curso 2026-2027).

POR QUÉ EXISTE ESTE SCRIPT
--------------------------
El asistente de IA que preparó esta carpeta no tiene acceso de red para descargar
archivos binarios (PDF/ODT) desde gobiernodecanarias.org. Este script hace ese
trabajo por ti: ejecútalo una vez en tu propio ordenador y descargará los 13
documentos oficiales en la subcarpeta "documentos-oficiales".

CÓMO USARLO
-----------
1. Necesitas Python 3 instalado (en Windows: https://www.python.org/downloads/).
   No hace falta instalar nada más: el script solo usa librerías estándar de Python.
2. Abre una terminal (PowerShell o CMD) en esta carpeta.
3. Ejecuta el script:
       python descargar_documentos_consejeria.py
4. Los archivos aparecerán en: consejeria/documentos-oficiales/

Si el año que viene la Consejería cambia las URL de la convocatoria, actualiza el
diccionario DOCUMENTOS de más abajo con los nuevos enlaces (los encontrarás en
https://www.gobiernodecanarias.org/educacion/web/formacion_profesional/programas_proyectos/proyectos_innovacion/).
"""

import os
import sys
import urllib.request
import urllib.error

# Carpeta donde se guardarán los documentos (junto a este script)
CARPETA_DESTINO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "documentos-oficiales")

BASE = "https://www.gobiernodecanarias.org/cmsgob1/export/sites/educacion/web/_galerias/descargas"

# nombre_de_archivo_local -> URL oficial
DOCUMENTOS = {
    "01-resolucion-154-2026-proyectos-innovacion.pdf": f"{BASE}/normativa-internas/resolucion-154-proyectos-innovacion-dgfpere-2627.pdf",
    "02-anexo-I-instrucciones.pdf": f"{BASE}/otros/anexo_I_instrucciones.pdf",
    "03-anexo-II-solicitud-participacion.pdf": f"{BASE}/otros/anexo_II_solicitud_participacion.pdf",
    "04-anexo-III-memoria-descriptiva-proyectos-nuevos.odt": f"{BASE}/otros/anexo_III_memoria_descriptiva_proyectos_nuevos.odt",
    "05-anexo-IV-memoria-descriptiva-continuidad.odt": f"{BASE}/otros/anexo_IV_memoria-_escriptiva_proyectos_continuidad.odt",
    "06-anexo-V-presupuesto.pdf": f"{BASE}/otros/anexo_V_presupuesto_justificacion.pdf",
    "07-anexo-VI-compromiso-centros-colaboradores.pdf": f"{BASE}/otros/anexo_VI_compromiso_centros.pdf",
    "08-anexo-VII-compromiso-empresas.pdf": f"{BASE}/otros/anexo_VII_compromiso_participacion_colaboracion_empresas-_entidades.pdf",
    "09-anexo-VIII-memoria-justificativa.odt": f"{BASE}/otros/anexo_VIII_memoria_justificativa.odt",
    "10-anexo-IX-criterios-valoracion.pdf": f"{BASE}/otros/anexo_IX_criterios_valoracion.pdf",
    "11-anexo-X-renuncia.pdf": f"{BASE}/otros/anexo_X_renuncia.pdf",
    "12-anexo-XI-certificado-profesorado.pdf": f"{BASE}/otros/anexo_XI_certificado-_participacion_profesorado.pdf",
    "13-anexo-XII-certificado-alumnado.pdf": f"{BASE}/otros/anexo_XII_certificado_participacion_alumnado.pdf",
}

HEADERS = {
    # Algunos servidores del Gobierno de Canarias rechazan peticiones sin
    # cabecera de navegador; simulamos una para evitar bloqueos.
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
}


def descargar(nombre, url):
    destino = os.path.join(CARPETA_DESTINO, nombre)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as respuesta, open(destino, "wb") as f:
            f.write(respuesta.read())
        tamano_kb = os.path.getsize(destino) / 1024
        print(f"  OK  {nombre}  ({tamano_kb:.0f} KB)")
        return True
    except urllib.error.HTTPError as e:
        print(f"  ERROR {nombre}: HTTP {e.code}")
    except urllib.error.URLError as e:
        print(f"  ERROR {nombre}: {e.reason}")
    except Exception as e:
        print(f"  ERROR {nombre}: {e}")
    return False


def main():
    print("Descarga de documentos oficiales - Proyectos de Innovación FP Canarias")
    print(f"Carpeta destino: {CARPETA_DESTINO}\n")
    os.makedirs(CARPETA_DESTINO, exist_ok=True)

    ok, fallidos = 0, []
    for nombre, url in DOCUMENTOS.items():
        if descargar(nombre, url):
            ok += 1
        else:
            fallidos.append(nombre)

    print(f"\nCompletado: {ok}/{len(DOCUMENTOS)} documentos descargados.")
    if fallidos:
        print("\nNo se pudieron descargar (revisa tu conexión o si la URL cambió):")
        for f in fallidos:
            print(f"  - {f}")
        print("\nPuedes descargarlos manualmente desde:")
        print("https://www.gobiernodecanarias.org/educacion/web/formacion_profesional/"
              "programas_proyectos/proyectos_innovacion/index.html")
        sys.exit(1)


if __name__ == "__main__":
    main()
