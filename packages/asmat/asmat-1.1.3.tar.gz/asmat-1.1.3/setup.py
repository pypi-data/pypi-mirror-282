import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'asmat',         # How you named your package folder (MyLib)
  packages=["asmat", "asmat.analysis"],   # Chose the same as "name"
  py_modules=["asmat", "asmat.analysis"],
  include_package_data=True,
  package_dir={"":"src"},
  package_data={"": ["*.db"]},
  version = "1.1.3",      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Assembly Testing and Analysis',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Erwan LEMATTRE',                   # Type in your name
  author_email = 'erwanlem4@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/erwanlem/atp',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/erwanlem/atp/archive/refs/tags/v1.0.tar.gz', 
  keywords = ['ASSEMBLER', 'TEST', 'ANALYSIS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'bs4',
          'matplotlib',
          'pillow'
      ],
  classifiers=[
    "Programming Language :: Python :: 3",
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    "Operating System :: OS Independent",
  ],
  python_requires= ">=3.6"
)