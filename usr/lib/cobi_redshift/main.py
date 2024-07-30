#! /bin/env python3
from argparse import ArgumentParser
import os, sys
from x11 import X11Randr

VERSION="1.0.0"

def is_x11():
    session_type = os.environ["XDG_SESSION_TYPE"]
    return session_type.lower() == "x11"

def show_display_info():
    print(f"DS:{"x11" if is_x11() else os.environ["XDG_SESSION_TYPE"]}")
    de = os.environ["XDG_CURRENT_DESKTOP"] or "unknown"
    print(f"DE:{de}")
    if is_x11():
        X11Randr().show_info(True)

def main():
    parser = ArgumentParser()
    parser.add_argument("-v", "--version", dest="version", action="version", version=VERSION, help="Show program version")
    parser.add_argument("-i", "--info", dest="show_display_info", help="Show display info", action="store_true", default=False)
    parser.add_argument("-t", "--temp", dest="temperature", help="Temperature in kelvin", action="store", default=6500, type=int)
    parser.add_argument("-b", "--brightness", dest="brightness", help="Brightness from 0.1 to 1.0", action="store", default=1.0, type=float)
    parser.add_argument("-g", "--gamma", dest="gamma", help="Gamma from 0.1 to 1.0", action="store", default=1.0, type=float)

    args = parser.parse_args()
    
    if args.show_display_info:
        show_display_info()
        return
    
    args.brightness = min(max(0.0, args.brightness), 1.0)
    args.gamma = min(max(0.0, args.gamma), 1.0)
    
    if is_x11():
        X11Randr().set_temperature(args.temperature, args.brightness, args.gamma)
    else:
        sys.stderr.write("Display server %s not supported\n" % os.environ["XDG_SESSION_TYPE"])

if __name__ == "__main__":
    main()
