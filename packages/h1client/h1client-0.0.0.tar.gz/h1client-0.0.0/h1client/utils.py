# Copyright (c) 2024 nggit


def read_header(header, key):
    name = b'\r\n%s: ' % key
    headers = []
    start = 0

    while True:
        start = header.find(name, start)

        if start == -1:
            break

        start += len(name)
        headers.append(header[start:header.find(b'\r\n', start)])

    return headers or [b'']


def parse_chunked(data):
    if not data.endswith(b'\r\n0\r\n\r\n'):
        return False

    data = bytearray(data)
    body = bytearray()

    while data != b'0\r\n\r\n':
        i = data.find(b'\r\n')

        if i == -1:
            return False

        try:
            chunk_size = int(data[:i].split(b';')[0], 16)
        except ValueError:
            return False

        del data[:i + 2]

        if data[chunk_size:chunk_size + 2] != b'\r\n':
            return False

        body.extend(data[:chunk_size])
        del data[:chunk_size + 2]

    return body
