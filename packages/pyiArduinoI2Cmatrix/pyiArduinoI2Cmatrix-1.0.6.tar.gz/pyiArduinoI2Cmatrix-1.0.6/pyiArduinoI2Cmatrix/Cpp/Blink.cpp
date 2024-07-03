// Данный пример заливает и стирает весь дисплей.

#include "../iarduino_I2C_Matrix_8x8.h"
iarduino_I2C_Matrix_8x8 disp;

void loop(void);

int main(int argc, char** argv)
{
	if (argc > 1)
		disp.changeBus(argv[1]);
	delay(500);
	disp.begin();
	loop();
}

void loop()
{
    while(true) {
        disp.fillScr();
	delay(1000);
        disp.clrScr();
	delay(1000);
    }
}
