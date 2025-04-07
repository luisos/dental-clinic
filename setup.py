from py2exe.build_exe import py2exe
from distutils.core import setup
setup(console=[{"script": "main.pyw"}],
      options={'py2exe': {"dll_excludes": ["MSVCP90.dll"], 'includes': ['sip']}})
