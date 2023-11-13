import unittest
import datetime

current_datetime = datetime.datetime.now() # 获取当前日期和时间
formatted_datetime = current_datetime.strftime("%Y%m%d_%H%M%S") # 格式化日期和时间为字符串

# 用TestLoader对象的discover方法来自动查找py,自动加载py文件中的方法
# 第一个参数是从哪里找py文件,"."从当前目录开始查找py文件
# 第二个参数是指定py文件的文件名,可以用通配符
suite = unittest.TestLoader().discover("./ANDROID/appeal", "test_recharg_appeal.py")
runner = unittest.TextTestRunner()
file = open(f"./ANDROID/appeal/test{formatted_datetime}.txt", "w", encoding="utf8")
runner = unittest.TextTestRunner(stream=file, verbosity=2)
runner.run(suite)
file.close()