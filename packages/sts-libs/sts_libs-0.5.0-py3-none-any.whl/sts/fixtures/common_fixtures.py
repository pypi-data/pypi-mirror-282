from collections.abc import Generator

import pytest

from sts import scsi_debug
from sts.utils.cmdline import run


@pytest.fixture(scope='class', autouse=True)
def _log_check() -> Generator:
    """Checks if a new coredump entry was generated during the test."""
    last_dump = run('coredumpctl -1', msg='Checking dumps before test').stdout
    yield
    recent_dump = run('coredumpctl -1', msg='Checking dumps after test').stdout
    assert recent_dump == last_dump, 'New coredump appeared during the test'


@pytest.fixture(scope='class')
def scsi_debug_test() -> Generator:
    scsi_debug.scsi_debug_load_module()
    yield scsi_debug.get_scsi_debug_devices()
    scsi_debug.scsi_debug_unload_module()
