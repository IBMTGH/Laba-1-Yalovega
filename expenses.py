import json 
import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "action",
    type=str,
    metavar="action",
    help="Действия: {add-category,add,total,list}",
    choices=["list","add","total","add-category"]
)
args=parser.parse_args()
if args.action=="list":
    print(12)
elif args.action=="add":
    print(1488)
elif args.action=="total":
    print(67)
elif args.action=="add-category":
    print(45)
print(sys.argv) 