from setuptools import setup


requires = ["requests>=2.14.2"]


setup(
    name='pykniout_reward',
    version='0.0.1',
    description='コード引き換えライブラリ',
    url='https://github.com/nmlyz/pykniout_reward',
    author='nmlyz',
    author_email='',
    license='MIT',
    keywords='nmlyz project',
    packages=[
        "pyknioutReward",
    ],
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)