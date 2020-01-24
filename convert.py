#!/usr/bin/env python
#
# This font is designed for pixels which are each a tall rectangle with
# an aspect ratio x:y of roughly 0.84 (approx 6/7 or 5/6 or 4/5).

from __future__ import print_function

import argparse
import bdflib
import bdflib.model
import bdflib.writer
import sys
from struct import calcsize, unpack

# https://tech-insider.org/unix/research/acrobat/8605.pdf
UNIXPC_X_PIXELS = 720
UNIXPC_Y_PIXELS = 348

# A review of the UNIX PC asserted its display was Apple IIe sized, so:
# https://groups.google.com/forum/#!topic/comp.emulators.apple2/YUsAV1BX1Ks
# I have no idea whether these are accurate measurements of the area of
# the screen surface on which pixels displayed, though.
WIDTH_INCHES = 9.0
HEIGHT_INCHES = 6.5

DPI_X = UNIXPC_X_PIXELS / WIDTH_INCHES
DPI_Y = UNIXPC_Y_PIXELS / HEIGHT_INCHES

def main(argv):
    parser = argparse.ArgumentParser(description='Convert UNIX PC font to bdf')
    parser.add_argument('path', help='path to an .ft font file')
    args = parser.parse_args(argv)

    with open(args.path, 'rb') as f:
        data = f.read()

    fmt = '>IBbbb'
    magic, flags, font_hs, font_vs, baseline = unpack(fmt, data[:calcsize(fmt)])
    assert magic == 0o616

    msg('Width and height in pixels: {}x{}'.format(font_hs, font_vs))
    msg('Pixel offset to baseline: {}'.format(baseline))
    msg('Approximate DPI (x y): {} {}'.format(DPI_X, DPI_Y))

    scale = 2

    name = '-unixpc-system-medium-r-normal-12-120-100-100-m-100-iso8859-1'
    pointsize = int(font_vs / DPI_Y * 72.0)
    font = bdflib.model.Font(name, pointsize, DPI_X / scale, DPI_Y)

    fmt = '>bbbbbbh'
    size = calcsize(fmt)
    assert size == 8

    for i in range(96):
        offset = 32 + i * size
        block = data[offset:offset + size]
        hs, vs, ha, va, hi, vi, mr = unpack(fmt, block)
        msg(repr(chr(i+32)), hs, vs, ha, va, hi, vi, mr)

        input_width = 2
        fmt2 = '>h'
        output_width = (hs + 3) // 4  # how many hex digits

        j = mr + offset + size - 2
        glyph_data = []

        for y in range(vs):
            bytelist = data[j : j+input_width]
            n, = unpack(fmt2, bytelist)
            n = flip(n, hs)
            n = n << (output_width * 4) - hs
            h = hex(n)[2:]
            h = h.zfill(output_width)
            for si in range(scale):
                glyph_data.append(h)
            j += input_width

        font.new_glyph_from_data(
            name=b'ASCII CHARACTER {}'.format(chr(i + 32)),
            data=glyph_data,
            bbX=ha,
            bbY=(-va - vs) * scale,
            bbW=hs,
            bbH=vs * scale,
            advance=hi,
            codepoint=i + 32,
        )

    bdflib.writer.write_bdf(font, sys.stdout)

BIG = 2 ** 60  # added before running bin() to avoid negative numbers

def flip(n, width):
    """Reverse the binary digits of integer `n`, which is `width` bits wide."""
    s = bin(BIG + n)[-width:]
    #msg(s)
    return int(s[::-1], 2)

def msg(*args):
    print(*args, file=sys.stderr)

if __name__ == '__main__':
    main(sys.argv[1:])
