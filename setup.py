from distutils.core import setup
setup(
  name = 'hg0428db',         # How you named your package folder (MyLib)
  packages = ['hg0428db'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A simple remote database system designed for replit terminal games.',   # Give a short description about your library
  author = 'Hudson Gouge',                   # Type in your name
  author_email = 'hudson.gouge@icloud.com',      # Type in your E-Mail
  url = 'https://github.com/hg0428/hg0428db',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/hg0428/hg0428db/archive/refs/tags/v0.0.1.tar.gz',    # I explain this later on
  keywords = ['Database', 'db', 'API'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'warnings'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which python versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)