from cconfig import SAMModelCfg
from feature_extraction.segment_analysis.segment_anything import SegmentAnything as Segmenter
from feature_extraction.object_detection.background_substraction import BGRemoveObjectDetector as ObjDetector

class ObjectCounter:
    def __init__(self, device = SAMModelCfg.device, sam_model_type = 'vit_h') -> None:
        self.object_detector = ObjDetector()
        self.counter = Segmenter(model_type=sam_model_type, device=device)
        pass


    def detect_object(self, img):
        object_detected = self.object_detector.detect_object(img)
        return object_detected


    def count_planks(self, img):
        return self.counter.get_masks(img)


    def run(self, img):
        object_detected = self.detect_object(img)
        planks_detected = self.count_planks(object_detected)
        return planks_detected