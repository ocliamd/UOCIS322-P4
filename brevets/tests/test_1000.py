import nose
import arrow
import acp_times 

def test_open_1000():
    assert str(acp_times.open_time(599, 1000, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T18:46:00+00:00"
    assert str(acp_times.open_time(620, 1000, arrow.get('2020-01-01T00:00:00'))) == "2020-01-01T19:31:00+00:00"
    assert str(acp_times.open_time(1000, 1000, arrow.get('2020-01-01T00:00:00'))) == "2020-01-02T09:05:00+00:00"
    assert str(acp_times.open_time(1050, 1000, arrow.get('2020-01-01T00:00:00'))) == "2020-01-02T09:05:00+00:00"

def test_close_1000():
    assert str(acp_times.close_time(599, 1000, arrow.get('2020-01-01T00:00:00'))) == "2020-01-02T15:56:00+00:00"
    assert str(acp_times.close_time(620, 1000, arrow.get('2020-01-01T00:00:00'))) == "2020-01-02T17:45:00+00:00"
    assert str(acp_times.close_time(1000, 1000, arrow.get('2020-01-01T00:00:00'))) == "2020-01-04T03:00:00+00:00"
    assert str(acp_times.close_time(1050, 1000, arrow.get('2020-01-01T00:00:00'))) == "2020-01-04T03:00:00+00:00"