# 手のデータセットをPascolVOC形式に変換
## mat_to_xml.py
mat -> xmlに変換するスクリプトである
・フォルダ構成
data - train - annotations - xml , mat 
data - train - images 
といった感じでフォルダを構成しておくと自動で変換してくれる

matに変換したいmatファイルを置く，変換した結果はxmlフォルダに格納される
また，対応する画像をimagesフォルダに入れておく




## MySplit.py
作成したデータセットを任意の分割数でテストデータと訓練データに分割し，txtファイルで出力する


## 全体のフォルダ構成
```
.
├── data
│   ├── train 
│   │   ├── annotations
│   │   │   ├── mat
│   │   │   │   ├──file1.mat
│   │   │   │   └── ...
│   │   │   └── xml
│   │   │       ├──file1.xml
│   │   │       └── ...
│   │   ├── labels
│   │   │   ├──file1.txt
│   │   │   └── ...
│   │   └── images
│   │       ├──file1.jpg
│   │       └── ...
│   ├── eval
│   │   └── ...
│   │
│   ├── train_labels.csv
│   ├── eval_labels.csv
│   ├── label_map.pbtxt
│   ├── train.record
│   ├── eval.record
│   ├── train.txt
│   └── eval.txt
│   
└── model
```
_deeptraining_hands
