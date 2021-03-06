import json
import pytest
import requests
import southwest
import checkin
from datetime import datetime, timedelta
from .my_vcr import custom_vcr
from pytz import timezone, utc
from tzlocal import get_localzone

my_vcr = custom_vcr()
r = southwest.Reservation('XXXXXX', 'John', 'Smith')


@my_vcr.use_cassette()
def test_generate_headers():
    print(southwest.Reservation.generate_headers())


@my_vcr.use_cassette()
def test_reservation_lookup():
    print(r.notifications)
    try:
        r.lookup_existing_reservation()
    except Exception:
        pytest.fail("Error looking up reservation")


@my_vcr.use_cassette()
def test_checkin():
    phone = southwest.Notifications.Phone('1234567890')
    email = southwest.Notifications.Email('test@example.com')
    r.notifications = [phone, email]
    try:
        r.checkin()
    except Exception:
        pytest.fail("Error checking in")


@my_vcr.use_cassette()
def test_checkin_without_passes():
    phone = southwest.Notifications.Phone('1234567890')
    email = southwest.Notifications.Email('test@example.com')
    r.notifications = [phone, email]
    try:
        r.checkin()
    except Exception:
        pytest.fail("Error checking in")


@my_vcr.use_cassette()
def test_openflights_api():
    assert southwest.timezone_for_airport('LAX').zone == "America/Los_Angeles"


@my_vcr.use_cassette()
def test_cli():
    try:
        checkin.auto_checkin('XXXXXX', 'John', 'Smith')
    except Exception:
        pytest.fail("cli error")
