#测试的是类的定义

#了解一下什么是类
'''Python中一切都是对象，那对象是怎么产生的呢？
对象是由类产生的，如果把对象比作饼干，那么类就是定义对象的模具
同时类也时产生对象的对象。类是将方法（行为）和属性（状态）包裹起来，对象与类共享方法，属性不共享，方法一样，但处理的数据类型可能不一样，产生的属性值可能就不一样'''

#定义类
class Student:      #class是定义类的关键字；类名首字母大写；多个单词时采用驼峰原则，例如GoodStudent

    def __init__(self,name,age):    #定义构造函数
        self.name = name
        self.age =age

    def say_age(self):
        print('{0}的年龄是{1}'.format(self.name,self.age))

s = Student('吴悸',25)     #实例对象
s.say_age()