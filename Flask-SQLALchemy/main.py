# 1.1 Flask-SQLALchemy 是一个为了Flask增加SQLALchemy支持的扩展。它致力于简化在Flask中SQLALchemy的使用，提供了有用的默认值和额外的API来更简单地完成常见任务

# 1.2 安装Flask-SQLALchemy
#      pip install flask-sqlalchemy

# 数据库的连接，以sqlite为例

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# 创建flask对象
app = Flask(__name__)



# sqlite数据库连接
# 获取项目所在的绝对路径
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# 配置数据库 （sqlite数据库)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR,'db.sqlite')

# MySQL数据库连接 (MySQL连接需要安装pymysql依赖)
# app.config["SQLALCHEMY_DATABASE_URI"]="maysql+pymysql://username:password@localhost/（数据库名字）"

# 配置动态追踪修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 创建SQLALchemy核心对象
db = SQLAlchemy(app)

# 常用的字段类型
# 属性     | 描述
# -------- | -----
# String  | 字符串
# Text  | 长文本
# Integer | 整型
# Float  | 浮点型
# Date | 时间类型年月日
# DateTime | 时间类型年月日时分秒

# 常用的字段属性
# 属性     | 描述
# -------- | -----
# primary_key | 主键
# unique | 键值唯一性
# unllable | 索引
# default | 默认值

# 数据库创建
class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32))
    age = db.Column(db.Integer)


# 增

# 增加一条
# table = Table(name='zx',age=13)
# session = db.session
# session.add(table)
# session.commit()
# 增加多条
# s1 =  Table(name='老李',age=14)
# s2 =  Table(name='刘六',age=16)
# s3 =  Table(name='戚七',age=12)
# session = db.session
# session.add_all([s1,s2,s3])
# session.commit()

# id    name   age
# 1 	zx  	13
# 2 	ls  	14
# 3 	ww  	16
# 4 	zl  	12
# 5 	老李	14
# 6 	李四	16
# 7 	王五	12
# 8 	老李	14
# 9 	刘六	16
# 10	戚七	12

# 查询

# 查询所有
# table = Table.query.all()
# print(table) # [<Table 1>, <Table 2>, <Table 3>, <Table 4>]
# 查询一条 （id=1）
# table = Table.query.get(1)
# print(table) # [<Table 1>]
# 查询多条 （年龄=16）
# table = Table.query.filter_by(age=16).all()
# print(table) # [<Table 3>, <Table 6>, <Table 9>]
# 查询多条 （年龄<=14）
# table = Table.query.filter(Table.age <= 14).all()
# print(table) # [<Table 1>, <Table 2>, <Table 4>, <Table 5>, <Table 7>, <Table 8>, <Table 10>]
# 模糊查询 （年龄小于16 名字带‘李’）
# table = Table.query.filter(Table.age < 16 ,Table.name.like("%李%")).all()
# print(table) # [<Table 5>, <Table 8>]

# 改
# table = Table.query.get(1)
# table.name = '小李'
# print(table.name) # 小李
# db.session.commit()

# 删
# 删除id = 2的用户
# table = Table.query.get(2)
# session = db.session
# session.delete(table)
# session.commit()
#
# t = Table.query.get(2)
# print(t) # None




db.create_all()






