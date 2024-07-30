# cobi-redshift

A linux terminal application that change screen color temperature.

This is a re-implementation of [QRedshift](https://github.com/raphaelquintao/QRedshift) in python.
In contrast to the original, cobi-redshift currently only support XRandr, not XCB, due to the lack of python bindings for xcb.

## Features

- [x] X11 Support
- [ ] Wayland Support
- [ ] Different settings for each monitor

## Usage

Basic: `cobi_redshift -t [temperature in Kelvin] -b [bright] -g [gamma]`

Reset: `cobi_redshift`

| Parameter | Description                |
|-----------|----------------------------|
| -h        | Display this help          |
| -v        | Show program version       |
| -i        | Show display info          |
| -t 6500   | Temperature in kelvin      |
| -b 1.0    | Brightness from 0.1 to 1.0 |
| -g 1.0    | Gamma from 0.1 to 1.0      |

## Installation

Run this command: `sudo make install`
