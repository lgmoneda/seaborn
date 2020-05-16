import numpy as np
import matplotlib as mpl

from numpy.testing import assert_array_equal

from ..core import (
    _VectorPlotter,
    unique_dashes,
    unique_markers,
)


class TestVectorPlotter:

    def test_flat_variables(self, flat_data):

        p = _VectorPlotter()
        p.establish_variables(data=flat_data)
        assert p.input_format == "wide"
        assert list(p.variables) == ["x", "y"]
        assert len(p.plot_data) == len(flat_data)

        try:
            expected_x = flat_data.index
            expected_x_name = flat_data.index.name
        except AttributeError:
            expected_x = np.arange(len(flat_data))
            expected_x_name = None

        x = p.plot_data["x"]
        assert_array_equal(x, expected_x)

        expected_y = flat_data
        expected_y_name = getattr(flat_data, "name", None)

        y = p.plot_data["y"]
        assert_array_equal(y, expected_y)

        assert p.variables["x"] == expected_x_name
        assert p.variables["y"] == expected_y_name


class TestCoreFunc:

    def test_unique_dashes(self):

        n = 24
        dashes = unique_dashes(n)

        assert len(dashes) == n
        assert len(set(dashes)) == n
        assert dashes[0] == ""
        for spec in dashes[1:]:
            assert isinstance(spec, tuple)
            assert not len(spec) % 2

    def test_unique_markers(self):

        n = 24
        markers = unique_markers(n)

        assert len(markers) == n
        assert len(set(markers)) == n
        for m in markers:
            assert mpl.markers.MarkerStyle(m).is_filled()
