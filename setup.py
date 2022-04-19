from distutils.core import setup
setup(
  name = 'hg0428db',  
  packages = ['hg0428db'], 
  version = '0.0.3',  
  license='MIT', 
  description = 'A simple remote database system designed for replit terminal games.', 
  author = 'Hudson Gouge',        
  author_email = 'hudson.gouge@icloud.com',     
  url = 'https://github.com/hg0428/hg0428db',  
  download_url = 'https://github.com/hg0428/hg0428db/archive/refs/tags/v0.0.2.tar.gz',
  keywords = ['Database', 'db', 'API'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',  
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)