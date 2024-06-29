import setuptools
with open('README.md','r' , encoding='utf-8') as f:
    data = f.read()
setuptools.setup(
    name= 'Pyrows',
    version= '0.2.2',
    author= 'youssef-khaled',
    description= 'library storage and management in txt files by-rows',
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License"
    ],
    long_description= data,
    long_description_content_type= 'text/markdown'

)   