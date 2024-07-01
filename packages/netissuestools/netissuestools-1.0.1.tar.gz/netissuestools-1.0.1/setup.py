import setuptools
# 若Discription.md中有中文 須加上 encoding="utf-8"
with open("Discription.md", "r",encoding="utf-8") as f:
    long_description = f.read()
  
setuptools.setup(
    name = "netissuestools",#套件的名稱，盡量不要包含"-","_"。
    version = "1.0.1",
    author = "wing",
    author_email="tomt99688@gmail.com",
    description="To solve some network issues",
    long_description=long_description,#PyPi上對此專案的介紹
    long_description_content_type="text/markdown",#係MIME格式,即係話比Pypi知要以md文件格讀取
    url="https://github.com/Wing9897/Network_issues_solution.git",
    packages=setuptools.find_packages(),
    install_requires=['ping3>=4.0.0'],
    classifiers=[#分類項目
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'sfastping = wingtools1.Superfast_multithread_ping:main',
        ]
    }
    )
    
#python setup.py sdist bdist_wheel 
#python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*