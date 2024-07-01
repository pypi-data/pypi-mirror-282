from setuptools import setup

setup(
    name='mtlhtml',
    version='1.0',
    description='A tool that help you to write HTML in Python',
    long_description='<p style="text-align: center">\n<img src="./logo.png">\n</p>\n<h1 style="text-align: center">By We Are In Space</h1>\n<h3 style="text-align: center">Write HTML in Python with MTL</h3>\n\n## ⬇️ Installation\n\n**Use Pip to install packgages in your project.**\n\n```shell\npip install mtl\n```\n\n### 📚 Docs\n\n<a href="ff">https://www.weareinspace.net/mtl/docs</a>',
    url='https://github.com/WeAreInSpace/MTL',
    author='WeAreInSpace',
    author_email='weareinspace.net@gmail.com',
    license='MIT',
    keywords='html in python website ssg',
    packages=['mtl'],
    package_dir={'mtl': 'src/mtl'},
    package_data={'mtl': ['css/*.py']}
)