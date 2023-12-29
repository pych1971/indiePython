def make_header(text: str, header: int = 1) -> str:
    text_html = (f'<h{header}>{text}</h{header}>')
    return text_html
