# Copyright (c) 2024 nggit

import asyncio
import ssl

from . import __version__
from .response import Response
from .utils import read_header, parse_chunked


class H1Client:
    def __init__(self, host, port=80, secure=False, loop=None):
        if host.startswith('/'):
            _host = 'localhost'
        else:
            _host = host

        self.host = host
        self.port = port
        self.ssl_context = {
            80: None,
            443: ssl.create_default_context()
        }.get(port, (secure or None) and ssl.create_default_context())
        self.connections = []
        self.headers = [
            b'Host: %s:%d' % (_host.encode('latin-1'), self.port),
            b'User-Agent: h1client/%s' % __version__.encode('latin-1'),
            b'Accept: */*'
        ]

        if loop is None:
            self.loop = asyncio.get_event_loop()

    def update_cookie(self, value):
        name, _ = value.split(b'=', 1)

        for i, header in enumerate(self.headers):
            if header.startswith(b'Cookie: %s=' % name):
                self.headers[i] = b'Cookie: %s' % value
                break
        else:
            self.headers.append(b'Cookie: %s' % value)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()

    async def open(self):
        try:
            return self.connections.pop(0)
        except IndexError:
            if self.host.startswith('/'):
                return await asyncio.open_unix_connection(self.host)

            return await asyncio.open_connection(
                self.host, self.port, ssl=self.ssl_context
            )

    async def close(self):
        while self.connections:
            _, writer = self.connections.pop()

            writer.close()
            await writer.wait_closed()

    async def send(self, line, data=b'', headers=None, timeout=30):
        if b' HTTP/' not in line:
            line += b' HTTP/1.1'

        if not headers:
            headers = []

        if data:
            if headers == []:
                headers.append(
                    b'Content-Type: application/x-www-form-urlencoded'
                )
            headers.append(b'Content-Length: %d' % len(data))

        conn = await self.open()
        reader, writer = conn
        writer.write(b'')

        try:
            await writer.drain()
        except ConnectionResetError:
            conn = await self.open()
            reader, writer = conn

        writer.write(
            b'%s\r\n%s\r\n\r\n%s' %
            (line, b'\r\n'.join(self.headers + headers), data)
        )
        await writer.drain()
        timer = self.loop.call_at(self.loop.time() + timeout, writer.close)

        try:
            header = await reader.readuntil(b'\r\n\r\n')
            content_length = (
                read_header(header, b'Content-Length')[0] or
                read_header(header, b'content-length')[0]
            )
            transfer_encoding = (
                read_header(header, b'Transfer-Encoding')[0] or
                read_header(header, b'transfer-encoding')[0]
            )
            cookies = (read_header(header, b'Set-Cookie') +
                       read_header(header, b'set-cookie'))

            for cookie in cookies:
                if cookie:
                    self.update_cookie(cookie[:cookie.find(b';')])

            if content_length:
                body = await reader.readexactly(int(content_length))
            elif b'chunked' in transfer_encoding.lower():
                body = parse_chunked(
                    await reader.readuntil(b'\r\n0\r\n\r\n')
                )
            else:
                # not an ordinary response. upgraded? who knows?
                return Response(header, b'', reader, writer)

            self.connections.append(conn)
            return Response(header, body, reader, writer)
        except asyncio.IncompleteReadError as exc:
            await writer.wait_closed()
            raise TimeoutError('timeout after %gs' % timeout) from exc
        finally:
            timer.cancel()
