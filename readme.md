# 目标检测图片模拟效果生成器使用

版本：1.0

环境要求：requirements.txt	python=3.8

适用范围：给定voc格式的标注文件存储格式，输出标注效果图，适用于预览目标检测标注效果。

使用步骤：

- 创建环境后进入环境和当前目录，然后安装依赖库(pip install -r requirements.txt)
- (该步骤可选)创建4个文件夹分别存储csv、dataset、output、txt。当然了，你也可以直接在UI界面指定你的文件位置
- 点击main.exe进入UI界面，填写参数即可。

参数说明：

- csv dir：导入文件信息表存放路径
- txt dir：bounding box信息存放路径
- xml dir：类似于voc datasets的Annotation
- image dir：类似于voc datsets的JPEGImages
- output dir：效果图保存路径

-----

tips：目前版本存在因数据量过大而导致的卡顿现象，请耐心等待
