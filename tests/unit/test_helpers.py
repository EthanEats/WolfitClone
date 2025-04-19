from datetime import datetime, timedelta
from app.helpers import pretty_date





def test_pretty_date_just_now():
    now = datetime.utcnow()
    assert pretty_date(now) == "just now"

def test_pretty_date_seconds():
    now = datetime.utcnow()
    newtime = now - timedelta(seconds=30)
    assert pretty_date(newtime) == "29 seconds ago"\
    or pretty_date(newtime) == "30 seconds ago"\
    or pretty_date(newtime) == "31 seconds ago"

def test_pretty_date_single_minute():
    now = datetime.utcnow()
    newtime = now - timedelta(minutes=1, seconds=30)
    assert pretty_date(newtime) == "a minute ago" 

def test_pretty_date_minutes():
    now = datetime.utcnow()
    newtime = now - timedelta(minutes=36, seconds=30)
    assert pretty_date(newtime) == "36 minutes ago" 

def test_pretty_date_single_hour():
    now = datetime.utcnow()
    newtime = now - timedelta(hours=1, minutes=36)
    assert pretty_date(newtime) == "an hour ago" 

def test_pretty_date_hours():
    now = datetime.utcnow()
    newtime = now - timedelta(hours=16, minutes=30)
    assert pretty_date(newtime) == "16 hours ago" 

def test_pretty_date_int_timestamp():
    now = datetime.utcnow()
    newtime = now - timedelta(hours=16, minutes=30)
    newtime = int(newtime.timestamp())
    assert pretty_date(newtime) == "16 hours ago" 

def test_pretty_date_no_time_specified():
    assert pretty_date() == "just now" 

def test_pretty_date_one_day():
    now = datetime.utcnow()
    newtime = now - timedelta(days=1, hours=16, minutes=30)
    assert pretty_date(newtime) == "Yesterday" 

def test_pretty_date_days():
    now = datetime.utcnow()
    newtime = now - timedelta(days=4, hours=16, minutes=30)
    assert pretty_date(newtime) == "4 days ago" 

def test_pretty_date_weeks():
    now = datetime.utcnow()
    newtime = now - timedelta(days=16, hours=16, minutes=30)
    assert pretty_date(newtime) == "2 weeks ago" 

def test_pretty_date_months():
    now = datetime.utcnow()
    newtime = now - timedelta(days=230, hours=16, minutes=30)
    assert pretty_date(newtime) == "7 months ago" 

def test_pretty_date_years():
    now = datetime.utcnow()
    newtime = now - timedelta(days=3120, hours=16, minutes=30)
    assert pretty_date(newtime) == "8 years ago" 

def test_pretty_date_future():
    now = datetime.utcnow()
    newtime = now + timedelta(minutes=30)
    assert pretty_date(newtime) == "just about now" 