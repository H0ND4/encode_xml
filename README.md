# 手のデータセットをPascolVOC形式に変換_deeptraining_hands




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
