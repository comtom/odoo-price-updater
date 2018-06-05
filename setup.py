# -*- coding: utf-8 -*-
import sys
from cx_Freeze import setup, Executable
from price_updater import __price_updater_version__


build_exe_options = {
    "packages": [
        "PyQt5.QtCore",
        "psycopg2",
        "psutil",
    ],
    "include_files": [
        "config/",
    ],
    "optimize": 2,
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Odoo Price Updater",
    version=__price_updater_version__,
    description="Actualizador de precios para Odoo",
    author="Comtom Tech",
    author_email="soporte@comtomtech.com",
    options={"build_exe": build_exe_options},
    executables=[
        Executable("price_updater.py", base=base, icon="icons/logo-36.ico",),
    ]
)
