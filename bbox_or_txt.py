import os


def txt_to_bboxinfo(txt_path):
    bbox_info = []
    f = open(txt_path, mode='r', encoding='utf-8')
    content = f.read()
    for info in content.split('\n'):
        info = info.split(' ')
        if len(info) == 1:
            continue
        label = info[0]
        xmin = int(info[1])
        ymin = int(info[2])
        xmax = int(info[3])
        ymax = int(info[4])
        bbox_info.append([label, xmin, ymin, xmax, ymax])
    return bbox_info


def get_bbox_txt(name, bbox_info, txt_save_dir):
    if os.path.exists(txt_save_dir)==0:
        os.makedirs(txt_save_dir)
    f = open('{}/{}.txt'.format(txt_save_dir, name), encoding='utf-8', mode='w')
    for object_info in bbox_info:
        for info in object_info:
            f.write(str(info))
            f.write(' ')
        f.write('\n')
    txt_path = '{}/{}.txt'.format(txt_save_dir, name)
    f.close()

    return txt_path