import argparse
import pytest

from unittest.mock import patch

from trops.log import TropsLog, add_log_subparsers


@pytest.fixture
def setup_log_args():
    with patch("sys.argv", ["trops", "log"]):
        parser = argparse.ArgumentParser(
            prog='trops', description='Trops - Tracking Operations')
        subparsers = parser.add_subparsers()
        add_log_subparsers(subparsers)
        args, other_args = parser.parse_known_args()
    return args, other_args


def test_log(monkeypatch, setup_log_args):
    args, other_args = setup_log_args

    monkeypatch.setenv("TROPS_DIR", '/tmp/trops')
    monkeypatch.setenv("TROPS_ENV", 'testenv')
    monkeypatch.setenv("TROPS_TAGS", '#123,TEST')
    tl = TropsLog(args, other_args)

def test_log_save(monkeypatch, setup_log_args):
    args, other_args = setup_log_args
    monkeypatch.setattr(args, 'save', True, raising=False)
    monkeypatch.setenv("TROPS_TAGS", "#22")

    assert args.save == True

    tl = TropsLog(args, other_args)
    assert tl.trops_logfile == '/home/devuser/trops/log/trops.log'
    assert tl.trops_tags == '#22'

def test_prim_tag(monkeypatch, setup_log_args):
    args, other_args = setup_log_args

    monkeypatch.setenv("TROPS_DIR", '/tmp/trops')
    monkeypatch.setenv("TROPS_ENV", 'testenv')
    monkeypatch.setenv("TROPS_TAGS", '#123,TEST')
    tl = TropsLog(args, other_args)
    assert tl.trops_prim_tag == '#123'