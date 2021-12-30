# BMT使用手册  

[TOC]



***

## 一、声明  

1. 该界面设计为中山大学《Python数据分析》教学班（2021.09-2022.01）-A301/A305-（9-10）/（7-8) 所制作的课程期末作业。  
2. 选择制作该GUI用户界面的原因是学习本课程后想利用所学知识应用到实际生活中，以期末作业为契机系统梳理python基础语法、图形交互、数据分析、可视化等知识点。
3. 该界面设计为智能书店系统用户注册和登录界面。
4. 本项目由中山大学研究生胡心亭、胡琰、李晋、李松璋（拼音字母排序，四人贡献值均等）共同完成，部分内容参考网络上的学习资源，如有侵权请在讨论区进行说明，作者将视情况进行删除修改。

***

## 二、使用说明  

1. 界面逻辑  

   ![image-20211229221820580](C:\Users\huyan35\AppData\Roaming\Typora\typora-user-images\image-20211229221820580.png)

2. 该GUI界面可用于智能书店系统用户注册和登录，注册完成之后将用户信息写入数据库，登录时用数据库查询是否有此用户、密码是否正确完成登录动作；通过数据库查询是否为管理员、是否为书店、是否为仓库端并最终确认是用户；普通用户主页面和普通网页无异，可检索、购买书籍，并用数据库保存用户的购买信息，分析其购买行为构建普通用户画像在主页面生成专属推荐。  

3. 该GUI界面设有管理员主页面，可用于对所有用户进行操作如添加、删除、查询和更新用户信息。  

4. 该GUI界面设有书店端主页面，可看到实时销量、利润统计的可视化图，每月还可以实时更新销售量前十和销售量后十作为首页推荐和特价书籍。  

5. 该GUI界面设有仓库端主页面，可生成库存清单包括书目类别、名称、进价、售价和库存量，可实时更新书籍进价和售价，以及在库存量低于100本时自动警告书店端并生成书籍采购清单。  

6. 本GUI界面应在 Python3 环境下运行，需要下载与主体程序相关的模块，仅下载主体程序无法正常运行，已在 PyCharm 和 Anaconda3 环境下成功运行。   

***

## 三、模块说明

### 1. log_in.py  

该模块负责用户登录，以及与其他窗口的联系，必须在用户名存在以及输入密码正确方可登陆成功，使用时应注意安装 PyQt5 模块，使用 pip 安装，在 PyCharm 配置 Qt Designer、pyuic、pyrcc工具。  

### 2. register_to.py  

该模块负责用户注册，注册时必须两次输入的密码相同并且用户名不存在方可注册成功，否则提示“用户已经存在”。  

### 3. register_success.py  

该模块主要提示新用户注册成功，以及与其他窗口的联系。  

### 4. Admin.py  

该模块负责管理员对所有用户信息的操作，包括添加、删除、查询和更新用户，只有用户名为 admin 才能进入管理员窗口，即管理员的账号一定为 admin，数据库中必含有 admin 用户名，如果该用户名被删除，会自动生成默认的 admin 及默认密码 admin123。  
管理员主页面可查询到用户名、密码及注册时间。删除用户时，需要勾选前面的选择框，然后点击 Delete，Select All 可方便一次性选择全部用户，点击之后变成 Unselect，可勾选不作操作的用户，再次点击 Unselect 可不选择任何用户；Clear 可一次性删除全部用户，包括 admin，但之后会自动生成 admin 及设置好默认密码 admin123；Refresh 可以更新表格，将数据库中的数据重新添加到表格中。

### 5. shop_windows.py  

该模块负责实时记录书籍销量、销售额和利润以及今日销售额、累计销售额、今日支出、累计支出、今日利润和累计利润的可视化图表，点击“从”和“到”可自主选择日期并查看该期间的销售和利润统计，也可刷新返回最初的页面或重新自主选择日期。 

### 6. storehouse_windows.py  

### 7. main_windows.py  

该模块负责用户检索、浏览、购买书籍并生成购买记录，以及与其他窗口的联系。  

### 8. books_info_to_db.py  

该模块负责把所有书籍信息转换成数据库文件，方便计算机处理。具体操作是利用 pandas 读取 books_info.csv 文件并创建 DataFrame，通过 sqlite3 内置模块连接数据库 books_info.db 并使用 append 方式添加书籍信息。  

### 9. resource_rc.py  

该模块负责把书籍图片文件转换成二进制数据，方便计算机保存和读取图片。  

### 10. Account_Database.py  

该模块是数据库模块，负责为操作数据提供更简易操作的接口，可实现插入数据、获取数据、更新数据，以用户名查找密码、以用户名删除数据，判断数据库中是否有用户名信息，清空所有数据等功能。

### 11. BMT_client.py  

该模块是未登录或用户登录后所看到的主页面，与网页登录页面无异，可常规操作，需要调用上述 log_in、register_to、register_success、main_windows、shop_windows 模块。  
注册时必须两次输入的密码相同并且用户名不存在方可注册成功，否则提示“用户已经存在”；如果用户名只有一个字符且两次输入的密码不为空，提示“用户名太短，请输入至少2个字符”；如果只输入一个密码或密码确认框为空时，提示“密码为空”；如果用户名符合要求且两次密码都少于6位，提示“密码少于六位，请重新输入”；如果用户名符合要求但两次输入密码不一致，提示“两次输入的密码不一致，请确认后重新输入”。注册完成后，提示“注册成功”，自动跳转到注册成功页面，返回用户注册成功可以去登录的页面。
只有输入已注册过的用户名和密码才能成功登录，并提示“欢迎加入 BMT：XX”，如果是管理员则进入管理员主页面，如果是书店用户则进入书店端主页面，如果是普通用户则进入个人主页，一旦输入错误密码或者输入没有注册的用户名等，则登录失败。  
用户未登录时，“注销”、“购买记录”、“购买”、“专属推荐”按钮无法击。  
点击“使用手册”可自动跳转到网页版 READEM.md，点击书籍类别可在下方显示相关书籍信息，并实时根据近期销量高低排序。  
实时更新销售量前十和销售量后十作为首页推荐和特价书籍，根据普通用户最多购买类型生成专属推荐。  

***

## 四、致谢  

感谢授课教师王佳琪老师对本项目提供的项目结构分析和技术支持！

