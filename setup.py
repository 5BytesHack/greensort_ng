from setuptools import setup


def _get_version():
    with open('VERSION') as fd:
        return fd.read().strip()


setup(
    name='aio-demo',
    version=_get_version(),
    packages=['aio_demo'],
    package_dir={'': 'backend'},
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'aio-demo-serve=main:main',
        ]
    }
)