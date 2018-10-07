import os
import subprocess
from setuptools import setup
from setuptools import find_packages


def version():
    if not os.path.isdir(".git"):
        print "This does not appear to be a Git repository."
        return
    try:
        p = subprocess.Popen(["git", "describe",
                              "--tags", "--always"],
                             stdout=subprocess.PIPE)
    except EnvironmentError:
        print "unable to run git, leaving ecdsa/_version.py alone"
        return
    stdout = p.communicate()[0]
    if p.returncode != 0:
        print "unable to run git, leaving ecdsa/_version.py alone"
        return
    return stdout[:-1]


README = os.path.join(os.path.dirname(__file__), 'README.md')


setup(
    name='mattermost_marmiton',
    version=version(),
    description="Marmiton Integration Service for Mattermost.",
    long_description=README,
    classifiers=[],
    author='d@corp',
    author_email='dakorp@ematome.com',
    url='https://github.com/tidalf/mattermost-integration-marmiton',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==0.10.1',
        'requests==2.10.0',
    ]
)
