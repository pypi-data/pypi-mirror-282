from setuptools import setup
def readrst():
    with open('README.rst',encoding='utf-8') as f:
        content = f.read()
    return content
setup(name='dirA',version='1.0.0',description='test inside is kunkun',long_description=readrst(),author='xiaotiantian',author_email='xiaotiantian@163.com',packages=['dirA'],py_modules=['tool'],license='MIT')