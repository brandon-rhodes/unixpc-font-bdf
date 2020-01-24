#sccs	"@(#)uts/kern/sys:font.h	1.3"
/*
	Unix Window System
	Font/Icon Defintions

 */

#ifndef FONT_H
#define FONT_H

#include "sys/types.h"
#include "sys/iohw.h"

#define FMAGIC		0616		/* font file magic number	*/
#define NSFONTS		16		/* More system font slots than 
					per- window slots */
#define FNTSIZE		96		/* size of a font		*/
#define FNTBASE		32		/* first character		*/
#define FNSIZE		60		/* maximum font name size	*/

#define ICONSIZE	64		/* shorts in icon raster area 	*/

#ifdef KERNEL
/***** BEWARE:								*/
/*****		the fntdef and fcdef structures should not be changed	*/
/*****		without changing the raster text function (io/rastex.s)	*/
#endif

struct fcdef				/* font character definition	*/
{
	char		fc_hs;		/* horizontal size in bits	*/
	char		fc_vs;		/* vertical size		*/
	char		fc_ha;		/* horizontal adjust (signed)	*/
	char		fc_va;		/* vertical adjust (signed)	*/
	char		fc_hi;		/* horizontal increment		*/
	char		fc_vi;		/* vertical increment (optional)*/
	short		fc_mr;		/* relative mini-raster pointer	*/
};

struct fntdef
{
	long		ff_magic;	/* magic number			*/
	unsigned char	ff_flags;	/* flags			*/
	char		ff_hs;		/* nominal horizontal spacing	*/
	char		ff_vs;		/* nominal vertical spacing	*/
	char		ff_baseline;	/* pixel offset to baseline	*/
	char		ff_dummy[24];	/* round to 32 bytes		*/
	struct	fcdef 	ff_fc[FNTSIZE];	/* font control			*/
	unsigned short 	ff_raster;	/* raster data begins here	*/
};

struct ufdata				/* user font data		*/
{
	short		uf_slot;	/* slot number			*/
	char		uf_name[FNSIZE];/* font name (file name)	*/
};

struct icon				/* an icon			*/
{
	char		ic_flags;	/* flags			*/
	struct fcdef	ic_fc;		/* font def			*/
	unsigned short	ic_raster[ICONSIZE]; /* raster data		*/
};

struct wfont				/* Loaded fonts bookkeeping	*/
{
	struct	fntdef	*wf_ff;		/* ptr to font file header	*/
	short	wf_usecnt;		/* use count of font, 0=free	*/
	ino_t	wf_ino;			/* inode number of font file	*/
	time_t	wf_mtime;		/* modified time of font file	*/
	long	wf_size;		/* size of font file		*/
};

#endif FONT_H
