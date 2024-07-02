from setuptools import setup, find_packages


setup(name='yj_tts',
      version='0.0.1',
      description='YunJing TTS',
      project_urls={
        'Code': 'https://gitlab.yunjingtech.cn:10010/distribution/DigitalHuman'
      },
      author='huqian',
      author_email='huqian@yunjingtech.cn',
      packages=find_packages(),
      license="LICENSE",
      python_requires='>=3.10',
      install_requires=[
            'edge_tts==6.1.11',
            'pymysql==1.1.1',
            'DBUtils==3.1.0',
            'fastapi==0.111.0',
            'soundfile==0.12.1',
            'requests==2.31.0',
            'numpy==1.26.4',
            'starlette==0.37.2',
            'apscheduler==3.10.4'
      ],
      zip_safe=False
      )
