import pandas as pd
from readvocxml import readvocxml
from bbox_or_txt import get_bbox_txt
import os
import numpy as np


def getvoccsv(xml_dir, csv_save_dir, txt_save_dir, image_dir):
    """
    得到csv和txt文件，并返回数据集样本数
    """
    col = ['filename', 'path', 'depth', 'height', 'width', 'object_txt_path']
    array = []

    for xml_name in os.listdir(xml_dir):
        xml_path = xml_dir + '/' + xml_name
        [filename, path, depth, height, width, objectinfo] = readvocxml(xml_path, image_dir=image_dir)
        object_txt_path = get_bbox_txt(filename[:-4], objectinfo, txt_save_dir)
        arr = [filename, path, depth, height, width, object_txt_path]
        array.append(arr)
    array = np.array(array)
    df = pd.DataFrame(array, columns=col)
    df.to_csv(csv_save_dir + '/' + 'object.csv', encoding='utf-8')