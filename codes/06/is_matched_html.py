from array_stack import ArrayStack


def is_matched_html(raw):
    """Return True if all HTML tags are properly match; False otherwise."""
    S = ArrayStack()
    j = raw.find("<")  # find first '<' character (if any)
    while j != -1:
        k = raw.find(">", j + 1)  # find next '>' character
        if k == -1:
            return False  # invalid tag
        tag = raw[j + 1 : k]  # strip away < >
        if not tag.startswith("/"):  # this is opening tag
            S.push(tag)
        else:
            if S.is_empty():
                return False  # nothing to match with
            if tag[1:] != S.pop():
                return False  # mismatched delimiter
        j = raw.find("<", k + 1)  # find next '<' character (if any)
    return S.is_empty()  # were all opening tags matched?


if __name__ == "__main__":
    html = """
    <html>
    <body>
    <hl>this is title</p>
    <p>This is the passage.</hl>
    </body>
    </html>
    """
    print(is_matched_html(html))
