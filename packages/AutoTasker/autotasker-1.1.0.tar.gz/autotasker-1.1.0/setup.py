from setuptools import setup, find_packages

setup(
    name='AutoTasker',
    version='1.1.0',
    packages=find_packages(),
    install_requires=[
        'setuptools==70.2.0',
    ],
    entry_points={
        'console_scripts': [
            'AutoTasker=AutoTasker.main:main_function',
        ],
    },
    test_suite='tests',
    tests_require=[
        'pytest',
    ],
    author='mramosg7',
    author_email='marioramos.cobisa@gmail.com',
    description='AutoTasker is a console application designed to simplify and automate repetitive tasks without the '
                'need for programming skills. With AutoTasker, you can easily set up a variety of automated tasks, '
                'saving you time and effort in your daily activities.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mramosg7/AutoTasker',
    license='MIT',
)