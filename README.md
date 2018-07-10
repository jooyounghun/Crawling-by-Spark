# SKT-WORKS-INTERNSHIP
___

## About

2018_SKT_WORKS_INTERNSHIP

Crawling_by_Spark

Do Crawling based on Spark Distributed Processing, However, there is no marit to Crawling, but It's not in Bigdata env.

We use the Spark Processing to Crawling. so Manage Our CPU Core resources.

there is a growing demand for information to process large amounts of data[text or image].

## Getting Started
Big data processing for large url data.

## Getting Started

### Spark Crawling Step
* Take Dataset from some Cooperations with SKT
  * using Take a CALL & GET data.
* Preprocessing  image using Mask-RCNN
  * using url labeling -> good or bad detect
  * using divide data into RDD structures in local for Analysis
  * using `Crawling_using_Python.py` split url dataset & Crawl them.
* Parsing HTML tags
  * using BeautifulSoup & Newspapers Package. parsing in local.
* Save CSV file from 1 url data.
* Visualize results
  * None.


###  Spark

![](https://spark.apache.org/images/spark-logo-trademark.png)

We use the Spark Distribute System to extract Performance in Crawling.
And There's second way to crawl, like multiprocessing, queue, etc..




If you want to know more about the above Tool, please refer to the link below.

* [Spark](https://spark.apache.org/)
* [Crawler(https://ko.wikipedia.org/wiki/%EC%9B%B9_%ED%81%AC%EB%A1%A4%EB%9F%AC)
* [Multiprocessing](https://ko.wikipedia.org/wiki/%EB%8B%A4%EC%A4%91_%EC%B2%98%EB%A6%AC)


### Dataset

urllist
* https://www.naver.com/
* https://www.daum.net/
* https://www.google.com/


### Prerequisites
* Spark2.3.1
* Centos version 7
* Tmux
* OpenVPN
* Vim Editor

### spark configuration
* master node with 1 slave nodes
* [ssh, ip configuration](https://github.com/philjjoon/2018-1-GROUP-2/blob/master/configuration/host/hosts)
* hadoop configration
  * [master](https://github.com/philjjoon/2018-1-GROUP-2/tree/master/configuration/hadoop/master)
  * [slave](https://github.com/philjjoon/2018-1-GROUP-2/tree/master/configuration/hadoop/slave)
* spark configuration
  * [master](https://github.com/philjjoon/2018-1-GROUP-2/tree/master/configuration/spark/master)
  * [slave](https://github.com/philjjoon/2018-1-GROUP-2/tree/master/configuration/spark/slave)

### Preprocessing
#### Unzip dataset

you can use unzip script in `processing_script`

```
./unzip
```

#### Train Segmentation

Train a new model starting from ImageNet weights using `train` dataset

```
python3 nucleus.py train --dataset=/path/to/dataset --subset=train --weights=imagenet
```

#### frame_split

Modify it to your location and run it. tiff image is converted to png image.

```
python3 frame_split.py
```

#### Segmentation dataset

```
python3 nucleus.py detect --dataset=/path/to/dataset --subset=stage1_test --weights=<last or /path/to/weights.h5>
```

#### split batch

if you can run above code, you should split image to batch using `preprocessing/split.py`.

```#! /usr/bin/python3
import os
import glob
import shutil
root=os.getcwd()
source=''
target=''
process=os.path.join(root,source)
temp=os.path.join(root,target)
abspath=os.path.abspath("./")
sum_list=os.listdir(process)
sum_list=sorted(sum_list)
for idx,_list in enumerate(sum_list):
    buffer=(round)(idx/1000)
    path=os.path.join(process,_list)
    dest=os.path.join(temp,str(buffer))
    shutil.move(path,dest)
    print(path,"\n",dest,"\nmove complete")
```

_you must modify file target and source folder name in code_

### processing

#### [medianFilter](https://en.wikipedia.org/wiki/Median_filter)

The median filter is a nonlinear digital filtering technique, often used to remove noise from an image or signal. Such noise reduction is a typical pre-processing step to improve the results of later processing (for example, edge detection on an image).

__Image has a noise! So  algorithm does not work well!__

![](https://user-images.githubusercontent.com/22635090/41164680-b3e56238-6b76-11e8-8571-8ed065f7ba73.png)

__After Median_filter__

![](https://user-images.githubusercontent.com/22635090/41164538-61b0d204-6b76-11e8-8fc2-e699483fcf5c.png)

#### csv processing

Perform the csv operation on the following metadata.

![](https://user-images.githubusercontent.com/22635090/41009654-4b96cc22-696d-11e8-8be3-f55140a68f78.png)

You can get an array of these masks, and you can get information about cell ratios and location information.

![](https://user-images.githubusercontent.com/22635090/41009236-b1870d7e-696a-11e8-8fc2-187830d9a92c.png)

![](https://user-images.githubusercontent.com/22635090/41474395-d0c195ea-70f6-11e8-81c7-b04736520785.png)

### Visualize

Visualization is performed by inserting csv data into MYSQL.


The demo has the following MVC pattern.

![](https://user-images.githubusercontent.com/22635090/41474377-ca43db6a-70f6-11e8-8513-5fef6424f7a4.png)

Below is a demo video.

![](https://user-images.githubusercontent.com/22635090/41474210-61c6acd4-70f6-11e8-9a5f-ffe9ddcf43da.gif)


### milestone

![](https://user-images.githubusercontent.com/22635090/41474335-a8d5fe0e-70f6-11e8-821b-940cd098b980.png)
