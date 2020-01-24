# The UNIX PC 3B1 system font, for modern computers

Convert the venerable AT&amp;T UNIX PC font to the modern BDF bitmap format

The `unixpc-system.8.bdf` font file that this tool produces has, for
your convenience, been committed to the root of this respoitory.  The
font makes your Linux terminal look charmingly like the classic UNIX
desktop machine of yore:

![An xterm using the UNIX PC font](screenshot.png?raw=true)

I want to thank Timothy Allen for his library
[bdflib](https://pypi.org/project/bdflib/)
which made this project not only possible but also fun.

## Studying the UNIX PC base filesystem

The `Makefile` in this directory can not only build the font file, but
also offers a few intermediate targets that might interest fans of the
old UNIX PC:

* `make fs` downloads the UNIX PC 3B1 "Foundation Set" and "Development
  Set" diskettes from `www.unixpc.org` and extracts them into the
  directory `fs`, giving you a base UNIX PC filesystem to browse right
  on your modern machine.

* `make font.h` copies into the repository root the C header file that
  defines the UNIX PC binary `.ft` font file format, in case you want to
  study it yourself.

* `make foundation.cpio` and `make development.cpio` download the raw
  floppy diskette contents without extracting them to a local directory,
  in case the raw CPIO archives are of more use to you.

## Other fonts

If you want to study the other fonts that came with the UNIX PC, run
`make fs` as described above, and then look inside the filesystem image:

```
$ ls -l fs/usr/lib/wfont/
```

You will find terminal fonts, several fonts offering special characters
and drawing characters, and large-format fonts with much more detail
than the basic 9x12 pixel font that the UNIX PC used by default.  You
can use the conversion program to turn any of them into a modern BDF
file:

```
$ python convert.py fs/usr/lib/wfont/PLAIN.R.E.24.A > tmp.bdf
```

## Design note

Pixels on the UNIX PC screen were not square: they were tall rectangles.
This means that the UNIX PC 9x12 terminal font did not, in fact, display
squarish little characters with a 3:4 aspect ratio, but taller and more
elegant characters.

To simulate their appreance on a modern display where pixels are
squares, the `convert.py` script sets an internal value `scale = 2` that
produces 2 rows of pixels for every 1 input row of pixels.  While this,
strictly speaking, produces an error in the other direction by making
the letters stretch taller than they would have on the UNIX PC, the
result is visually more beautiful and more readable.

If someone were to convert the font into a scalable format, then
experiments could be made with intermediate ratios that even more
closely matched the UNIX PC display.  But I am happy enough with the
double-height version of the font and am not at this point planning
further experiments.
