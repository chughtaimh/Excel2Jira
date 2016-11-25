import platform
from distutils.core import setup

if platform.system().lower() == 'darwin':
	import py2app
	setup(app=["excel2jira.py"], setup_requires=["py2app"])

else:
	import py2exe
	setup(console=['excel2jira.py'])

