# vim:fileencoding=utf-8:noet

from setuptools import setup

setup(
    name='powerline-treesitter',
    description='A Powerline segment for showing treesitter status.',
    version='0.1.0',
    keywords='powerline treesitter nvim neovim prompt',
    author='Stefan Sonski',
    author_email='s.sonski@gmail.com',
    url='https://github.com/stefansonski/powerline-treesitter',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Terminals'
    ],
    packages=setuptools.find_packages(),
)