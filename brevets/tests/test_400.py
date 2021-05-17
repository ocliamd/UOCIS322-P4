import nose
import arrow
import acp_times

def test_open_400():
    assert str(acp_times.open_time(275, 400, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T08:14:00+00:00"
    assert str(acp_times.open_time(300, 400, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T09:00:00+00:00"
    assert str(acp_times.open_time(400, 400, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T12:08:00+00:00"
    assert str(acp_times.open_time(450, 400, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T12:08:00+00:00"

def test_close_400():
    assert str(acp_times.close_time(275, 400, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T18:20:00+00:00"
    assert str(acp_times.close_time(300, 400, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T20:00:00+00:00"
    assert str(acp_times.close_time(400, 400, arrow.get('2020-01-01T00:00:00'))) == "2020-01-02T03:00:00+00:00"
    assert str(acp_times.close_time(450, 400, arrow.get('2020-01-01T00:00:00'))) == "2020-01-02T03:00:00+00:00"