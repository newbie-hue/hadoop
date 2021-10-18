



async def fetch(session, url, headers=None, timeout=9):
    _headers = {
        'User-Agent': ('Mozilla/5.0 (compatible; MSIE 9.0; '
                       'Windows NT 6.1; Win64; x64; Trident/5.0)'),
    }
    if headers:
        _headers = headers
    try:
        async with session.get(url, headers=_headers, timeout=timeout) as response:
            status = response.status
            html = await response.read()
            encoding = response.get_encoding()
            if encoding == 'gb2312':
                encoding = 'gbk'
            html = html.decode(encoding, errors='ignore')
            redirected_url = str(response.url)
    except Exception as e:
        msg = 'Failed download: {} | exception: {}, {}'.format(url, str(type(e)), str(e))
        print(msg)
        html = ''
        status = 0
        redirected_url = url
    return status, html, redirected_url