#!/usr/bin/env python
#read xml files

import pandas as pd
from xml.etree import ElementTree

FOLDER = './xml/'
DATAFILE = FOLDER + 'example.xml'

def main():
    read_xml()

#--------------------------------------------------------
def read_xml():
    tree = ElementTree.parse(DATAFILE)
    root = tree.getroot()
    Tables= root.findall('.//Table')

    item_list = []
    for table in Tables:
        table_name = table.find('TableName')
        if table_name.text == 'new_tb':
            items = table.findall('.//Item')
            for item in items:
                name = item.find('name').text
                score = item.find('score').text
                item_list.append([name, score])

    df = pd.DataFrame(item_list, columns=['name', 'score'])
    print(df)

    return

#--------------------------------------------------------------------
if __name__ == '__main__':
    main()

