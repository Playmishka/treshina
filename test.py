from ultralytics import YOLO

model = YOLO("model/best.pt")

result = model.predict(source="images/photo_2023-10-24_17-38-22.jpg", stream=False,
											save=True, conf=0.1, project="images", name="Hello")

