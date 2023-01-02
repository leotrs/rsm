import re
import subprocess

import pytest
import ujson as json

from rsm.app import ProcessorApp

EMPTY_MANUSCRIPT = ":manuscript: ::"
EMPTY_MANUSCRIPT_LOGS = {}
EMPTY_MANUSCRIPT_LOGS_V = [
    {
        "name": "RSM",
        "level": "INF",
        "msg": "Application started",
        "filename": "app.py",
        "lineno": 89,
    },
    {
        "name": "RSM",
        "level": "INF",
        "msg": "Configuring...",
        "filename": "app.py",
        "lineno": 90,
    },
    {
        "name": "RSM.parse",
        "level": "INF",
        "msg": "Parsing...",
        "filename": "tsparser.py",
        "lineno": 86,
    },
    {
        "name": "RSM.parse",
        "level": "INF",
        "msg": "Abstractifying...",
        "filename": "tsparser.py",
        "lineno": 96,
    },
    {
        "name": "RSM.tform",
        "level": "INF",
        "msg": "Transforming...",
        "filename": "transformer.py",
        "lineno": 28,
    },
    {
        "name": "RSM.tlate",
        "level": "INF",
        "msg": "Translating...",
        "filename": "translator.py",
        "lineno": 415,
    },
    {
        "name": "RSM",
        "level": "INF",
        "msg": "Done.",
        "filename": "app.py",
        "lineno": 96,
    },
]

WRONG_MANUSCRIPT = ":manuscript: * ::"
WRONG_MANUSCRIPT_LOGS = [
    {
        "name": "RSM.parse",
        "level": "WRN",
        "msg": "The CST contains errors.",
        "filename": "tsparser.py",
        "lineno": 381,
    }
]
WRONG_MANUSCRIPT_LOGS_V = [
    {
        "name": "RSM",
        "level": "INF",
        "msg": "Application started",
        "filename": "app.py",
        "lineno": 89,
    },
    {
        "name": "RSM",
        "level": "INF",
        "msg": "Configuring...",
        "filename": "app.py",
        "lineno": 90,
    },
    {
        "name": "RSM.parse",
        "level": "INF",
        "msg": "Parsing...",
        "filename": "tsparser.py",
        "lineno": 86,
    },
    {
        "name": "RSM.parse",
        "level": "INF",
        "msg": "Abstractifying...",
        "filename": "tsparser.py",
        "lineno": 96,
    },
    {
        "name": "RSM.parse",
        "level": "WRN",
        "msg": "The CST contains errors.",
        "filename": "tsparser.py",
        "lineno": 381,
    },
    {
        "name": "RSM.tform",
        "level": "INF",
        "msg": "Transforming...",
        "filename": "transformer.py",
        "lineno": 28,
    },
    {
        "name": "RSM.tlate",
        "level": "INF",
        "msg": "Translating...",
        "filename": "translator.py",
        "lineno": 415,
    },
    {
        "name": "RSM",
        "level": "INF",
        "msg": "Done.",
        "filename": "app.py",
        "lineno": 96,
    },
]


def cmd(src: str, log_format: str, verbose: int = 0):
    args = [
        "rsm-render",
        f'"{src}"',
        "-c",  # interpret source as string, not path
        "-s",  # silent, only output logs
        f"--log-format {log_format}",  # log format
        "--log-exclude-time",  # no timestamps
    ]
    if verbose:
        args.append("-" + ("v" * verbose))
    return " ".join(args)


def run(src: str, log_format: str, verbose: int = 0, replace=False, split=False):
    result = subprocess.run(
        cmd(src, log_format, verbose),
        check=True,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    ).stdout.decode("utf-8")
    if replace:
        result = re.sub(r"}\s*{", "},{", result)
    if split:
        result = [l.strip() for l in result.strip().split("\n")]
    return result


@pytest.mark.slow
def test_json_logs_of_empty_file():
    have = json.loads(run(EMPTY_MANUSCRIPT, "json") or "{}")
    assert have == EMPTY_MANUSCRIPT_LOGS


@pytest.mark.slow
def test_json_logs_of_empty_file_verbose():
    output = run(EMPTY_MANUSCRIPT, "json", verbose=1, replace=True)
    have = json.loads(f"[{output}]")
    assert have == EMPTY_MANUSCRIPT_LOGS_V


@pytest.mark.slow
def test_plain_logs_of_empty_file():
    have = run(EMPTY_MANUSCRIPT, "plain").strip() or {}
    assert have == EMPTY_MANUSCRIPT_LOGS


@pytest.mark.slow
def test_plain_logs_of_empty_file_verbose():
    have = run(EMPTY_MANUSCRIPT, "plain", verbose=1, split=True)
    assert have == [r["msg"] for r in EMPTY_MANUSCRIPT_LOGS_V]


@pytest.mark.slow
def test_json_logs_of_wrong_file():
    output = run(WRONG_MANUSCRIPT, "json", replace=True)
    have = json.loads(f"[{output}]")
    assert have == WRONG_MANUSCRIPT_LOGS


@pytest.mark.slow
def test_json_logs_of_wrong_file_verbose():
    output = run(WRONG_MANUSCRIPT, "json", verbose=1, replace=True)
    have = json.loads(f"[{output}]")
    assert have == WRONG_MANUSCRIPT_LOGS_V


@pytest.mark.slow
def test_plain_logs_of_wrong_file():
    have = run(WRONG_MANUSCRIPT, "plain", split=True)
    assert have == [r["msg"] for r in WRONG_MANUSCRIPT_LOGS]


@pytest.mark.slow
def test_plain_logs_of_wrong_file_verbose():
    have = run(WRONG_MANUSCRIPT, "plain", verbose=1, split=True)
    assert have == [r["msg"] for r in WRONG_MANUSCRIPT_LOGS_V]


# # we need to set (and later unset?) the logger at run()-time, not at instantiation time
# # test using the following:
# aj = ProcessorApp(plain=source, log_time=False, log_format="json")
# ar = ProcessorApp(plain=source, log_time=False, log_format="rsm")
