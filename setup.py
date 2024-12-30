import setuptools

__version__ = "0.0.0"
REPO_NAME = "End-to-End-ML-Course"
AUTHOR_USER_NAME = "lenkenslin"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "lindalenkens2510@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME, 
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app", 
    #Long_description=long_description,
    Long_description_content="text/markdown", 
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls= {"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"}, 
    packages=setuptools.find_packages(where="src")
)