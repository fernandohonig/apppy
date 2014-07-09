#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO -- implement required params check

import MySQLdb

from flask import Flask
from flask import request

# ##########
# Flask'ing
app = Flask(__name__)

# ########################################
# AUTHENTICATION

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    '''
    landing page
    '''
    out = '¡Hola!'
    return out, 200

@app.route('/db', methods=['GET'])
def db():
    '''
    test db connection
    '''
    out = 'connecting to MySQL db... '
    
    try:
        db = MySQLdb.connect(host="localhost",
                             user="apppy",
                             passwd="qwerty",
                             db="apppy")

#         cur = db.cursor() 
#     
#         sql = '''select key_, val_ from keyval;'''
#     
#         cur.execute(sql)
#     
#         out += '<table><th>key_</th><th>val_</th>'
#         for row in cur.fetchall() :
#             out += "<tr><td>%s</td><td>%s</td></tr>" % (row[0], row[1])
#         out += '</table>'

        out += 'success'
    except:
        out += 'failed'

    return out, 200

@app.route('/ip', methods=['GET'])
def ip():
    '''
    test db connection
    '''
    out = "Your IPv4 address is: %s" % request.remote_addr
    return out, 200

def main():
    # ##########
    # FLASK
    app.run(port=5000, debug=True)

if __name__ == '__main__':
    main()
