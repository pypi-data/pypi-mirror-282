import os
import cv2
from tqdm import tqdm
from segment_and_count import ObjectCounter


def main(img_folder = 'data/test', output_object = 'object_detected', output_planks = 'oplanks_detected'):
    os.makedirs(os.path.join(img_folder, output_object), exist_ok=True)
    os.makedirs(os.path.join(img_folder, output_planks), exist_ok=True)

    all_imgs = [file for file in os.listdir(img_folder) if file.split('.')[-1] in ['jpg', 'png']]
    counter = ObjectCounter()

    for img_file in tqdm(all_imgs):
        path_read = os.path.join(img_folder, img_file)
        path_save = os.path.join(img_folder, output_object, img_file) + '.output_object.jpg'

        img = cv2.imread(path_read)
        obj = counter.detect_object(img)
        cv2.imwrite(path_save, obj)

        print(counter.count_planks(obj))


if __name__ == '__main__':
    main()