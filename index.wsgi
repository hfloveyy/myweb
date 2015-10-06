# coding: UTF-8
import os
import sys

 


 

 
app_root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(app_root, 'site-packages'))



import sae
from myapp import app

application = sae.create_wsgi_app(app)