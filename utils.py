import re


def add_bold(text):
    bolds = {
        "url": r"http(s)?:\/\/[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+",
        "hash": r"(?:\s|^)#[A-Za-z0-9\-\.\_]+(?:\s|$)",
        "handle": r"(?:\s|^)@[A-Za-z0-9\-\.\_]+(?:\s|$)",
    }
    for css_class, regex in bolds.items():
        res = re.search(regex, text)
        if res:
            start = res.start()
            end = res.end()
            text = (
                add_bold(text[:start])
                + f'<b class="{css_class}">'
                + text[start:end]
                + "</b>"
                + add_bold(text[end:])
            )
    return text
