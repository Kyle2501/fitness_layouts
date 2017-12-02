#!/usr/bin/python
# coding: latin-1




#----------------------------------------------#
#             Code                             #
#----------------------------------------------#
import os
import urllib
import wsgiref.handlers
import webapp2
from webapp2_extras import routes
import json
import logging
# - 
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
# -
from google.appengine.ext import db
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
# -
from urlparse import urlparse
import urllib2
# -
import time
import datetime





#----------------------------------------------#
#            Error Handling                    #
#----------------------------------------------#
def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('A 404 error occurred!')
    response.set_status(404)

def handle_500(request, response, exception):
    logging.exception(exception)
    response.write('A 500 error occurred!')
    response.set_status(500)
#----------------------------------------------#
#                                              #
#----------------------------------------------#
app = webapp2.WSGIApplication([    # - Pages

    ('/', publicSite),


], debug=True)

