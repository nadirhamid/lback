import os, os.path
import sys
import shutil
from lback.lib.dal import DAL,Field
import json
import subprocess



try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

from distutils.command.build_py import build_py
from distutils.command.install import install

class installsetup(install):
    def run(self):
      version = get_version()
      cwd = os.getcwd()
      os.remove(cwd+"/db.sql")
      db = open(cwd+"/db.sql","w+")
      db.close()
      home_path = os.getenv("HOME")
    
        
      if os.path.isdir("%s/.lback"%(home_path)):
          shutil.rmtree("%s/.lback"%(home_path))

      os.makedirs("%s/.lback"%(home_path))
      os.makedirs("%s/.lback/backups/"%(home_path))
      os.makedirs("%s/.lback/bin/"%(home_path))
	
      lback_path = "%s/.lback/"%(home_path)
      links = [
            (cwd+"/lback/main.py", "%s/bin/lback.py"%(lback_path)),
            (cwd+"/lback/dal.py", "%s/bin/dal.py"%(lback_path)),
            (cwd+"/lback/odict.py", "%s/bin/odict.py"%(lback_path)),
            (cwd+"/bin/lback", "%s/bin/lback"%(lback_path)),
            (cwd+"/bin/lback-client", "%s/bin/lback-client"%(lback_path)),
            (cwd+"/bin/lback-server", "%s/bin/lback-server"%(lback_path)),
            (cwd+"/settings.json", "%s/settings.json"%(lback_path)),
            (cwd+"/profiles.json", "%s/profiles.json"%(lback_path)),
            (cwd+"/db.sql", "%s/db.sql"%(lback_path))
        ]
      for i in links:
	 if os.path.islink(i[1]):
	      os.remove(i[1])
         subprocess.Popen(['ln', '-s', i[0], i[1]])
      install.run(self)

def get_version():
  import pkg_resources
  try:
    version = pkg_resources.get_distribution("LinuxOpenSuseBackupTool").version
  except:
    return None
  return version

def get_settings():
  file = open(".lback/settings.json", "r")
  jsonobj = json.loads(file.read())
  file.close()
  return jsonobj
   

def finalizesetup():
	pass
 

setup(name="LinuxOpenSuseBackupTool",
      version="0.1.0",
      description="Quick and simple backups for linux",
      maintainer="Nadir Hamid",
      maintainer_email="matrix.nad@gmail.com",
      url="https://",
      download_url = "https://pypi.python.org/pypi/",
      license="MIT",
      long_description="",
      packages=["lback", "lback/lib/", "lback/rpc/"],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Communications',
          'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
          'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      cmdclass=dict(install=installsetup))



