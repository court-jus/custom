import datetime
from babel.dates import format_date, format_time


def extra_context(locale=None):
    now = datetime.datetime.now()
    kwargs = {"format": "short"}
    if locale:
        kwargs["locale"] = locale
    fmt_time = format_time(now, **kwargs)
    kwargs = {}
    if locale:
        kwargs["locale"] = locale
    fmt_date = format_date(now, "EEEE dd MMMM", **kwargs)
    return {"datetime": {"now": now, "fmt_time": fmt_time, "fmt_date": fmt_date}}
