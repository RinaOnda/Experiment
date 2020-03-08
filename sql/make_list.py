#!/usr/bin/env python

import subprocess, sys, time, json, os

FOLDER = './sql/'
SQLFILE = FOLDER + "MakeList.sql"
SQLTMPFILE = FOLDER + "MakeList_tmp.sql"
SQLFILEFIRST = FOLDER + "MakeList_first.sql"
SQLFILELAST = FOLDER + "MakeList_last.sql"
SQLFILEDICT = FOLDER + "MakeList_dict.sql"
OUTPUTFILE = FOLDER + 'list.txt'
PHYLUM = 'chordata'

#sql setting
host_name = 'localhost'
user_name = 'root'
password = 'password'
database = 'example_db'

def main():
   name_list = get_name_list()
   if len(name_list)==0:
       print('list is empty!')
       return

   fout = open(OUTPUTFILE,'w')
   for name in name_list:
      fout.write(name + '\n')

   fout.close()

   print('wrote ' + OUTPUTFILE)

   return

def get_phylum_id():
    fread = open(SQLFILEDICT,'r')
    fwrite = open(SQLTMPFILE, 'w')
    lines = fread.readlines()
    for line in lines:
        new_line = line.replace('PHYLUM', PHYLUM)   
        fwrite.write(new_line)
    fread.close()
    fwrite.close()
    if host_name == 'local':
        ret = subprocess.check_output('mysql -u %s --password=%s -D %s < %s'%(user_name,password,database,SQLTMPFILE), shell=True)
    else:
        ret = subprocess.check_output('mysql -h %s -u %s --password=%s -D %s < %s'%(host_name,user_name,password,database,SQLTMPFILE), shell=True)
    ret = ret.split()
    phylum_id = int(ret[2])

    return phylum_id

def get_name_list():
    phylum_id = get_phylum_id()
    phylum_id = 'phylum = ' + str(phylum_id)

    fread = open(SQLFILEFIRST,'r')
    fwrite = open(SQLTMPFILE, 'w')
    lines = fread.readlines()
    for line in lines:
        new_line = line.replace('phylum = -1', phylum_id)   
        fwrite.write(new_line)
    fread.close()
    fwrite.close()
    ret = subprocess.check_output('mysql -h %s -u %s --password=%s -D %s < %s'%(host_name,user_name,password,database,SQLTMPFILE), shell=True)
    ret = ret.split()
    first_id = int(ret[4])

    fread = open(SQLFILELAST,'r')
    fwrite = open(SQLTMPFILE, 'w')
    lines = fread.readlines()
    for line in lines:
        new_line = line.replace('phylum = -1', phylum_id)   
        fwrite.write(new_line)
    fread.close()
    fwrite.close()
    ret = subprocess.check_output('mysql -h %s -u %s --password=%s -D %s < %s'%(host_name,user_name,password,database,SQLTMPFILE), shell=True)
    ret = ret.split()
    last_id = int(ret[4])

    id_list_tmp = range(first_id, last_id+1)
    name_list = []
    for id_tmp in id_list_tmp:
        fread = open(SQLFILE,'r')
        fwrite = open(SQLTMPFILE, 'w')
        new_id = 'id = ' + str(id_tmp)
        lines = fread.readlines()
        for line in lines:
            new_line = line.replace('phylum = -1', phylum_id)   
            new_line = new_line.replace('id = -1', new_id)   
            fwrite.write(new_line)
        fread.close()
        fwrite.close()

        ret = subprocess.check_output('mysql -h %s -u %s --password=%s -D %s < %s'%(host_name,user_name,password,database,SQLTMPFILE), shell=True)
        if(ret):
            ret = ret.split()
            name = ret[5].decode('utf-8')
            name_list.append(name)
      
    subprocess.check_output('rm %s'%SQLTMPFILE,shell=True)   

    print(name_list)
    return name_list


#------------------------
if __name__ == '__main__':
    main()
