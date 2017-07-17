#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script Name	: util
# Author		: badger
# Created		: 2017/7/16
# Description	: 

import re


def search_str(expr_str, context):
    result = ""
    if re.search(expr_str, context):
        result = re.search(expr_str, context).group(1)
    return result
