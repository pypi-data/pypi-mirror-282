from setuptools import setup, find_packages  
  
with open('README.md', 'r', encoding='utf-8') as f:  
    long_description = f.read()  
  
setup(  
    name='quantumtrader_ta',  # 通常这里应该是包的名字，不是库的子集  
    version='0.2',  
    packages=find_packages(),  
    description='一个基于freqtrade的量化交易策略系统',  
    long_description=long_description,  
    long_description_content_type='text/markdown',  
    author='YUCHIU',  
    author_email='yu.chiu@foxmail.com',  
    url='https://gitee.com/yu-chiu/quantum_trader',  
    classifiers=[  
        'Development Status :: 3 - Alpha',  
        'Intended Audience :: Developers',  
        'License :: OSI Approved :: MIT License',  # 假设您使用的是MIT许可证  
        'Operating System :: OS Independent',  
        'Programming Language :: Python',  
        'Programming Language :: Python :: 3',  
        'Programming Language :: Python :: 3 :: Only',  
        'Programming Language :: Python :: 3.10',  
        'Programming Language :: Python :: 3.11',  
        'Programming Language :: Python :: 3.12',  
        'Topic :: Office/Business :: Financial',  # 更具体的分类器  
        'Topic :: Scientific/Engineering :: Artificial Intelligence',  # 量化交易可能涉及AI  
    ],  
    python_requires='>=3.8',  
    install_requires=[  
        "freqtrade",  # 添加freqtrade作为依赖项  
        "pandas_ta",  
        "TA-Lib",  
        "PyWavelets",  
        "scipy",  
        "matplotlib"
    ],  

)