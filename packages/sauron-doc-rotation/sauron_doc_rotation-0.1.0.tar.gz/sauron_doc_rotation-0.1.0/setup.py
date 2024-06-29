import io
import re

from setuptools import find_packages, setup

run_requirements = [
    "numpy==2.0.0",
    "scikit-image==0.24.0",
    "scipy==1.14.0",
    "matplotlib==3.9.0",
    "pytesseract==0.3.10",
    "opencv-python==4.10.0.84",
    "imutils==0.5.4",
    "loguru==0.7.2",
]

with io.open("./sauron_doc_rotation/__init__.py", encoding="utf8") as version_f:
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_f.read(), re.M
    )
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

with io.open("README.md", encoding="utf8") as readme:
    long_description = readme.read()

setup(
    name="sauron-doc-rotation",
    version=version,
    author="Augusto Modesto",
    description="Fix rotation in images",
    url="https://github.com/modestoo/sauron-doc-rotation.git",
    download_url="https://github.com",
    keywords=["image-processing", "image-rotation", "rotation", "text"],
    packages=find_packages(),
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=run_requirements,
    python_requires="==3.10.*",
    classifiers=[
        "Intended Audience :: Information Technology",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.10",
    ],
)
