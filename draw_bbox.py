import matplotlib.pyplot as plt


def drawbbox(img, bboxes, grid_num=None, bbox_color='r', bbox_linewidth=5, content_color='red', fig_save_path=None,
             font_size=16, mode=1):
    """
    ---bbox---

    (left,upper)         (right,upper)
        ----------------------
        |                    |
        |       bbox         |
        |                    |
        ----------------------
        (left,lower)         (right,lower)
    Arg:
        img: a PIL object.

        bbox:a 2D int list
            [
                row1:[label_1,xmin_1,ymin_1,xmax_1,ymax_1]
                row2:[label_2,xmin_2,ymin_2,xmax_2,ymax_2]
                ....
                row_i[label_i,xmin_i,ymin_i,xmax_i,ymax_i]
            ]

        [xmin,ymin,xmax,ymax] is equal to [left,upper,right,lower].

        bbox_color:a str.It's bbox's bounding color.
        eg:
            'r' :red
            'b':blue
            'w':white
            'y':yellow
            'g':green

        content_color:content font's color.

        bbox_info:bounding box's some infomation that you want to display.

        fig_save_path:image with bbox displayed's saved path.

        font_size:content's font size.

    """
    h, w = img.height, img.width
    fig = plt.figure(figsize=(6, 6))
    axis = fig.gca()  # get figure's axis
    if len(bboxes[0]) == 5:
        for bbox in bboxes:
            if mode == 1:
                bboxer = plt.Rectangle(bbox[1:3], bbox[3] - bbox[1], bbox[4] - bbox[2], linewidth=bbox_linewidth,
                                       edgecolor=bbox_color, facecolor='none')
            if mode == 2:
                bboxer = plt.Rectangle((int(bbox[1] - bbox[3] / 2), int(bbox[2] - bbox[4] / 2)), bbox[3], bbox[4],
                                       linewidth=bbox_linewidth, edgecolor=bbox_color, facecolor='none')
            axis.add_patch(bboxer)
    elif len(bboxes[0]) == 4:
        for bbox in bboxes:
            if mode == 1:
                bboxer = plt.Rectangle(bbox[0:2], bbox[2] - bbox[0], bbox[3] - bbox[1], linewidth=bbox_linewidth,
                                       edgecolor=bbox_color, facecolor='none')
            if mode == 2:
                bboxer = plt.Rectangle((int(bbox[0] - bbox[2] / 2), int(bbox[1] - bbox[3] / 2)), bbox[2], bbox[3],
                                       linewidth=bbox_linewidth, edgecolor=bbox_color, facecolor='none')
            axis.add_patch(bboxer)
    plt.imshow(img)
    if grid_num:
        grid_width = (int(h / grid_num[0]), int(w / grid_num[1]))
        x = 0
        y = 0
        for i in range(grid_num[0] + 1):
            bboxer1 = plt.Rectangle((x, y + i * grid_width[0]), w, 5, linewidth=2, edgecolor='black', facecolor='black')
            axis.add_patch(bboxer1)
        x = 0
        y = 0
        for j in range(grid_num[1] + 1):
            bboxer1 = plt.Rectangle((x + j * grid_width[1], y), 5, h, linewidth=2, edgecolor='black', facecolor='black')
            axis.add_patch(bboxer1)
    if fig_save_path:
        plt.savefig(fig_save_path, bbox_inches='tight', pad_inches=0.0)