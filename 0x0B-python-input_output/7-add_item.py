#!/usr/bin/python3
"""
a script that adds all arguments to a Python list,
and then save them to a file:
"""
import sys
import os

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


len_args = len(sys.argv)
args_ls = list()
count = 1
while (count < len_args):
    args_ls.append(sys.argv[count])
    count += 1

if os.path.exists("add_item.json"):
    obj = load_from_json_file("add_item.json")
    for item in args_ls:
        obj.append(item)
    save_to_json_file(obj, "add_item.json")
else:
    save_to_json_file(args_ls, "add_item.json")
