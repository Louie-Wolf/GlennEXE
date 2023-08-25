from setuptools import setup

APP=['GlennRenamer.py']
DATA_FILES = ['icon.gif']
OPTIONS = {
    'argv_emulation': True,
    'iconfile' : 'icon.gif',

}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app' : OPTIONS},
    setup_requires=['py2app'],
)