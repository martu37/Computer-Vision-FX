import cv2
from ultralytics import YOLO
from tqdm import tqdm
import os

# Carpeta de input y output
input_folder = "videos"
output_folder = "videos_detected"
os.makedirs(output_folder, exist_ok=True)

# Nombre del video de entrada (el usuario solo cambia esto)
input_filename = "walking_crowd.mp4"  #          <-- CAMBIAR ESTO

# Rutas completas
input_path = os.path.join(input_folder, input_filename)
base_name, ext = os.path.splitext(input_filename)
output_filename = f"{base_name}_detected{ext}"
output_path = os.path.join(output_folder, output_filename)

# Evitar sobreescribir archivos existentes
counter = 1
while os.path.exists(output_path):
    output_filename = f"{base_name}_detected({counter}){ext}"
    output_path = os.path.join(output_folder, output_filename)
    counter += 1

# Cargar modelo YOLO
model = YOLO("yolov8n.pt")

# Abrir video
cap = cv2.VideoCapture(input_path)
if not cap.isOpened():
    print(f"No se pudo abrir el video: {input_path}")
    exit()

# Configuración de ventana
cv2.namedWindow("YOLO Detection", cv2.WINDOW_NORMAL)
cv2.resizeWindow("YOLO Detection", 800, 600)

# Info del video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# VideoWriter
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Procesar frames
with tqdm(total=total_frames, desc="Procesando video", unit="frame") as pbar:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        annotated_frame = results[0].plot(line_width=2, font_size=12, labels=True, conf=True)
        out.write(annotated_frame)
        cv2.imshow("YOLO Detection", annotated_frame)
        pbar.update(1)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
out.release()
cv2.destroyAllWindows()
print(f"\n✅ Video guardado en: {output_path}")
