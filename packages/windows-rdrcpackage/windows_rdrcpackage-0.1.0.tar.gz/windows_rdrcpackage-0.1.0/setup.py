from setuptools import setup, find_packages

setup(
    name='windows_rdrcpackage',  # 套件名稱
    version='0.1.0',  # 版本號
    description='A package for image processing and file renaming',  # 套件描述
    long_description=open('README.md').read(),  # 長描述，通常從 README.md 文件中讀取
    long_description_content_type='text/markdown',  # 長描述的內容類型
    url='https://github.com/peggy2125/windows_rdrcpackage.git',  # 套件的URL（例如GitHub倉庫）
    packages=find_packages(),  # 自動查找所有套件
    install_requires=[
        'opencv-python',
        'numpy'
    ],  # 套件依賴
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Python版本要求
)