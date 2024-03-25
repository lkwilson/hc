from argparse import ArgumentParser
from aiohttp import web, web_request

from hc.lib import get_state, set_off, set_on


async def handle(request: web_request.Request):
    if 'state' not in request.rel_url.query:
        state = get_state()
        return web.Response(text='on' if state else 'off')
    else:
        target_state = request.rel_url.query['state']
        if target_state == 'on':
            change = set_on()
        elif target_state == 'off':
            change = set_off()
        else:
            return web.Response(text='invalid state')
        return web.Response(text='ok' if change else 'no change')


app = web.Application()
app.add_routes([web.get("/outlet", handle)])


def run(port: int):
    web.run_app(app, port=port)


def main():
    parser = ArgumentParser()
    parser.add_argument("--port", "-p", type=int, help="Port to listen on")
    args = parser.parse_args()
    run(args.port)


if __name__ == "__main__":
    main()
