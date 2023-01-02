import subprocess

import pytest
import ujson as json

from rsm.app import ProcessorApp

EMPTY_MANUSCRIPT = ":manuscript: ::"
EMPTY_MANUSCRIPT_LOGS = {
    "msg": "Manuscript with no title",
    "name": "RSM.tlate",
    "level": "WRN",
    "filename": "translator.py",
    "lineno": 471,
}


def cmd(src, log_format):
    return " ".join(
        [
            "rsm-render",
            f'"{src}"',
            "-c",  # interpret source as string, not path
            "-s",  # silent, only output logs
            f"--log-format {log_format}",  # log format
            "--log-exclude-time",  # no timestamps
        ]
    )


def run(src, log_format):
    return subprocess.run(
        cmd(src, log_format),
        check=True,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    ).stdout.decode("utf-8")


@pytest.mark.slow
def test_json_logs_of_empty_file():
    have = json.loads(run(EMPTY_MANUSCRIPT, "json"))
    assert have == EMPTY_MANUSCRIPT_LOGS


@pytest.mark.slow
def test_plain_logs_of_empty_file():
    have = run(EMPTY_MANUSCRIPT, "plain").strip()
    assert have == EMPTY_MANUSCRIPT_LOGS["msg"]


# # we need to set (and later unset?) the logger at run()-time, not at instantiation time
# # test using the following:
# aj = ProcessorApp(plain=source, log_time=False, log_format="json")
# ar = ProcessorApp(plain=source, log_time=False, log_format="rsm")
