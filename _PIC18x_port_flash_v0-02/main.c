/*

Purpose: Flashes LED on RC0 of micro.
Micro: PIC18F252
Compiler: Hi-Tech C18 v8.12PL1 from www.htsoft.com
Author: Shane Tolmie of DesignREM Ltd.
Web: www.designrem.com

*/

#include <pic18.h>

#define PIC_CLK 3686400 //Mhz
//#define PIC_CLK 20000000 //Mhz

#if PIC_CLK<8000000
	__CONFIG(1, XT);
#elif PIC_CLK>=8000000
	__CONFIG(1, HS);
#else
	#warning PIC_CLK not defined properly
#endif

__CONFIG(2, PWRTDIS & WDTPS1 & WDTEN);
__CONFIG(4, STVRDIS);

#include "delay.c"

unsigned char var;

main()
{
  int c;
  c=0;

  TRISC=0;
  while(1) {
    RC0=1;
    DelayBigMs(250);
    RC0=0;
    DelayBigMs(250);
  }
}

