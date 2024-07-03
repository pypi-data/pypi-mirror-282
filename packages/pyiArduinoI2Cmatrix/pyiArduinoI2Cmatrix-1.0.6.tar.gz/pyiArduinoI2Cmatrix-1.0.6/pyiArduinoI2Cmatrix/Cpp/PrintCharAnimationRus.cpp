// Данный пример выводит символы на Русском языке и с анимацией.

#include "../iarduino_I2C_Matrix_8x8.h"
iarduino_I2C_Matrix_8x8 disp;

void loop(void);

int main(int argc, char** argv) 
{
	if (argc > 1)
		disp.changeBus(argv[1]);
	delay(500);
	disp.begin();
	disp.codingDetect("п");
	for (;;)
		loop();
}

void loop()
{
	disp.print("П", X8_FILLED_TOP);
	delay(300);
	disp.print("р");
	delay(300);
	disp.print("и");
	delay(300);
	disp.print("в");
	delay(300);
	disp.print("е");
	delay(300);
	disp.print("т");
	delay(300);
	disp.fillScr(X8_TOP);
}
