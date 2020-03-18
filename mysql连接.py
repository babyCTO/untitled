import  pymysql

#设置打开数据库连接
db=pymysql.connect("95.179.239.100","root","ZQa51650703","mydb")

#设置游标对象
cursor=db.cursor()
#sql执行语句：
sql="insert into uu (name) values('王二');"
#"insert into uu values('张三');"#写入数据库表的字段值
#"alter table uu change name id int not null;"#修改表字段名（必须保证该字段空值或类型一致）
#"delete from uu;"#清空表中所有字段值
#"alter table  uu drop name;"#删除表字段
#"alter table uu add (name varchar(8) not null,age int(8) not null);" 增加数据库表字段
#"update uu set name='张’；#修改整个字段值
#"uodate uu set name='张' where id='3';#修改制定表字段的值
#"drop table uu;"#删除数据表操作
#"create table uu (id  int AUTO_INCREMENT Primary Key);"#创建表id 并自增


#设置执行命令行操作语句
cursor.execute(sql)
#提交确认修改
db.commit()
#获取单条数据查询结果
data=cursor.fetchall()
#返回此次执行影响的行数
data1=cursor.rowcount

print(data)
print(data1)
#关闭游标函数
cursor.close()
#关闭数据库连接
db.close()
