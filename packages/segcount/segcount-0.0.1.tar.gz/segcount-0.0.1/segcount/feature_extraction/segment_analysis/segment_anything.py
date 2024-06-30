import os
import cv2

from cconfig import SAMModelCfg
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry


class SegmentAnything:
    def __init__(self, model_type, device = SAMModelCfg.device) -> None:
        self.validate_model_type(model_type)
        model_info = SAMModelCfg.model_info
        model_type_info = model_info[model_type]

        checkpoint = self.get_checkpoint_model(model_type_info)
        self.sam = sam_model_registry[model_type](checkpoint=checkpoint)
        self.sam.to(device=device)
        self.mask_generator = SamAutomaticMaskGenerator(self.sam)
        self.img_resolution = model_type_info['img_resolution']
        pass


    def get_checkpoint_model(self, model_type_info):
        model_path = model_type_info['model_path']
        if not os.path.exists(model_path):
            model_url = model_type_info['model_url']
            self.download_checkpoint(model_url, model_path)

        return model_path


    def validate_model_type(self, model_type):
        if model_type not in SAMModelCfg.valid_model_type:
            raise Exception(f'Model type of SAM is invalid. Please use {SAMModelCfg.valid_model_type}')


    def download_checkpoint(self, model_url, model_path):
        import requests
        print(f'Checkpoint SAM downloading...')
        response = requests.get(model_url)
        if response.status_code != 200:
            raise Exception(f"Failed to download file. HTTP status code: {response.status_code}")

        with open(model_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully and saved to {model_url}")


    def get_scale_dim(self, image):
        height, width, _ = image.shape

        if height > width:
            new_height = self.img_resolution
            new_width = int((self.img_resolution / height) * width)
        else:
            new_width = self.img_resolution
            new_height = int((self.img_resolution / width) * height)
        return new_height, new_width


    def preprocess_image(self, image):
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return img


    def draw_bboxes(self, image, anns):
        if len(anns) == 0:
            return

        bboxes = [ann['bbox'] for ann in anns]
        for i, bbox in enumerate(bboxes):
            x, y, w, h =  bbox
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

            text = str(i + 1)
            text_size, _ = cv2.getTextSize(str(text), cv2.FONT_HERSHEY_SIMPLEX, 0.9, 2)

            text_width, text_height = text_size
            text_x = x + (w - text_width) // 2
            text_y = y + (h + text_height) // 2
            cv2.putText(image, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        return image


    def get_masks(self, img):
        img = self.preprocess_image(image=img)
        masks = self.mask_generator.generate(img)
        return masks


    def count_masks(self, masks, img=None, get_result=False):
        pass