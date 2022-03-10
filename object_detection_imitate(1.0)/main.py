import pandas as pd
import os
from tkinter import *
from xml.dom.minidom import parse
import random
import matplotlib.pyplot as plt
from PIL import Image

#----------------------------------------------------------------------------------------------
def readxml(xml_path):
    tree=parse(xml_path)
    rootnode=tree.documentElement
    objects=rootnode.getElementsByTagName('object')
    objects_info=[]
    for object in objects:
        label=object.getElementsByTagName('name')[0].childNodes[0].data
        xmin=int(object.getElementsByTagName('xmin')[0].childNodes[0].data)
        ymin=int(object.getElementsByTagName('ymin')[0].childNodes[0].data)
        xmax=int(object.getElementsByTagName('xmax')[0].childNodes[0].data)
        ymax=int(object.getElementsByTagName('ymax')[0].childNodes[0].data)
        info=[]
        info.append(label)
        info.append(xmin)
        info.append(ymin)
        info.append(xmax)
        info.append(ymax)
        objects_info.append(info)
    return objects_info

def DrawBBox(image_path,bboxes,bbox_color='r',bbox_linewidth=5,content_color='red',fig_save_path=None,font_size=16):
    """
    Params:
        bbox_info:bounding box's some infomation that you want to display.
    
        bbox:(left,upper,right,lower)
        
        (left,upper)         (right,upper)
        ----------------------
        |                    |
        |       bbox         |
        |                    |
        ----------------------
        (left,lower)         (right,lower)
        
    """
    img=Image.open(image_path)
    fig=plt.figure(figsize=(16.6,12.1))
    axis=fig.gca()  # get figure's axis
    # default:bbox's color is red.
    for bbox in bboxes:
        bboxer=plt.Rectangle(bbox[1:3],bbox[3]-bbox[1],bbox[4]-bbox[2],linewidth=bbox_linewidth,edgecolor=bbox_color,facecolor='none')
        axis.add_patch(bboxer)
        plt.text(bbox[1],bbox[2]-font_size,
                '{}:{}'.format(bbox[0],round(0.9+0.1*random.random(),2))
                ,color=content_color,size=font_size)
        plt.axis('off')
    plt.imshow(img)
    if fig_save_path:
        plt.savefig(fig_save_path,bbox_inches='tight',pad_inches=0.0)
        
def generate(xml_dir,image_dir,output_dir):
    num_image=len(os.listdir(image_dir))
    image_list=os.listdir(image_dir)
    xml_list=os.listdir(xml_dir)
    for i in range(num_image):
        img_path=image_dir+'/'+image_list[i]
        xml_path=xml_dir+'/'+xml_list[i]
        objects_info=readxml(xml_path)
        img_name=image_list[i]
        DrawBBox(img_path,objects_info,fig_save_path=output_dir+'/'+img_name)
    output_tips_label.configure(text="The output is saved into{}.".format(output_dir))
    
#----------------------------------------------------------------------------------------------
root=Tk()

root.title("目标检测标注效果模拟")
root.geometry("300x400")

tipslabel=Label(root,
                text="提示:\n在进行操作前，请保证已详细阅读readme.md.",
                bg='black',
                fg='white',
                justify='left')
tipslabel.place(relx=0,rely=0,relheight=0.1,relwidth=1)


xml_indicate_label=Label(root,
                    text="xml dir:",
                    bg='white',
                    fg='black',
                    justify='left')
xml_indicate_label.place(relx=0,rely=0.2,relwidth=0.3,relheight=0.08)
image_indicate_label=Label(root,
                    text="image dir:",
                    bg='white',
                    fg='black',
                    justify='left')
image_indicate_label.place(relx=0,rely=0.3,relwidth=0.3,relheight=0.08)

output_indicate_label=Label(root,
                    text="output dir:",
                    bg='white',
                    fg='black',
                    justify='left')
output_indicate_label.place(relx=0,rely=0.4,relwidth=0.3,relheight=0.08)

xml_dir_inp=Entry(root)
image_dir_inp=Entry(root)
output_dir_inp=Entry(root)


xml_dir_inp.place(relx=0.3,rely=0.2,relheight=0.08,relwidth=0.4)
image_dir_inp.place(relx=0.3,rely=0.3,relheight=0.08,relwidth=0.4)
output_dir_inp.place(relx=0.3,rely=0.4,relheight=0.08,relwidth=0.4)

button_generate=Button(root,
                    text="生成结果",
                    command=lambda:generate(xml_dir_inp.get(),image_dir_inp.get(),output_dir_inp.get()),
                    )
button_generate.place(relx=0.3,rely=0.6,relheight=0.08,relwidth=0.4)

output_tips_label=Label(root,justify=LEFT,
                        text="")
output_tips_label.place(relx=0,rely=0.7,relheight=0.08,relwidth=0.8)

root.mainloop()