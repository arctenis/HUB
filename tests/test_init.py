import os
import pytest
import hub

def test_init(tmp_path):
    """Test the init function."""
    # Run init function
    hub.init(tmp_path)
    # Check if 'content' directory exists
    assert os.path.isdir(f"{tmp_path}/content")
    assert os.path.isdir(f"{tmp_path}/build")
    # Check if 'index.md' in content directory exists
    assert os.path.isfile(f"{tmp_path}/content/index.md")
    # Check if 'config.yaml' exists
    assert os.path.isfile(f"{tmp_path}/config.yaml")

def test_build(tmp_path):
    """Test the build function."""
    # Run build function
    hub.init(tmp_path)
    hub.build(tmp_path)
    # Check if 'index.html' exists
    assert os.path.isfile(f"{tmp_path}/build/index.html")
    # Check if css file path is correct
    with open(f"{tmp_path}/build/index.html", "r") as f:
        html = f.read()
    # Check if css file is based on theme in config.yaml
    theme = "default"
    with open(f"{tmp_path}/config.yaml", "r") as f:
        config = f.read()
        theme = config.split("theme: ")[1].strip()
    assert f"css/{theme}.css" in html
