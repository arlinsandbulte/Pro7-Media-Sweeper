# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['Pro7 Media Sweeper.py'],
             pathex=['./Pro7-File-API-Python/'],
             binaries=[],
             datas=[('./resource_files', 'resource_files')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='Pro7 Media Sweeper',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch='x86_64',
          codesign_identity=None,
          entitlements_file=None , icon='resource_files/icons/sweeper.icns')
app = BUNDLE(exe,
             name='Pro7 Media Sweeper.app',
             icon='resource_files/icons/sweeper.icns',
             bundle_identifier=None,
             version='2.3.0')
