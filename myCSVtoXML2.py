#
# Egohandsで自動生成されたcsvをxmlに変換するスクリプト
# 




# -*- coding: utf-8 -*-
import pandas as pd
import xml.etree.ElementTree as et
import os

# 自動にしたので 不使用
input_file = "egohands/_LABELLED_SAMPLES/CARDS_COURTYARD_B_T/CARDS_COURTYARD_B_T_frame_0011.csv"
output_file = "egohands/test/aaa.xml"

def csv2xml(file_input, xmlname):
    # CSV 読込 (なんかヘッダーに各行のヘッダーがないと0列目がキャプションとして無視されるのでcsvで読み込み時に追加する設定)
    df = pd.read_csv(file_input, names=["a", "b", "c", "d", "e", "f", "g", "h"])


    # ルートを作成
    root = et.Element("annotaion") #全てを囲む<annotation>
    # 基本データ 
    folder = et.SubElement(root, "folder")
    filename = et.SubElement(root, 'filename')
    path = et.SubElement(root, 'path')
    size_child = et.SubElement(root, "size")
    width = et.SubElement(size_child, "width") #sizeの中に作成
    height = et.SubElement(size_child, "height")
    segmented = et.SubElement(root, "segmented")

    
    # 行数繰り返し
    #for i in range(len(df)):
    for i, row in df.iterrows():
        # ここのバウンディングボックスの情報(objectで囲む)
        object_child = et.SubElement(root, "object")
        name = et.SubElement(object_child, 'name')
        pose = et.SubElement(object_child, 'pose')
        truncated = et.SubElement(object_child, 'truncated')
        difficult = et.SubElement(object_child, 'difficult')
        # 箱の情報はbndboxで囲む
        budbox_child = et.SubElement(object_child, 'bndbox')
        xmin = et.SubElement(budbox_child, 'xmin')
        ymin = et.SubElement(budbox_child, 'ymin')
        xmax = et.SubElement(budbox_child, 'xmax')
        ymax = et.SubElement(budbox_child, 'ymax')

        # 各要素に値をセットする csvより
        for iCol, column in df.iteritems():

            if iCol == "a":
                folder.text = str("imgs/") # 基本はきまってるので固定
                filename.text = str(row[iCol])
                path.text = str(row[iCol])
                segmented.text = str(0)
                pose = str("Unspecified")
                truncated = str(0)
                difficult = str(0)
            elif iCol == "b":
                width.text = str(row[iCol])
            elif iCol == "c":
                height.text = str(row[iCol])
            elif iCol == "d":
                name.text = str(row[iCol])
            elif iCol == "e":
                xmin.text = str(row[iCol])
            elif iCol == "f":
                ymin.text = str(row[iCol])
            elif iCol == "g":
                xmax.text = str(row[iCol])
            elif iCol == "h":
                ymax.text = str(row[iCol])

    # XMLを出力
    et.ElementTree(root).write("egohands/xml/"+xmlname+".xml", encoding="utf-8")

if __name__ == '__main__':

    #探索したいフォルダ /data
    image_dir = str("egohands/_LABELLED_SAMPLES/")

    for root, dirs, filenames in sorted(os.walk(image_dir)):
        for dir in dirs: #すべてのディレクトリで
            for f in os.listdir(image_dir + dir): # すべてのファイル(＝＝csvで)
                if(f.split(".")[1] == "csv"):
                    csv2xml(image_dir + dir +"/"+ f, f)

   
    #for root, dirs, filenames in os.walk(image_dir):
    #    for dir in dirs: 
    #        for f in filenames: 
    #                if(f.split(".")[1] == "csv"):
    #                    csv2xml(image_dir+f)
    print("SUCESSE!!!!!!!")