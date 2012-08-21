#coding:utf-8
skeleton = """---
layout: post
title: %(title)s
category: %(category)s
tags: 
---"""
from optparse import OptionParser
import os, sys
from datetime import datetime

parser = OptionParser()
parser.add_option("-t", "--title", dest="title", help="Title of the post")
parser.add_option("-c", "--category", dest="category", help="category of the post")
parser.add_option("-n", "--name", dest="name", help="name of the post")

(options, args) = parser.parse_args()
if options.title and options.category and options.name:
    today = datetime.today().strftime("%Y-%m-%d")
    post_name = "%s-%s.md" % (today, options.name)
    post_name = os.path.join("_posts", post_name)
    if os.path.exists(post_name):
        print "%s already exists!" % post_name
        parser.print_help()
        sys.exit(0)
    else:
        cont = skeleton % {"title" : options.title, "category" : options.category}
        fh = open(post_name, "w")
        fh.write(cont)
        fh.close()
        print "%s created successfully!" % post_name
        sys.exit(0)
else:
    print "You must specify title and category of the post, and also the name of the file"
    parser.print_help()
    sys.exit(0)


