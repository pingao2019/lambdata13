# to build package

# setup.py

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pingao2019-lambdata13",
    version="1.0",
    author="pingao2019",
    author_email="pingao2019@outlook.com",
    description="For software programming",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/pingao2019/lambdata13.git",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)