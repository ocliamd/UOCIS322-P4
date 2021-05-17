import nose
import arrow
import acp_times

def test_open_300():
    assert str(acp_times.open_time(75, 300, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T02:12:00+00:00"
    assert str(acp_times.open_time(150, 300, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T04:25:00+00:00"
    assert str(acp_times.open_time(200, 300, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T05:53:00+00:00"
    assert str(acp_times.open_time(250, 300, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T07:27:00+00:00"
    assert str(acp_times.open_time(300, 300, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T09:00:00+00:00"
    assert str(acp_times.open_time(305, 300, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T09:00:00+00:00"

def test_close_300():
    assert str(acp_times.close_time(75, 300, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T05:00:00+00:00"
    assert str(acp_times.close_time(150, 300, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T10:00:00+00:00"
    assert str(acp_times.close_time(200, 300, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T13:20:00+00:00"
    assert str(acp_times.close_time(250, 300, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T16:40:00+00:00"
    assert str(acp_times.close_time(300, 300, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T20:00:00+00:00"
    assert str(acp_times.close_time(305, 300, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T20:00:00+00:00"