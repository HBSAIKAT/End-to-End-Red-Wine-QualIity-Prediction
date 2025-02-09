import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-to-End-Red-Wine-QualIity-Prediction"
AUTHOR_USER_NAME = "HBSAIKAT"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "habibulbasher01644@gmail.com"

setuptools.setup(
    name=f"{REPO_NAME}-{SRC_REPO}-{AUTHOR_USER_NAME}",
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="This is a project on Red Wine Quality Prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)