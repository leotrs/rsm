import glob
import pytest

files = [fn[7:-4] for fn in glob.glob('inputs/*.rst')]

@pytest.mark.parametrize('filename', files)
def test_inputs(filename):
    with open(f'outputs/{filename}.html', 'r') as file:
        output = file.read().strip()
    with open(f'targets/{filename}.html', 'r') as file:
        target = file.read().strip()

    assert output == target
