# -*- coding: utf-8 -*-
import sys
from cx_Freeze import setup, Executable
from version import version

build_exe_options = {
    "packages": [
        "PyQt5.QtCore",
        "psutil",
    ],
    "include_files": [
        "icons/",
    ],
    "excludes": [
        "tkinter",
        "PyQt5/Qt/",
        "PyQt5/uic/",
        "*.ui",
        "unittest/",
        "ctypes/test",
        "psutil/tests",
        "distutils/",
        "pydoc_data/",
        "icudt53.dll",
        "icuin53.dll",
        "icuuc53.dll",
        "Qt5Svg.dll",
        "imageformats/qwebp.dll",
        "imageformats/qwebp.dll",
        "imageformats/qjp2.dll",
        "imageformats/qtiff.dll",
        "imageformats/qwebp.dll",
        "imageformats/qmng.dll",
        "imageformats/qdds.dll",
        "imageformats/qicns.dll",
        "imageformats/qgif.dll",
        "imageformats/qsvg.dll",
        "imageformats/qtga.dll",
        "imageformats/qwbmp.dll",
        "_hashlib.pyd",
        "_ssl.pyd",
        "_bz2.pyd",
    ],
    "optimize": 2,
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Odoo Price Update",
    version=version,
    description="Actualizador de precios para Odoo",
    author="Comtom Tech",
    author_email="soporte@comtomtech.com",
    options={"build_exe": build_exe_options},
    executables=[
        Executable("price_updater.py", base=base, icon="icons/logo-36.png",),
    ]
)
