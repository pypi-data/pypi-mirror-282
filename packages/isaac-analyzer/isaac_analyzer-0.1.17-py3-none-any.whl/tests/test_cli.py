import subprocess


def test_version():
    result = subprocess.run(
        ["isaac-analyzer", "--version"], capture_output=True, text=True
    )
    assert result.returncode == 0
    assert "isaac-analyzer 0.1.17" in result.stdout
