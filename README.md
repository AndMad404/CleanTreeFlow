XML ETL
XML ETL es una herramienta ligera de línea de comandos diseñada para extraer y decodificar etiquetas anidadas en archivos XML. Su función principal es transformar las convenciones de codificación hexadecimal (comunes en exportaciones de datos de proveedores de servicios) en texto plano legible por humanos.

🚀 Funcionalidades
Extracción Profunda: Procesa estructuras anidadas bajo el nodo service-providers hasta 3 niveles de profundidad.

Decodificador de Caracteres: Convierte automáticamente códigos hexadecimales (como _x0020_, _x0026_, etc.) a sus caracteres correspondientes (espacios, ampersands, paréntesis, etc.).

Salida Optimizada: Muestra los resultados en consola agrupados para facilitar la revisión de productos y categorías.

Monitor de Rendimiento: Incluye un contador de tiempo de ejecución para medir la eficiencia del procesamiento.

🛠️ Requisitos
Versión recomendada de Python: 3.10 o superior.

Versión mínima soportada: Python 3.3+ (debido al uso de time.perf_counter).

Dependencias: Ninguna. Utiliza únicamente la biblioteca estándar de Python (xml.etree.ElementTree).

📋 Preparación del archivo
Para que el script funcione correctamente, el archivo fuente debe:

Llamarse estrictamente .content.xml.

Estar ubicado en la misma carpeta que el script de Python.

Contener una estructura de nodos basada en <service-providers>.

💻 Uso
Coloca tu archivo .content.xml en la raíz del proyecto.

Ejecuta el script desde la terminal:

Bash
python main.py
El script imprimirá en la consola las etiquetas decodificadas y el tiempo total de procesamiento.

⚙️ Cómo funciona el proceso ETL
Extract: El script busca el nodo raíz y navega por la jerarquía service-providers -> subchild -> subsubchild -> subsubsubchild.

Transform: Se aplica la función replace_char para limpiar cualquier residuo de codificación hexadecimal en los nombres de las etiquetas.

Load: Los datos se presentan en la salida estándar (consola) formateados en grupos de tres.

Notas Técnicas
Este script es ideal para entornos de desarrollo web o gestión de contenidos donde los nombres de los componentes o productos vienen "escapados" desde el repositorio de datos original.
