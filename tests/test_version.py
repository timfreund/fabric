"""
Tests covering Fabric's version number pretty-print functionality.
"""

from nose.tools import eq_

import fabric.version


def test_get_version():
    for version, version_str, verbose_version_str in [
        ((0, 2, 0, 'final'), '0.2', '0.2 final'),
        ((0, 2, 1, 'final'), '0.2.1', '0.2.1 final'),
        ((0, 2, 0, 'alpha', 1), '0.2a1', '0.2 alpha 1'),
        ((0, 2, 1, 'beta', 1), '0.2.1b1', '0.2.1 beta 1')
    ]:
        fabric.version.VERSION = version
        yield eq_, fabric.version.get_version(), version_str
        yield eq_, fabric.version.get_version(verbose=True), verbose_version_str
