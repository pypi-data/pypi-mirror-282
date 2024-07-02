from _typeshed import Incomplete
from edgeiq import barcode_detection as barcode_detection, image_classification as image_classification, instance_segmentation as instance_segmentation, object_detection as object_detection, object_tracking as object_tracking, pose_estimation as pose_estimation, qrcode_detection as qrcode_detection, re_identification as re_identification
from edgeiq._production_client import PRODUCTION_CLIENT as PRODUCTION_CLIENT
from typing import Any

POSE_ESTIMATION_RESULT: Incomplete
OBJECT_DETECTION_RESULT: Incomplete
CLASSIFICATION_RESULT: Incomplete
TRACKING_RESULT: Incomplete
BARCODE_RESULT: Incomplete
QRCODE_RESULT: Incomplete
INSTANCE_SEGMENTATION_RESULT: Incomplete
REIDENTIFICATION_RESULT: Incomplete
INVALID_ANALYTICS_FORMAT_MESSAGE: str
CORRUPTED_ANALYTICS_FILE_MESSAGE: str

class CustomEvent:
    def __init__(self, results) -> None: ...
    @property
    def results(self): ...
    @property
    def tag(self): ...

def load_analytics_results(filepath): ...
def parse_analytics_packet(packet): ...
def publish_analytics(results, tag: Any = ...): ...
