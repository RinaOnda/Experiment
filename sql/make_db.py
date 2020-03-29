#!/usr/bin/env python
#create table from csv file

import sys, getpass
import subprocess, os
import pandas as pd
import sqlite3
import mysql.connector

FOLDER = './sql/'
DATAFILE = FOLDER + 'db_data.csv' 

#sql setting
host_name = 'localhost'
user_name = 'root'
password = 'password'
database = 'example_db'
table = 'new_tb'

#recreate the table if true
RECREATE = False

def main():
    if os.path.exists(DATAFILE):
        #assuming the first row specifies dtype
        with open(DATAFILE, mode='r') as f:
            for line in f:
                dtypes = line.split(',')
                break
        df = pd.read_csv(DATAFILE,header=1)
        import_db(df, dtypes)

#______________________________________________________________________
def import_db(df, dtypes):
    con = mysql.connector.connect(user=user_name,passwd=password,host=host_name,db=database)
    cur = con.cursor()

    if RECREATE:
        sql = 'drop table if exists %s'%table
        cur.execute(sql)

    sql = 'create table if not exists %s(id int)'%table
    cur.execute(sql)

    #add columns
    for column, dtype in zip(df.columns.values, dtypes):
        sql = 'select NULL from INFORMATION_SCHEMA.COLUMNS where table_name="%s" and table_schema="%s" and column_name="%s"'%(table, database, column)
        cur.execute(sql)
        ret = cur.fetchall()
        if len(ret)==0:
            sql = 'alter table %s add column %s %s'%(table, column, dtype)
            cur.execute(sql)

    #get column list in db
    sql = 'show columns from %s'%table
    cur.execute(sql)
    ret = cur.fetchall()
    column_list = [x[0] for x in ret]

    #get id
    sql = 'select id from %s order by id desc limit 1'%(table)
    cur.execute(sql)
    ret = cur.fetchone()
    new_id = -1
    if (ret):
        new_id = ret[0]
    new_id += 1

    for row, items in df.iterrows():
        sql = 'insert into %s values('%table
        for col, i in zip(column_list, range(len(column_list))):
            if i > 0:
                sql += ', '
            if col in items:
                if col == 'id':
                    sql += '"%s"'% new_id
                else:
                    sql += '"%s"' % items[col]
            else:
                sql += 'NULL'
        sql += ')'
        cur.execute(sql)
        new_id += 1

    sql = 'select * from %s'%table
    cur.execute(sql)
    print('****** new table ******')
    for row in cur.fetchall():
        print(row)

    while True:
        print('save? select y/n --> ')
        ans = input()
        if ans == 'y': 
            con.commit()
            print('saved!')
            break
        elif ans =='n':
            print('aborted!')
            break

    con.close()
    return

#--------------------------------------------------------------------
if __name__ == '__main__':
    main()

