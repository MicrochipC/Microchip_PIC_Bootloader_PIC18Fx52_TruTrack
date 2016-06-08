/*

high level delay routines - see delay.h for more info.

Designed by Shane Tolmie of DesignREM.  Freely distributable.
Questions and comments to shane@keyghost.com
PICuWEB - Program PIC micros with C. Site has FAQ and sample source code. http://www.workingtex.com/htpic/

Designed for Microchip PIC18xxxx or PIC18Fxxx and Hi-Tech C.

Tested with PIC18F252 and simulator under MPlab.

Compiled with Hi-Tech C v8.12PL1.

*/

#ifndef __DELAY_C
#define __DELAY_C

#include <pic18.h>
#include	"always.h"

unsigned char delayus_variable;

#include	"dly18xxx.h"

void DelayBigUs(unsigned int cnt)
{
	unsigned char	i;

	i = (unsigned char)(cnt>>8);
	while(i>=1)
	{
		i--;
		DelayUs(253);
		CLRWDT();
	}
	DelayUs((unsigned char)(cnt & 0xFF));
}

void DelayMs(unsigned char cnt)
{
	unsigned char	i;
	do {
		i = 4;
		do {
			DelayUs(250);
			CLRWDT();
		} while(--i);
	} while(--cnt);
}

//this copy is for the interrupt function
void DelayMs_interrupt(unsigned char cnt)
{
	unsigned char	i;
	do {
		i = 4;
		do {
			DelayUs(250);
		} while(--i);
	} while(--cnt);
}

void DelayBigMs(unsigned int cnt)
{
	unsigned char	i;
	do {
		i = 4;
		do {
			DelayUs(250);
			CLRWDT();
		} while(--i);
	} while(--cnt);
}

void DelayS(unsigned char cnt)
{
	unsigned char i;
	do {
		i = 4;
		do {
			DelayMs(250);
			CLRWDT();
		} while(--i);
	} while(--cnt);
}

#endif


