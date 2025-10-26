# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for Calculadora com Integração Numérica
This file defines how to build the executable.
"""

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('src', 'src'),
    ],
    hiddenimports=[
        'ttkbootstrap',
        'ttkbootstrap.themes',
        'numpy',
        'numpy.core',
        'scipy',
        'matplotlib',
        'matplotlib.backends.backend_tkagg',
        'matplotlib.figure',
        'PIL',
        'PIL._tkinter_finder',
        'tkinter',
        'tkinter.ttk',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'fastapi',
        'uvicorn',
        'jinja2',
        'webapp',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Calculadora-Integral',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console window
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Add icon path here if you have one
)
