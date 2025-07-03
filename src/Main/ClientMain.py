import threading
import time

import cv2
import numpy
import supervision as sv
import yaml

from Client.InferenceCaller import InferenceCaller

# from Client.PPP.YoloSegmentationPPP import YoloSegmentationPPP
from Client.PPP.YoloDetectionPPP import YoloDetectionPPP

# from Client.PPP.YoloPPP import YoloPPP
from Client.PPP.YoloPPPALL import YoloPPP
from Common import ConfigReader


def main():

    interactor = InferenceCaller()

    # coco_config_path = ConfigReader.ConfigReader().read_str(
    #     "device_paths", "COCO_CONFIG_PATH"
    # )
    # classes = yaml.safe_load(open(coco_config_path))["names"]
    classes = {
        0: "fire",
        1: "default",
        2: "smoke",
    }

    # yolo_segmentation_ppp = YoloDetectionPPP(640, 640, classes)
    yolo_segmentation_ppp = YoloPPP(640, 640)

    # Pre-process
    orig_image = cv2.imread("./Client/test/fire.jpg")
    # preprocess_dict = yolo_segmentation_ppp.preprocess(orig_image)
    # pre_image: numpy.ndarray = preprocess_dict["preprocessed_image"]
    pre_image = yolo_segmentation_ppp.preprocess(orig_image)

    model_list = [
        "yolo11n",
    ]
    thr_list = []
    for idx in range(1):
        thr = threading.Thread(
            target=do_inference,
            args=(
                interactor,
                yolo_segmentation_ppp,
                pre_image,
                orig_image,
                model_list[idx % len(model_list)],
                classes,
            ),
        )
        thr_list.append(thr)

    start = time.perf_counter_ns()
    for thr in thr_list:
        thr.start()

    for thr in thr_list:
        thr.join()
    end = time.perf_counter_ns()

    print("Total Inference Time >>> ", (end - start) / 1e9)


def do_inference(
    inference_caller: InferenceCaller,
    yolo_segmentation_ppp: YoloPPP,
    pre_image,
    orig_image,
    model_name,
    classes,
):
    output, request_idx = inference_caller.call_inference(
        model_name, {"images": pre_image}
    )

    output0 = output["output0"]
    # output1 = output["output1"]

    # post_image = yolo_segmentation_ppp.postprocess(
    #     orig_image,
    #     output0,
    #     0.5,
    #     0.5,
    #     ratio=preprocess_dict["ratio"],
    #     pad_w=preprocess_dict["pad_w"],
    #     pad_h=preprocess_dict["pad_h"],
    #     nm=32,
    # )

    # Post-process
    bboxes, masks, _ = yolo_segmentation_ppp.postprocess(
        orig_image,
        predictions=output0,
        prototypes=None,  # if seg output1
        score_thr=0.1,
        iou_thr=0.1,
        num_classes=len(classes),  # 80 for COCO
    )

    if bboxes is not None:

        detections = sv.Detections(
            xyxy=bboxes[:, :4],
            mask=masks,
            confidence=bboxes[:, 4],
            class_id=bboxes[:, 5].astype(int),
        )

        # mask_annotator = sv.MaskAnnotator()

        # Applica le annotazioni a un'immagine
        # annotated_image = mask_annotator.annotate(
        #     scene=orig_image,  # la tua immagine (array NumPy)
        #     detections=detections,  # le detections da disegnare
        # )

        labels = [
            f"{classes[class_id]} {confidence:.2f}"
            for class_id, confidence in zip(detections.class_id, detections.confidence)
        ]

        box_annotator = sv.BoxAnnotator()

        # Applica le annotazioni a un'immagine
        annotated_image = box_annotator.annotate(
            scene=orig_image,  # la tua immagine (array NumPy)
            detections=detections,  # le detections da disegnare
        )

        label_annotator = sv.LabelAnnotator()

        # Applica le annotazioni a un'immagine
        annotated_image = label_annotator.annotate(
            scene=orig_image,  # la tua immagine (array NumPy)
            detections=detections,  # le detections da disegnare
            labels=labels,
        )

        cv2.imwrite("./Client/test/Test_Image_Out.jpg", annotated_image)
        # print(f"Request {request_idx} done, saving image...")
        # cv2.imwrite(f"./Client/test/Test_Image_Out_{request_idx}.jpg", post_image)
    else:
        print(f"Request {request_idx} returned no detections.")


if __name__ == "__main__":
    main()
