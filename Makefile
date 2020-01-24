
FLOPPIES := http://www.unixpc.org/3b1/floppies

unixpc-system.8.bdf: convert.py system.8.ft
	python -c 'import bdflib' 2>/dev/null || (cat NEED_BDFLIB && exit 1)
	python convert.py system.8.ft > /tmp/temporary-bdf
	cp /tmp/temporary-bdf $@

system.8.ft: fs/usr/lib/wfont/system.8.ft
	cp -p $< $@

font.h: fs/usr/include/sys/font.h
	cp -p $< $@

fs/usr/lib/wfont/system.8.ft: fs

fs: foundation.cpio development.cpio
	rm -rf fs-tmp
	mkdir -p fs-tmp
	fakeroot cpio -i -D fs-tmp -cmv --make-directories --no-preserve-owner -W none < foundation.cpio
	fakeroot cpio -i -D fs-tmp -cmv --make-directories --no-preserve-owner -W none < development.cpio
	mv fs-tmp fs

foundation.cpio:
	for n in 05 06 07 08 09 10 11 12; \
	 do curl $(FLOPPIES)/foundation/disk$$n; \
	 done > $@

development.cpio:
	for n in 01 02 03 04 05 06 07 08; \
	 do curl $(FLOPPIES)/utilities/development/disk$$n; \
	 done > $@
