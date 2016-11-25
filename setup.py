import platform

from distutils.core import setup


def main():
	OPTIONS = {
	    'iconfile':'images/atlassian.icns',
	    'plist': {'CFBundleShortVersionString':'0.1.0',}
	}

	if platform.system().lower() == 'darwin':
		import py2app
		setup(
			app=["excel2jira.py"], 
			setup_requires=["py2app"],
			options={'py2app': OPTIONS})
	else:
		import py2exe
		setup(console=['excel2jira.py'])


if __name__ == '__main__':
	main()