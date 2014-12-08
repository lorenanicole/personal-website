# This file contains the WSGI configuration required to serve up your
# web application at http://lorenanicole.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# Below are templates for Django and Flask.  You should update the file
# appropriately for the web framework you're using, and then
# click the 'Reload /yourdomain.com/' button on the 'Web' tab to make your site
# live.


# +++++++++++ CUSTOM WSGI +++++++++++
# If you have a WSGI file that you want to serve using PythonAnywhere, perhaps
# in your home directory under version control, then use something like this:
#
#import os
#import sys
#
#path = '/home/lorenanicole/path/to/my/app
#if path not in sys.path:
#    sys.path.append(path)
#
#from my_wsgi_file import application

activate_this = '/home/lorenanicole/environment/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os
import sys

# assuming your django settings file is at '/home/lorenanicole/mysite/settings.py'
path = '/home/lorenanicole/personal-website/'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'lorenamesa.settings'

sys.path.append('/home/lorenanicole/personal-website/lorenamesa/wsgi.py')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()


# +++++++++++ FLASK +++++++++++
# Here is a simple Flask app. It is currently serving the default welcome
# page.  You can adapt this if you want.
#
# If you're using a different web framework, you'll need to comment all of this
# out

