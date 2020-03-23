# -*- coding: utf-8 -*-
import pytest
from subsync.subsync_gui import _make_version_tuple


@pytest.mark.parametrize('vstr, expected', [
    ('v0.1.1', (0, 1, 1)),
    ('v1.2.3', (1, 2, 3)),
    ('4.5.6.1', (4, 5, 6, 1))
])
def test_version_tuple_from_string(vstr, expected):
    assert _make_version_tuple(vstr) == expected