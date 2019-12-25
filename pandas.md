# <center>Pandas</center>
pandas是数据清洗最著名的一个库了可以说，使用频率相当的高，再次做一次总结。最常用的可能就是用dataframe来整理数据，本次整理的来源于本人的一些使用案例或者是董付国老师编著的《python程序设计基础》或是官方文档<br>
<p align="right">----整体架构借鉴于老师的ipynb文件</p>
<p align="right"> [官方文档](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html) </p>

###  pandas读数据
<br>最简单也最重要的一part
pandas提供了读取和写入主流文件格式的方法，如csv，excel，json,html,HDF5 format,SQL
首先从最重要也最常用的csv文件开始<br>
>CSV(comma-separated value，逗号分隔值)文件格式是一种非常简单的数据存储与分享方式，以纯文本形式存储表格数据（数字和文本）。CSV文件由任意数目的记录组成，记录间以某种换行符分隔；每条记录由字段组成，字段间的分隔符是其它字符或字符串，最常见的是逗号或制表符。通常，所有记录都有完全相同的字段序列，读取csv的语句大概是长这样子的<br>

#### `import pandas as pd` <br>
#### `df=pd.read_csv("filename")#df(whatever you want)暗指DataFrame,因为读出来的对象是dataframe类型`
read_csv一般而言只需要指定需要读的文件信息即可，但是为了其他处理，你也可以对其他默认参数进行修改，一般读不了的文件就需要修改默认参数的值，才能正确读取文件。<br>
下面来扒一下read_csv方法参数的意义
> 基本参数：filepath__or__buffer,sep,delimiter,delim_whitespace.
在介绍参数时，英文部分为指定的参数的数据类型，和默认的参数值。

filepath__or__buffer：str 指的是文件信息，这里可以是在工作目录下的csv文件(如果找不到会报错),也可以是绝对路径下的csv文件，也可以是URL格式(直接访问网络资源，支持主流的数据传输方式)，都是str类型。<br>
sep:指定分隔符,default=",",dtype=str,如果是read_table()的话默认是"\t",可以指定不同类型的分隔符，但是分隔符必须是str类型的。<br>
delimiter:跟sep参数一致，和sep二选一即可<br>
delim_whitespace：default=false，dtype=boolean，如果参数为True,则sep="\s+"
![](read_csv.png)

一些不常见但是有可能会用上的参数，其实算是数据预(预处理)，是比较高级用法，涉及到内存管理，引擎设置等，是为了更加efficient去读一个csv文件，但是绝大多数情况下都不怎么用到(像我就用到过一次),一般都是在读完csv之后对DataFrame对象进行操作，而不是在读的时候就进行操作，我更加推荐前者。

> 非常用参数： header,names,index_col,prefix,dtype,skiprows,skipinitialspace,nrows,na_values,keep_default_na,na_filter,compression等

很多的参数一看名字就知道用法，我就简单介绍，涉及用法较多，更加常用的涉及的篇幅会长一点。
header：dtype=infer or list of ints,default="infer"，不设置列名header=0，列名会自动取文件的第一行，如果想自己设定列名(header=None，columns=[]),如果涉及到multipleindex的话，参数就是list of ints。<br>
names:设置列名，和columns一致。<br>
prefix:dtype=str default=None，当列名不存在时，对列名进行预修改，如'x'to 'x1'	,'x2'.....<br>
dtype:default=None,指定数据类型,可以指定数据类型为dtype=object。<br>
skiprows:dtype=list-like 跳过行,default=None,传入list可以跳过指定行。nrows:dtpye=int,default=None,阅读文件前多少行。<br>
na_values:dtype=scalar,str,list-like,default=None,具体描述见官方文档<br>
na_filter:dtype=boolean,default=True,检测缺失值，如果不想检测设为false，可以提高阅读大型文档的表现
compression : dtype={'infer', 'gzip', 'bz2', 'zip', 'xz', None}, default='infer'自动检测以压缩包为后缀的文件，也可以自己指定，但是压缩包内必须有且仅有一个数据文件。