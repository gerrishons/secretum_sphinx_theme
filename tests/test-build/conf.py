import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

extensions = [
    "secretum_sphinx_theme",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "sphinx_rtd_theme"
