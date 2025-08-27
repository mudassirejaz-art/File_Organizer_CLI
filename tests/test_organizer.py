import os
import shutil
import pytest
import organizer



TEST_DIR = "test_files"

@pytest.fixture
def setup_files(tmp_path):
    # create temporary test folder
    test_dir = tmp_path / TEST_DIR
    test_dir.mkdir()

    # create dummy files
    (test_dir / "image.jpg").write_text("fake image")
    (test_dir / "doc.txt").write_text("fake doc")
    (test_dir / "archive.zip").write_text("fake zip")

    return test_dir

def test_organize_by_type(setup_files):
    organizer.organize_by_type(str(setup_files), dry_run=False)

    assert os.path.exists(setup_files / "Images" / "image.jpg")
    assert os.path.exists(setup_files / "Documents" / "doc.txt")
    assert os.path.exists(setup_files / "Archives" / "archive.zip")

def test_dry_run(setup_files):
    organizer.organize_by_type(str(setup_files), dry_run=True)

    # Dry run hone ke baad files still original jagah pe hone chahiye
    assert os.path.exists(setup_files / "image.jpg")
    assert os.path.exists(setup_files / "doc.txt")
    assert os.path.exists(setup_files / "archive.zip")
