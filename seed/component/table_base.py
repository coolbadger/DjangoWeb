#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: table
# Author		: badger
# Created		: 2017/7/19
# Description	: 

class TableView(object):
    table_name = ""
    class_name = None
    titles = []
    data_columns = []

    def __init__(self, name):
        self.table_name = name

    def add_column(self, new_column):
        if type(new_column) is Column:
            self.titles.append(new_column.name)
            self.data_columns.append(new_column)


class Column(object):
    name = None
    key = None
    data = None
    visible = True

    def __init__(self, name, key):
        self.name = name
        self.key = key
    
