# 手のデータセットをPascolVOC形式に変換_deeptraining_hands

## mat_to_xml.py
これは mat -> xmlに変換するスクリプトである

data - train - annotations - xml
	     	 	   - mat
	     - images 

といった感じでフォルダを構成しておくと自動で変換してくれる


## MySplit.py
作成したデータセットを任意の分割数でテストデータと訓練データに分割し，txtファイルで出力する

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
See ```howto_tf``` and ```howto_yolo``` for information how to train on yolo or tensorflow
