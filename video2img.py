import cv2


def video2img(videopath,output_dir,img_num=50):
    """
    :param videopath: mp4 video's path.
    """
    cap = cv2.VideoCapture(videopath)
    # 计数
    i = 0
    # 循环判断视频是否打开
    while cap.isOpened():
        # 逐帧读取视频，读取到时ret的返回值为true，当返回false时表示视频结束，frame为矩阵；
        ret, frame = cap.read()
        # i=50 指定截取50张图片
        if i == img_num:
            break
        else:
            i = i + 1
            # 图片命名+保存路径
            filename = "src" + str(i) + ".jpg"
            # result文件夹必须存在才能实现保存，{}是分解出的所有图片的集合
            # 保存图片
            # format方法使路径格式化
            cv2.imwrite(output_dir+'/'+"{}".format(i), frame)
    # 释放资源
    cap.release()
    cv2.destroyAllWindows()

