from distutils.core import setup
setup(
  name = 'kvJSON',         # How you named your package folder (MyLib)
  packages = ['kvJSON'],   # Chose the same as "name"
  version = '1.1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'An easy way to work with JSON in Python.',   # Give a short description about your library
  author = 'Dillon Runke',                   # Type in your name
  author_email = 'dillonr5@live.wsd1.org',      # Type in your E-Mail
  url = 'https://github.com/Kronifer/kvJSON',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Kronifer/kvJSON/archive/v1.0.0.tar.gz',    # I explain this later on
  keywords = ['JSON', 'Data Storage'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.8',
  ],
)