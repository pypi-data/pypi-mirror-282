from setuptools import setup
from setuptools.command.install import install
from distutils.command.build import build
from sys import maxsize
from os import path
from os import name as oname

BASEPATH = path.dirname(path.abspath(__file__))
GCC_PATH = path.join(BASEPATH, 'libhupf','gcc')

class Build(build):
  def run(self):
    # run original build code
    build.run(self)
    build_path = path.abspath(self.build_temp)
    
    if maxsize > 2**32 : #64 bit
      makefile = "makefile64"
    else:
      makefile = "makefile"
    
    cmd = [
      'make',
      'OUT=' + build_path,
      '-f ' + makefile,
    ]

    def compile():
      call(cmd, cwd=GCC_PATH)

    self.execute(compile, [], 'Compiling libhupf')

    # copy resulting tool to library build folder
    self.mkpath(self.build_lib)

    if not self.dry_run:
      self.copy_file("libhupf.so", self.build_lib)


class Install(install):
  if not oname == "nt":
    def initialize_options(self):
      install.initialize_options(self)
      self.build_scripts = None

    def finalize_options(self):
      install.finalize_options(self)
      self.set_undefined_options('build', ('build_scripts', 'build_scripts'))

  def run(self):
    # run original install code
    install.run(self)
    target = path.join(BASEPATH, 'license.txt')
    self.copy_file(target, path.join(self.install_lib,'libhupf'))
    
    if oname == "nt": #just copy binaries
      if maxsize > 2**32 : #64 bit
        target = path.join(BASEPATH, 'bin', 'win64','libhupf.dll')
      else: #32bit
        target = path.join(BASEPATH, 'bin','win32','libhupf.dll')
      self.copy_file(target, path.join(self.install_lib,'libhupf'))

setup(
  name='libhupf',
  version='0.1',
  packages=['libhupf'],
  cmdclass={
      'install': Install
  },
  author = 'Jose Capco'
)
