#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/2/20 15:52 
# @Author : Edison 
# @Version：V 0.1
# @File : basic_mysql.py
# @desc : 关系数据库入门
import pymysql
import sys

# 新增部门语句
INSERT_TB_DEPT = """
insert into tb_dept (dno, dname, dloc) 
values (%s, %s, %s)
"""
# 删除部门语句
DELETE_TB_DEPT = """
delete from tb_dept where dno=%s
"""
# 更新部门语句
UPDATE_TB_DEPT = """
update tb_dept set dname=%s, dloc=%s
where dno=%s
"""
# 查询全部部门数量
FIND_ALL_TB_DEPT_COUNT = """
select count(dno) as total from tb_dept
"""
# 分页查询部门
SELECT_TB_DEPT = """
select dno as id, dname as deptname, dloc as address 
from tb_dept limit %s offset %s
"""


class TbDept(object):

    def __init__(self, id, deptname, address):
        self.id = id
        self.deptname = deptname
        self.address = address

    def __str__(self):
        return f'\n编号：{self.id}\n名称：{self.deptname}\n所在地：{self.address}'


def input_dept_info():
    dno = input('编号: ')
    name = input('名称: ')
    dloc = input('所在地: ')
    return dno, name, dloc


# 添加一个部门
def add_tb_dept(con):
    dno, name, dloc = input_dept_info()
    try:
        with con.cursor() as cursor:
            if cursor.execute(INSERT_TB_DEPT,
                              (dno, name, dloc)) == 1:
                print('添加部门成功!')
    except pymysql.MySQLError as err:
        print(err)
        print('添加部门失败!')


# 删除一个部门
def del_tb_dept(con):
    del_id = int(input('请输入要删除的部门编号:'))
    try:
        with con.cursor() as cursor:
            if cursor.execute(DELETE_TB_DEPT, (del_id,)) == 1:
                print('该部门已经删除!')
    except pymysql.MySQLError as err:
        print(err)
        print('删除部门失败!')


# 更新部门
def update_tb_dept(con):
    dno, name, dloc = input_dept_info()
    try:
        with con.cursor() as cursor:
            if cursor.execute(UPDATE_TB_DEPT,
                              (name, dloc, dno)) == 1:
                print('部门信息已经更新!')
    except pymysql.MySQLError as err:
        print(err)
        print('更新部门信息失败!')


# 查询全部部门
def find_all_tb_dept(con):
    page, size = 1, 5
    try:
        with con.cursor() as cursor:
            cursor.execute(FIND_ALL_TB_DEPT_COUNT)
            total = cursor.fetchone()['total']
            while True:
                cursor.execute(SELECT_TB_DEPT,
                               (size, (page - 1) * size))
                for dept_dict in cursor.fetchall():
                    dept = TbDept(dept_dict['id'], dept_dict['deptname'], dept_dict['address'])
                    # dept = TbDept(dept_dict)
                    print(dept)
                    print('dept_dict:', type(dept_dict))
                    print('dept:', type(dept))
                if page * size < total:
                    choice = input('继续查看下一页?(yes|no)')
                    if choice.lower() == 'yes':
                        page += 1
                    else:
                        break
                else:
                    print('没有下一页记录!')
                    break
    except pymysql.MySQLError as err:
        print(err)


def main():
    # autocommit=True 执行SQL之后自动提交事务
    con = pymysql.connect(host='localhost', port=3306,
                          user='root', password='yourpassword',
                          db='hrs', charset='utf8mb4',
                          autocommit=True, cursorclass=pymysql.cursors.DictCursor)
    # add_tb_dept(con)
    print('所有部门'.center(50, '*'))
    find_all_tb_dept(con)
    # del_tb_dept(con)
    # update_tb_dept(con)


if __name__ == '__main__':
    main()



