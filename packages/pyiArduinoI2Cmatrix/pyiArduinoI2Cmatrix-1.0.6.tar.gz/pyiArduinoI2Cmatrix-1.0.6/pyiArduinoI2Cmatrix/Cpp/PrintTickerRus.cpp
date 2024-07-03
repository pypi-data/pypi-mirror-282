// Данный пример выводит бегущую строку на Русском языке.

#include "../iarduino_I2C_Matrix_8x8.h"
iarduino_I2C_Matrix_8x8 disp;

int main(int argc, char** argv)
{
	if (argc > 1)
		disp.changeBus(argv[1]);
	delay(500);
	disp.begin();
	disp.codingDetect("п");
	disp.print("Unknown coding");
	if (disp.getCoding() == X8_TXT_CP866){
		disp.print("Данная программа использует кодировку CP866");
	}
	if (disp.getCoding() == X8_TXT_UTF8){
		disp.print("Данныя программа использует кодировку UTF-8");
	}
	if (disp.getCoding() == X8_TXT_WIN1251){
		disp.print("Данныя программа использует кодировку WIN1251");
	}

	disp.autoScroll(240, 1000);
}
