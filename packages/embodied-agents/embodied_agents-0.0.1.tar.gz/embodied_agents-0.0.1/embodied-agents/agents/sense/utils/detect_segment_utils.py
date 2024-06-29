import random
from dataclasses import dataclass
from typing import Dict, List, Tuple, Union

import cv2
import matplotlib.pyplot as plt
import numpy as np
import torch
from PIL import Image


@dataclass
class BoundingBox:
    """
    A class to represent a bounding box with coordinates.

    Attributes:
        xmin (int): The minimum x-coordinate of the bounding box.
        ymin (int): The minimum y-coordinate of the bounding box.
        xmax (int): The maximum x-coordinate of the bounding box.
        ymax (int): The maximum y-coordinate of the bounding box.
    """

    xmin: int
    ymin: int
    xmax: int
    ymax: int

    @property
    def xyxy(self) -> List[float]:
        """Return the bounding box coordinates as a list."""
        return [self.xmin, self.ymin, self.xmax, self.ymax]


@dataclass
class DetectionResult:
    """
    A class to represent a detection result.

    Attributes:
        score (float): The confidence score of the detection.
        label (str): The label of the detected object.
        box (BoundingBox): The bounding box of the detected object.
        mask (np.array, optional): The segmentation mask of the detected object.
        centroid (Tuple[int, int], optional): The centroid of the detected object.
    """

    score: float
    label: str
    box: BoundingBox
    mask: np.array = None
    centroid: Tuple[int, int] = None

    @classmethod
    def from_dict(cls, detection_dict: Dict) -> "DetectionResult":
        """Create a DetectionResult instance from a dictionary."""
        return cls(
            score=detection_dict["score"],
            label=detection_dict["label"],
            box=BoundingBox(
                xmin=detection_dict["box"]["xmin"],
                ymin=detection_dict["box"]["ymin"],
                xmax=detection_dict["box"]["xmax"],
                ymax=detection_dict["box"]["ymax"],
            ),
        )

    # Placeholder for future implementation of from_yolo_result
    # @classmethod
    # def from_yolo_result(cls, yolo_result: Dict) -> "DetectionResult":
    #     return cls(
    #         score=yolo_result.conf,
    #         box=BoundingBox(
    #             xmin=yolo_result.boxes.xyxy[0],
    #             ymin=yolo_result.boxes.xyxy[1],
    #             xmax=yolo_result.boxes.xyxy[2],
    #             ymax=yolo_result.boxes.xyxy[3],
    #         ),
    #     )


def calculate_centroid(mask: np.ndarray) -> Tuple[int, int]:
    """
    Calculate the centroid of a binary mask.

    Args:
        mask (np.ndarray): Binary mask.

    Returns:
        Tuple[int, int]: Coordinates of the centroid.
    """
    M = cv2.moments(mask)
    if M["m00"] == 0:
        return (0, 0)
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    return (cx, cy)


def annotate(image: Union[Image, np.ndarray], detection_results: List[DetectionResult]) -> np.ndarray:
    """
    Annotate the image with detection results.

    Args:
        image (Union[Image, np.ndarray]): The image to annotate.
        detection_results (List[DetectionResult]): The detection results.

    Returns:
        np.ndarray: The annotated image.
    """
    # Convert PIL Image to OpenCV format
    image_cv2 = np.array(image) if isinstance(image, Image) else image
    image_cv2 = cv2.cvtColor(image_cv2, cv2.COLOR_RGB2BGR)

    # Iterate over detections and add bounding boxes and masks
    for detection in detection_results:
        label = detection.label
        score = detection.score
        box = detection.box
        mask = detection.mask

        # Sample a random color for each detection
        color = np.random.randint(0, 256, size=3)

        # Draw bounding box
        cv2.rectangle(image_cv2, (box.xmin, box.ymin), (box.xmax, box.ymax), color.tolist(), 2)
        cv2.putText(
            image_cv2,
            f"{label}: {score:.2f}",
            (box.xmin, box.ymin - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            color.tolist(),
            2,
        )

        # If mask is available, apply it
        if mask is not None:
            # Convert mask to uint8
            mask_uint8 = (mask * 255).astype(np.uint8)
            contours, _ = cv2.findContours(mask_uint8, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(image_cv2, contours, -1, color.tolist(), 2)

            # Calculate and draw centroid
            centroid = calculate_centroid(mask_uint8)
            cv2.circle(image_cv2, centroid, 5, color.tolist(), -1)
            detection.centroid = centroid

            print(f"Centroid for {label}: {centroid}")

    return cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)


def plot_detections(
    image: Union[Image, np.ndarray], detections: List[DetectionResult], save_name: str = None
) -> None:
    """
    Plot and save detection results on the image.

    Args:
        image (Union[Image, np.ndarray]): The image to plot detections on.
        detections (List[DetectionResult]): The detection results.
        save_name (str, optional): The file name to save the plotted image.
    """
    plt.figure()
    annotated_image = annotate(image, detections)
    plt.imshow(annotated_image)
    plt.axis("off")
    if save_name:
        plt.savefig(save_name, bbox_inches="tight")

    plt.show()
    plt.close()


def random_named_css_colors(num_colors: int) -> List[str]:
    """
    Returns a list of randomly selected named CSS colors.

    Args:
        num_colors (int): Number of random colors to generate.

    Returns:
        list: List of randomly selected named CSS colors.
    """
    # List of named CSS colors
    named_css_colors = [
        "aliceblue",
        "antiquewhite",
        "aqua",
        "aquamarine",
        "azure",
        "beige",
        "bisque",
        "black",
        "blanchedalmond",
        "blue",
        "blueviolet",
        "brown",
        "burlywood",
        "cadetblue",
    ]

    # Sample random named CSS colors
    return random.sample(named_css_colors, min(num_colors, len(named_css_colors)))


def mask_to_polygon(mask: np.ndarray) -> List[List[int]]:
    """
    Convert a binary mask to a polygon.

    Args:
        mask (np.ndarray): Binary mask.

    Returns:
        List[List[int]]: Polygon vertices.
    """
    # Find contours in the binary mask
    contours, _ = cv2.findContours(mask.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the largest area
    largest_contour = max(contours, key=cv2.contourArea)

    # Extract the vertices of the contour
    polygon = largest_contour.reshape(-1, 2).tolist()

    return polygon


def polygon_to_mask(polygon: List[Tuple[int, int]], image_shape: Tuple[int, int]) -> np.ndarray:
    """
    Convert a polygon to a segmentation mask.

    Args:
        polygon (list): List of (x, y) coordinates representing the vertices of the polygon.
        image_shape (tuple): Shape of the image (height, width) for the mask.

    Returns:
        np.ndarray: Segmentation mask with the polygon filled.
    """
    # Create an empty mask
    mask = np.zeros(image_shape, dtype=np.uint8)

    # Convert polygon to an array of points
    pts = np.array(polygon, dtype=np.int32)

    # Fill the polygon with white color (255)
    cv2.fillPoly(mask, [pts], color=(255,))

    return mask


def load_image(image: Union[str, np.ndarray, Image]) -> Image:
    """
    Load an image from a file path, NumPy array, or PIL Image.

    Args:
        image (Union[str, np.ndarray, Image]): The image to load.

    Returns:
        Image: The loaded image.
    """
    if isinstance(image, str):
        return Image.open(image)
    elif isinstance(image, np.ndarray):
        return Image.fromarray(image)
    elif isinstance(image, Image):
        return image
    else:
        raise ValueError("Unsupported image type")


def get_boxes(results: List[DetectionResult]) -> List[List[float]]:
    """
    Extract bounding boxes from detection results.

    Args:
        results (List[DetectionResult]): The detection results.

    Returns:
        List[List[float]]: List of bounding boxes.
    """
    boxes = []
    for result in results:
        xyxy = result.box.xyxy
        boxes.append(xyxy)

    return boxes


def refine_masks(masks: torch.BoolTensor, polygon_refinement: bool = False) -> List[np.ndarray]:
    """
    Refine segmentation masks.

    Args:
        masks (torch.BoolTensor): The masks to refine.
        polygon_refinement (bool): Flag to enable or disable polygon refinement.

    Returns:
        List[np.ndarray]: The refined masks.
    """
    masks = masks.cpu().float()
    masks = masks.permute(0, 2, 3, 1)
    masks = masks.mean(axis=-1)
    masks = (masks > 0).int()
    masks = masks.numpy().astype(np.uint8)
    masks = list(masks)

    if polygon_refinement:
        for idx, mask in enumerate(masks):
            shape = mask.shape
            polygon = mask_to_polygon(mask)
            mask = polygon_to_mask(polygon, shape)
            masks[idx] = mask

    return masks
