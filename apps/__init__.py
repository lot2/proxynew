#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)

from apps import index, database, sql, normal, proxy, user, pwd





