from pathlib import Path

def setup(app):
    path = Path(__file__).parent.absolute()
    app.add_html_theme('rsm_test_theme', path)
