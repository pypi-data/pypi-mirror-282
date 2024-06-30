from setuptools import setup, find_packages

setup(
    name='revengine',
    version='0.0.1',
    description='RevEngine',
    author='James Evans',
    author_email='joesaysahoy@gmail.com',
    url='https://github.com/primal-coder/Revengine',
    packages=find_packages(),
    install_requires=[
        'dicepy',
        'entyty',
        'CharActor',
        'CharObj',
        'gridengine_framework',
        'pyglet',
        'pymunk'
    ],
    scripts=[
        'revengine/__main__.py'
    ]
)