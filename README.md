# kwic

One project in OO class

-----------

#### 目录

> 由Linux tree命令生成

**kwic**

├── README.md

├── UI

│  ├── Components_py    

│  │  ├── Components.py  （连接UI和业务）

│  │  ├── Help.py         (由help.ui文件转换所得)

│  │  ├── MainWindow.py  (由MainWindow.ui文件转换所得)

│  │  ├── Setting.py        (由setting.ui文件转换所得)

│  │  ├── **__****pycache****__**     （一些运行文件）

│  │  │  ├── Components.cpython-39.pyc

│  │  │  ├── Help.cpython-39.pyc

│  │  │  ├── MainWindow.cpython-39.pyc

│  │  │  └── Setting.cpython-39.pyc

│  │  └── app.py

│  └── ui        (由qtdesigner生成)

│    ├── MainWindow.ui

│    ├── help.ui

│    └── setting.ui

├── modules       （业务类）

│  ├── Line.py

│  ├── LineSearchRule.py

│  ├── LinesSearchRule.py

│  ├── LinesSortRule.py

│  └── Text.py

└── profiles     （一些可能用到的配置文件）

  ├── AppConfig.py

  ├── Untitled Diagram.drawio

  ├── Untitled Diagram.drawio.png

  ├── config.xml

  └── dev.py

------------

#### 进度

-----

2022-02-25   1:45

UI界面基本完成，细节后期完善

- 已实现：

​    	菜单栏基本功能：文件的简单导入、导出和内容展示；

​    	设置界面、帮助界面弹窗展示

- 待实现：

   	 按钮功能：循环移位、排序、搜索；

    设置界面的参数传递；

​    等。

---------

