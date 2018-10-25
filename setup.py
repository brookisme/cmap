from distutils.core import setup
setup(
  name = 'cmap',
  packages = ['cmap'],
  version = '0.0.0.1',
  description = 'SublimeRemote: A Sublime-SFTP companion',
  author = 'Brookie Guzder-Williams',
  author_email = 'bguzder-williams@wri.org',
  url = 'https://github.com/brookisme/cmap',
  download_url = 'https://github.com/brookisme/cmap/tarball/0.1',
  keywords = ['Sublime-SFTP','Sublime'],
  include_package_data=True,
  data_files=[
    (
      'config',[]
    )
  ],
  classifiers = [],
  entry_points={
      'console_scripts': [
          'cmap=cmap.cli:cli'
      ]
  }
)