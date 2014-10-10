
import distutils
import py2exe

distutils.core.setup(
    console=['pend.py'],

    name="pend",
    version="0.0",
    author='James Abel',
    author_email='j@abel.co',
    url='abel.co',
    license='LICENSE', # points to the actual file
    description="pend on one or more files",

    # make a single executable
    options={'py2exe': {'bundle_files': 1, 'compressed': True, }},

    zipfile = None,
)
