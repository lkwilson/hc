from argparse import ArgumentParser
from hc.lib import set_on, set_off


def main():
    parser = ArgumentParser()
    parser.add_argument("state", choices=["on", "off"], help="Set the state of device")
    args = parser.parse_args()

    if args.state == "on":
        res = set_on()
    else:
        res = set_off()
    if res:
        print('ok')
    else:
        print('already', args.state)



if __name__ == "__main__":
    main()
