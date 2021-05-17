import nose
import arrow
import acp_times

def test_open_600():
    assert str(acp_times.open_time(399, 600, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T12:06:00+00:00"
    assert str(acp_times.open_time(410, 600, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T12:28:00+00:00"
    assert str(acp_times.open_time(475, 600, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T14:38:00+00:00"
    assert str(acp_times.open_time(600, 600, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T18:48:00+00:00"
    assert str(acp_times.open_time(650, 600, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T18:48:00+00:00"


def test_close_600():
    assert str(acp_times.open_time(399, 600, arrow.get('2020-01-01T00:00:00'))) == "2020-01-02T02:36:00+00:00"
    assert str(acp_times.open_time(410, 600, arrow.get('2020-01-01T00:00:00'))) == "2020-01-02T03:20:00+00:00"
    assert str(acp_times.open_time(475, 600, arrow.get('2020-01-01T00:00:00'))) == "2020-01-02T07:40:00+00:00"
    assert str(acp_times.open_time(600, 600, arrow.get('2020-01-01T00:00:00'))) == "2020-01-02T16:00:00+00:00"
    assert str(acp_times.open_time(650, 600, arrow.get('2020-01-01T00:00:00'))) == "2020-01-02T16:00:00+00:00"
