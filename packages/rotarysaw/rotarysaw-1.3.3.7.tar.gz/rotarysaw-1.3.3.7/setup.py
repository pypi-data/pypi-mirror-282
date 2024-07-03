from setuptools import setup, find_packages

VERSION = '1.3.3.7'
DESCRIPTION = 'Rotary Saw'
LONG_DESCRIPTION = 'Turrican turns into a rotary saw in combat. This is my personal import collection for quick scripts and helpers. So Nice to have it under PyPi. It will not be useful for whomever finds this, but I hope it could be one day.'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="rotarysaw",
    version=VERSION,
    author="Kuu Tirronen",
    author_email="<kuu@uraanikaivos.fi>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['tabulate'],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'turrican', 'rotary saw', 'tirronen', 'rotarysaw'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.11',
    ]
)