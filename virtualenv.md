# 纪录virtualenv的使用方式 以及过程

## pip3 install virtualenv 安装第三方库

### virtualenv environment_name  创建虚拟环境

#### source environment_name/bin/active  激活环境

#### pip install virtualenvwrapper 暂时不知道是干什么用的

#### pip freeze 查看当前环境安装了那些包

# 纪录re库的使用

> . 匹配除了换行符的所有字符 !! 如果有换行符就要注意！更改匹配模式
> ^ 插入字符匹配字符串的开头
> $ 匹配字符串尾或者换行符中的前一个字符
> * 对它前面的正则匹配0-任意多次 ab*可以匹配'a','ab','a....b'
> + 对它前面的正则匹配1-任意多次 ab+会匹配'a后面跟随1个b~任意个b',但他不会匹配a
> ? 对它前面的正则匹配0-1次重复 ab?会匹配'a'或者'ab'
> re.match(^开始 .* 指定字符$结束,指定字符串) , result.group()返回匹配结果字符串,result.span()返回长度

> .* 贪婪匹配 ，.*?非贪婪匹配  意识这里面的区别 ！ 
常见匹配模式有 re.S (匹配所有字符包括换行符，默认不匹配换行符)。
re.A (match all ASICII characters) 
re.I(ignore the letter's type) 
re.L(language reliable)
re.M(mutiple line mode)
re.U(Unicode match)
