// Данный пример заливает и стирает весь дисплей с анимацией.

#include "../iarduino_I2C_Matrix_8x8.h"
iarduino_I2C_Matrix_8x8 disp;

void loop(void);

int main(int argc, char** argv)
{
	if (argc > 1)
		disp.changeBus(argv[1]);
	delay(500);
	disp.begin();
	for(;;) {
		loop();
	}
}

void loop(){
	disp.fillScr(X8_RIPPLES);
	delay(1000);
	disp.clrScr (X8_RIPPLES);
	delay(1000);
	disp.fillScr(X8_DOWN);
	delay(1000);
	disp.clrScr (X8_DOWN);
	delay(1000);
	disp.fillScr(X8_TOP);
	delay(1000);
	disp.clrScr (X8_TOP);
	delay(1000);
}
