<h1>Computer Vision FX</h1>
<p align="center">Este es un <b>proyecto personal</b> que aplica detección de objetos con YOLOv8 sobre videos para crear un efecto estético de visión por computadora. <br>
El objetivo es más enfocado a la estética y lo creativo que de análisis de datos: resalta objetos en el video con cuadros y etiquetas</p>
<pre>
<code>
Computer-Vision-Effect/
│── src/
│   └── main.py
│── videos/
│── videos_detected/
│── yolov8n.pt
│── README.md
│── requirements.txt
</code>
</pre>
<ul>
    <li><b>main.py</b> ---- código principal</li>
    <li><b>videos</b> ---- carpeta para tus videos de entrada</li>
    <li><b>videos_detected</b> ---- carpeta donde se guardan los videos procesados</li>
    <li><b>yolov8n.pt</b> ---- modelo YOLOv8 (peso pre-entrenado)</li>
    <li><b>README.md</b> ---- este archivo</li>
    <li><b>requirements.txt</b> ---- dependencias de Python</li>
</ul>

<h2>Cómo usarlo (version 1: para VS Code)</h2>
<ol>
    <li><b>Colocar tu video en la carpeta</b> <code>videos/</code>
    <ul>
        <li>Solo permite un video por ejecución</li>
        <li>Formatos comunes: <code>.mp4</code>, <code>.mov</code>, etc...</li>
    </ul>
    </li>
    <li><b>Abrir </b><code>main.py</code><b> en VS Code</b> 
    <ul>
        <li>Cambiar el nombre del video de entrada en esta línea</li>
        <pre>
        <code>input_filename = "tu_video.mp4" # <- CAMBIAR ESTO</code>
        </pre>
    </ul>
    </li>
    <li><b>Ejecutar el script</b>
    <ul>
        <li>Ejecutar directamente desde VS Code</li>
        <li>El script procesará el video, mostrando el efecto en pantalla</li>
    </ul>
    </li>
    <li><b>Revisar el resultado</b>
    <ul>
        <li>El video procesado se guarda automáticamente en la carpeta <code>videos_detected/</code></li>
        <li>El nombre será el mismo del video de entrada, con <code>_detected</code> agregado</li>
        <li>Si ya existe un archivo con ese nombre, se agregará (2), (3), etc... automáticamente</li>
    </ul>
    </li>
</ol>


<h2>Características</h2>
<ul>
    <li>Uso de <b>YOLOv8</b> para detección de objetos en cada frame del video</li>
    <li>Ventana redimensionable para visualizar el proceso en tiempo real</li>
    <li>Barra de progreso para seguir cuánto falta del video</li>
    <li>Output automático con nombre seguro (no sobreescribe archivos)</li>
</ul>


<h2>Requisitos</h2>
<ul>
    <li>Python 3.10 +</li>
    <li>Paquetes (instalables con pip): 
    <pre>
    <code>pip install -r requirements.txt</code>
    </pre>
    </li>
    <li><code>requirements.txt</code> sugerido:
    <pre>
    <code>
    ultralytics
    opencv-python
    tqdm
    </code>
    </pre>
    </li>
</ul>

<h2>Próximas versiones</h2>
<p>Versión 2 : correr el script desde terminal/powershell usando parámetros <code>--input</code> y <code>--output</code>, sin tocar el código</p>

<h2>Tips para principiantes</h2>
<p>Para la gente que no está muy familiarizada con programación o python, con este repositorio tiene las siguientes ventajas:</p>
<ul>
    <li>No necesitas cambiar rutas de carpetas</li>
    <li>Solo cambia el nombre del video en <code>input_filename</code></li>
</ul>