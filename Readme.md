## YOLOv5 数据集准备步骤

### 步骤 1: 创建目录与文件夹

首先，在YOLOv5的根目录下执行以下操作：

1. 创建一个名为 `VOCData` 的文件夹。
2. 在 `VOCData` 文件夹下创建两个子文件夹：`Annotations` 和 `images`。`images` 文件夹用于存放图像文件（格式应为.jpg），而 `Annotations` 文件夹用于存放标注图片后生成的内容，采用XML格式。

### 步骤 2: 划分训练集和验证集

运行 `split_train_val.py` 程序，它将在项目的 `ImagesSets\Main` 文件夹下生成测试集、训练集和验证集。具体的划分情况由代码决定。

### 步骤 3: 将XML格式转换为YOLO TXT格式

运行 `xml_to_yolo.py` 程序，它将把XML格式的标注文件转换为YOLO格式的TXT文件。此步骤会生成 `labels` 文件夹和 `dataSet_path` 文件夹。

- `labels` 文件夹中包含不同图像的标注文件。每个图像对应一个TXT文件，每行包含一个目标的信息，包括 class、x_center、y_center、width 和 height 格式。这种格式即为YOLO TXT格式。
- `dataSet_path` 文件夹包含了三个数据集的TXT文件。

### 步骤 4: 修改参数并运行训练

最后，在 `train.py` 文件中根据具体情况修改参数，然后运行训练脚本。

以上这些步骤将有助于准备YOLOv5所需的数据集以进行训练。

