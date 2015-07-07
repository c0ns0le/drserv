from setuptools import setup

install_requires = (
    'pyaml',
    'crtauth',
    'six',
    'requests==2.6.0',
)

tests_require = (
    'nose',
)

setup_requires = (
    'flake8',
)

setup(
    name='drserv',
    version='0.1.0',
    url='https://github.com/spotify/drserv',
    author='Client Build Squad @ Spotify',
    author_email='client-build@spotify.com',
    description=('RESTful service for publishing packages to debian '
                 'repositories'),
    license='Apache 2.0',
    packages=['drserv'],
    test_suite='nose.collector',
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=setup_requires,
    entry_points={
        'console_scripts': [
            'drserv-server = drserv.server:main',
            'drserv-client = drserv.client:main'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Build Tools',
    ],
)
