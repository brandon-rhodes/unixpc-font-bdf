
unixpc-system.8.bdf: convert.py system.8.ft
	python -c 'import bdflib' 2>/dev/null || (cat NEED_BDFLIB && exit 1)
	python convert.py system.8.ft > $@

system.8.ft: fs/usr/lib/wfont/system.8.ft
	cp -p $< $@

fs/usr/lib/wfont/system.8.ft:
	mkdir -p fs
	(for n in 05 06 07 08 09 10 11 12; \
	 do curl http://www.unixpc.org/3b1/floppies/foundation/disk$$n \
	  | (cd fs; cpio -i -cmv --no-preserve-owner -W none); \
	 done)
