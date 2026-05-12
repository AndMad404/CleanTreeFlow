# XML ETL — Service Provider Content Extractor 🗂️ 

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Stable-28a745?style=for-the-badge&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-F7DF1E?style=for-the-badge&logoColor=black)
![Dependencies](https://img.shields.io/badge/Dependencies-Zero-lightgrey?style=for-the-badge)
![Standard Library](https://img.shields.io/badge/Stdlib-xml.etree%20%7C%20time-informational?style=for-the-badge&logo=python&logoColor=white)

> **Herramienta de línea de comandos** que extrae, limpia y muestra los productos anidados dentro de etiquetas de proveedores de servicios en archivos `.content.xml`. Sin dependencias externas. Sin configuración. Solo ejecutar.

---

## Tabla de Contenidos 📋 

- [¿Qué problema resuelve?](#qué-problema-resuelve-)
- [Proceso ETL](#proceso-etl-️)
- [Estructura de Carpetas](#estructura-de-carpetas-)
- [Requisitos](#requisitos-️)
- [Instalación y Uso](#instalación-y-uso-)
- [Tabla de Transformación de Caracteres](#tabla-de-transformación-de-caracteres-)
- [Detalles Técnicos](#detalles-técnicos-)
- [Ejemplo de Salida](#ejemplo-de-salida-)
- [Licencia](#licencia-)

---

## ¿Qué problema resuelve? 🎯 

Los sistemas CMS como **Adobe Experience Manager (AEM)** almacenan el contenido en archivos `.content.xml` donde los nombres de nodos contienen caracteres especiales codificados en formato hexadecimal (por ejemplo, `Mi_x0020_Producto_x0028_2024_x0029_`). Leer estos archivos manualmente es tedioso y propenso a errores.

**XML ETL** automatiza ese proceso en tres pasos:

1. 📥 **Extrae** la jerarquía de nodos desde `service-providers` en el XML
2. 🔄 **Transforma** los códigos hexadecimales a texto legible
3. 🖨️ **Muestra** los resultados formateados en consola, agrupados por proveedor

---

## Proceso ETL ⚙️ 

```
╔══════════════════╦══════════════════════════╦══════════════════════════╗
║  🟡  EXTRACT     ║  🔵  TRANSFORM           ║  🟢  LOAD               ║
╠══════════════════╬══════════════════════════╬══════════════════════════╣
║                  ║                          ║                          ║
║  Parsea el       ║  replace_char() convierte║  Imprime en consola los  ║
║  .content.xml    ║  códigos hex a caracteres║  tags en grupos de 3:    ║
║  con ElementTree ║  legibles:               ║                          ║
║                  ║                          ║  proveedor categoría     ║
║  Navega hasta    ║  _x0020_ → espacio       ║  producto                ║
║  3 niveles desde ║  _x0026_ → &             ║                          ║
║  <service-       ║  _x0028_ → (             ║  Reporta el tiempo de    ║
║  providers>      ║  _x002b_ → +  etc.       ║  ejecución al finalizar  ║
║                  ║                          ║                          ║
╚══════════════════╩══════════════════════════╩══════════════════════════╝
```

### Extract — `ET.parse()` + `get_tags()` 🟡

El script abre y parsea el archivo `.content.xml` usando `xml.etree.ElementTree`. La función `get_tags()` recorre los nodos `service-providers` con bucles anidados y recolecta los tags de los tres sub-niveles de la jerarquía.

### Transform — `replace_char()` 🔵

Cada tag extraído pasa por `replace_char()`, que aplica una lista de reemplazos secuenciales para decodificar los caracteres especiales codificados por el CMS. Los reemplazos cubren espacios, símbolos de puntuación y dígitos del 0 al 9.

### Load — `print()` + `time.perf_counter()` 🟢

Los tags limpios se imprimen en la consola en grupos de 3 elementos por línea (proveedor, categoría, producto) usando `" ".join()`. Al finalizar, el script reporta el tiempo total de ejecución con precisión de microsegundos.

---

## Estructura de Carpetas 📁

```
xml-etl/
│
├── 📄 .content.xml        ← Archivo fuente (debes colocarlo aquí)
├── 🐍 xml_etl.py          ← Script principal
├── 📖 README.md
└── 📜 LICENSE
```

> ⚠️ **Importante:** El archivo `.content.xml` debe estar en la **raíz del proyecto**, en el mismo directorio desde donde se ejecuta el script. Si necesitás apuntar a otra ruta, editá esta línea en `xml_etl.py`:
> ```python
> tree = ET.parse('.content.xml')  # ← Reemplazá por la ruta absoluta o relativa
> ```

---

## Requisitos 🛠️

| Componente | Versión / Detalle |
|---|---|
| **Python** | `3.10` o superior |
| `xml.etree.ElementTree` | Incluida en la librería estándar |
| `time` | Incluida en la librería estándar |
| **Dependencias externas** | ✅ Ninguna — zero `pip install` |

---

## Instalación y Uso 🚀

No hay nada que instalar. Solo necesitás Python y tu archivo XML.

### Paso 1 — Obtené el script

```bash
git clone https://github.com/tu-usuario/xml-etl.git
cd xml-etl
```

### Paso 2 — Colocá tu archivo en la raíz

```bash
cp /ruta/a/tu/.content.xml .
```

### Paso 3 — Ejecutá

```bash
python xml_etl.py
```

### Paso 4 — Revisá la salida en consola

```
Proveedor A  Categoria 1  Producto 001
Proveedor A  Categoria 1  Producto 002
Proveedor B  Categoria 2  Producto 010
...

Elapse time: 0.03 seconds
```

> 💡 **Tip:** Para guardar la salida en un archivo de texto, usá redirección de consola:
> ```bash
> python xml_etl.py > output.txt
> ```

---

## Tabla de Transformación de Caracteres 🔄

La función `replace_char()` decodifica los siguientes 16 códigos hexadecimales. Los reemplazos se aplican **de forma secuencial** sobre el mismo string, por lo que un tag puede contener múltiples códigos y todos serán sustituidos en un solo paso.

| # | Código Hexadecimal | Carácter resultante | Descripción | Ejemplo de transformación |
|---|---|---|---|---|
| 1 | `_x0020_` | ` ` | Espacio en blanco | `Mi_x0020_Producto` → `Mi Producto` |
| 2 | `_x0026_` | `&` | Ampersand | `AT_x0026_T` → `AT&T` |
| 3 | `_x0027_` | `'` | Apóstrofe / comilla simple | `It_x0027_s` → `It's` |
| 4 | `_x0028_` | `(` | Paréntesis de apertura | `Plan_x0028_A_x0029_` → `Plan(A)` |
| 5 | `_x0029_` | `)` | Paréntesis de cierre | `Plan_x0028_A_x0029_` → `Plan(A)` |
| 6 | `_x0030_` | `0` | Dígito 0 | `SKU_x0030_1` → `SKU01` |
| 7 | `_x0031_` | `1` | Dígito 1 | `Tier_x0031_` → `Tier1` |
| 8 | `_x0032_` | `2` | Dígito 2 | `Modelo_x0032_` → `Modelo2` |
| 9 | `_x0033_` | `3` | Dígito 3 | `Pack_x0033_` → `Pack3` |
| 10 | `_x0034_` | `4` | Dígito 4 | `Plan_x0034_G` → `Plan4G` |
| 11 | `_x0035_` | `5` | Dígito 5 | `Plan_x0035_G` → `Plan5G` |
| 12 | `_x0036_` | `6` | Dígito 6 | `Rev_x0036_` → `Rev6` |
| 13 | `_x0037_` | `7` | Dígito 7 | `Code_x0037_` → `Code7` |
| 14 | `_x0038_` | `8` | Dígito 8 | `Line_x0038_` → `Line8` |
| 15 | `_x0039_` | `9` | Dígito 9 | `Zone_x0039_` → `Zone9` |
| 16 | `_x002b_` | `+` | Signo más | `Plan_x0035_G_x002b_` → `Plan5G+` |

> 📝 **Nota:** La codificación `_xHHHH_` es generada automáticamente por AEM y sistemas basados en JCR cuando los nombres de nodo contienen caracteres especiales no permitidos directamente en XML.

---

## Detalles Técnicos 🔬 

### Profundidad de Navegación XML

El script utiliza **4 niveles de bucles anidados** en `get_tags()` para atravesar la estructura del XML:

```
📦 Raíz del XML (.content.xml)
 └── 🏢 <service-providers>                    ← findall() — punto de entrada
      └── 📁 subchild     (Nivel 1)            ← Proveedor de servicio  ✅ tag guardado
           └── 📂 subsubchild    (Nivel 2)     ← Categoría de productos ✅ tag guardado
                └── 🛒 subsubsubchild (Nivel 3)← Producto individual    ✅ tag guardado
```

| Variable | Nivel | Rol en el negocio | ¿Tag recolectado? |
|---|---|---|---|
| `node` | contenedor | Nodo `<service-providers>` | ❌ Solo como punto de entrada |
| `subchild` | 1 | Proveedor de servicio | ✅ `tags.append(subchild.tag)` |
| `subsubchild` | 2 | Categoría de productos | ✅ `tags.append(subsubchild.tag)` |
| `subsubsubchild` | 3 | Producto individual | ✅ `tags.append(subsubsubchild.tag)` |

> 🔍 **Nota sobre el `break`:** El bucle más interno incluye un `break` al final de cada iteración. Esto asegura que se procese únicamente el **primer hijo** de cada nodo `subsubchild`, capturando un tag representativo por categoría y evitando duplicados en la salida.

### Formato de Salida en Consola

Los tags recolectados forman una lista plana que se imprime en triadas:

```python
for i in range(0, len(modified_tags), 3):
    print(" ".join(modified_tags[i:i+3]))
```

Cada línea representa un **triplete** del árbol: `[Proveedor]  [Categoría]  [Producto]`.

### Medición de Rendimiento

El script usa `time.perf_counter()` — el reloj de mayor resolución disponible en Python — para medir el tiempo total de ejecución, incluyendo el parse del XML y todas las transformaciones.

```python
start_time = time.perf_counter()
# ... todo el procesamiento ...
end_time = time.perf_counter()
print(f"\nElapse time: {end_time - start_time:.2f} seconds")
```

### Complejidad Computacional

| Métrica | Valor |
|---|---|
| **Tiempo** | `O(n × r)` — `n` nodos procesados × `r` reemplazos por tag (16 fijos) |
| **Espacio** | `O(t)` — `t` tags recolectados almacenados en lista |
| **I/O** | Una única lectura del archivo XML completo en memoria |

---

## Ejemplo de Salida 📤

Dado un `.content.xml` con proveedores de servicios de telecomunicaciones cuyos nodos están codificados:

**Tags originales en el XML:**
```xml
<service-providers>
  <Proveedor_x0020_A>
    <Internet_x0028_Hogar_x0029_>
      <Plan_x0035_G_x002b_ />
    </Internet_x0028_Hogar_x0029_>
  </Proveedor_x0020_A>
</service-providers>
```

**Salida en consola tras ejecutar el script:**
```
Proveedor A  Internet(Hogar)  Plan5G+

Elapse time: 0.03 seconds
```

---

## Licencia 📜 

Distribuido bajo la licencia **MIT**. Consultá el archivo `LICENSE` para más detalles.

---

<div align="center">

Hecho con 🐍 Python puro &nbsp;·&nbsp; Sin dependencias &nbsp;·&nbsp; Sin complicaciones

</div>
