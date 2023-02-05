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

def test_build(init_fixture):
    """Test the build function."""
    # Run build function
    hub.build()
    # Check if 'index.html' exists
    assert os.path.isfile("build/index.html")
