import setuptools

import secretum_sphinx_theme

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=secretum_sphinx_theme.__name__,
    version=secretum_sphinx_theme.__version__,
    author=secretum_sphinx_theme.__author__,
    description=secretum_sphinx_theme.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scalabli/secretum_sphinx_theme",
    download_url=f"https://github.com/scalabli/secretum_sphinx_theme/archive/v{secretum_sphinx_theme.__version__}.tar.gz",
    packages=setuptools.find_packages(exclude=["tests"]),
    package_data={
        "secretum_sphinx_theme": [
            "static/dark_mode_css/general.css",
            "static/dark_mode_css/dark.css",
            "static/dark_mode_js/theme_switcher.js",
            "static/dark_mode_js/default_light.js",
            "static/dark_mode_js/default_dark.js",
        ]
    },
    license=secretum_sphinx_theme.__license__,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["sphinx-rtd-theme"],
)
