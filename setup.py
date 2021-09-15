from setuptools import setup, find_packages

setup(
    name = 'PyPokerGUI_tomtest',
    version = '0.0.7',
    author = 'ishikota',
    author_email = 'ishikota086@gmail.com',
    description = 'GUI application for PyPokerEngine',
    license = 'MIT',
    keywords = 'python poker engine gui',
    url = 'https://github.com/tomS-mindlab/PyPokerGUI_tomtest',
    packages = [pkg for pkg in find_packages() if pkg != "tests"],
    package_data={
        'pypokergui_tomtest': [
            'server/static/*.css',
            'server/static/*.js',
            'server/static/images/*',
            'server/templates/*',
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        'tornado==4.4.2',
        'click==6.7',
        'PyYAML==3.12',
    ],
    entry_points={
        'console_scripts': ['pypokergui=pypokergui.__main__:cli']
    },
    )

