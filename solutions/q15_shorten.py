def shorten(title, limit):
    if len(title) <= limit:
        return title
    return title[:limit - 1] + "…"
