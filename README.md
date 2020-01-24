# unixpc-font-bdf
Convert the venerable AT&amp;T UNIX PC font to the modern BDF bitmap format

The `unixpc-system.8.bdf` font file that this tool produces has, for
your convenience, been committed to the root of this respoitory.  The
font makes your Linux terminal look charmingly like the classic UNIX
desktop machine of yore:

![An xterm using the UNIX PC font](screenshot.png?raw=true)

I want to thank Timothy Allen for his library
[bdflib](https://pypi.org/project/bdflib/)
which made this project not only possible but also fun.

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
