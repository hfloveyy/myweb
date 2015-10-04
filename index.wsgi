# coding: UTF-8
import os
import sae
from run import app

application = sae.create_wsgi_app(app)