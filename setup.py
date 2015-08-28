from distutils.core import setup

setup(
    name='buildbot_status_slack',
    version='0.1.0',
    author=['Andrew S. Brown', 'Sylvain Zimmer', 'Marten Klitzke', 'Raphael Randschau'],
    packages=[],
    scripts=[],
    url='https://github.com/mp-andrew/buildbot-status-slack',
    license='LICENSE.txt',
    description='slack status plugin for buildbot',
    long_description=open('README.md').read(),
    install_requires=[
        "buildbot >= 0.8.0",
    ],
)
