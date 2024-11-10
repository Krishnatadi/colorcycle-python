from setuptools import setup, find_packages

setup(
    name='colorcycle',
    version='1.0.1',
    author='Krishna Tadi',
    author_email='',
    description='ColorCycle is a Python package that helps developers easily convert color formats between Hex, RGB, and HSL. This tool is ideal for designers and developers working on color management for websites, applications, and graphical projects. Simply provide a color in any of the supported formats, and ColorCycle will convert it into the others.',
    packages=find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url='https://github.com/krishnatadi/colorcycle-python',
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
    ],
    python_requires='>=3.6',
    keywords='web scraping, data extraction, html parser, scraping',
    project_urls={
    'Documentation': 'https://github.com/krishnatadi/colorcycle-python#readme',
    'Source': 'https://github.com/krishnatadi/colorcycle-python',
    'Issue Tracker': 'https://github.com/krishnatadi/colorcycle-python/issues',
    },
    license='MIT'
)