import setuptools

setuptools.setup(
    name="dartrig",
    version="0.2.1",
    install_requires=[
        'requests',
        'bs4',
        'adt_cache==0.0.14',
        'crawler_commons==0.0.54'
    ],
    license='MIT',
    author="cheddars",
    author_email="nezahrish@gmail.com",
    description="dartrig api wrapper",
    long_description_content_type="text/markdown",
    long_description=open('README.md', "r").read(),
    url="https://github.com/cheddars/dart_rigger",
    packages=setuptools.find_packages(),
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
