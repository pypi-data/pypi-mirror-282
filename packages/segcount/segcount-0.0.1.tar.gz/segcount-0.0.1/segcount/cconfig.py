import os

MODELZOO = 'modelzoo'
SAM_MODELZOO = os.path.join(MODELZOO, 'sam')
os.makedirs(SAM_MODELZOO, exist_ok=True)

class SAMModelCfg:
    model_info = {
        'vit_h': {
            'img_resolution': 1024,
            'model_path': os.path.join(SAM_MODELZOO, 'sam_vit_h.pth'),
            'model_url': 'https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth'
        },
        'vit_l': {
            'img_resolution': 1024,
            'model_path': os.path.join(SAM_MODELZOO, 'sam_vit_l.pth'),
            'model_url': 'https://dl.fbaipublicfiles.com/segment_anything/sam_vit_l_0b3195.pth'
        },
        'vit_b': {
            'img_resolution': 1024,
            'model_path': os.path.join(SAM_MODELZOO, 'sam_vit_b.pth'),
            'model_url': 'https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth'
        }
    }

    valid_model_type = list(model_info.keys())
    device = 'cpu'