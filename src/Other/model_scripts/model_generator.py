import gc
import os
import shutil
from tabnanny import verbose

from ultralytics import YOLO


def download_and_export(model_names: list[str]):
    for mod_name in model_names:
        try:
            model = YOLO(mod_name)
            model.train(
                data="../datasets/fire_dataset_yolov8/data.yaml",
                epochs=50,
                imgsz=160,
                batch=16,  # Reduced batch size for CPU
                device="cpu",  # Use CPU (AMD GPU not supported with CUDA PyTorch)
                workers=8,  # Use multiple CPU cores for data loading
                cache=True,  # Cache images for faster loading
                amp=False,  # Disable AMP on CPU (not supported)
            )
            export_path = model.export(format="onnx", imgsz=640)
            mod_name = mod_name.replace(".pt", "")
            shutil.move(export_path, "../models/" + mod_name + ".onnx")
            os.remove("./" + mod_name + ".pt")

            del model
            gc.collect()
            print(f"✅ Model {mod_name} exported successfully.")
        except Exception as e:
            print(f"❌ Error exporting model {mod_name}: {e}")
            continue


def main():
    seg_models = [
        "yolo11n-seg.pt",
        # "yolo11s-seg.pt",
        # # "yolo11m-seg.pt",
        # "yolo11l-seg.pt",
        # "yolo11x-seg.pt",
    ]
    det_models = [
        "yolo11n.pt",
        # "yolo11s.pt", "yolo11l.pt", "yolo11x.pt"
    ]

    cls_models = [
        "yolo11n-cls.pt",
        "yolo11s-cls.pt",
        "yolo11l-cls.pt",
        "yolo11x-cls.pt",
    ]
    # download_and_export(seg_models)
    download_and_export(det_models)
    # download_and_export(cls_models)


if __name__ == "__main__":
    main()
