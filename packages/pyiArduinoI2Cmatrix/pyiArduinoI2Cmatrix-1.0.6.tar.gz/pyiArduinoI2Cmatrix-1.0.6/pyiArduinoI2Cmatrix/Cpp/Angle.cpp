// Данный пример постоянно поворачивает дисплей на 90°.    
#include "../iarduino_I2C_Matrix_8x8.h"                      
                                                            
uint8_t image[8] = {0b00111100,    //       ####
                    0b01111110,    //      ######
                    0b11001111,    //     ##  ####
                    0b10000110,    //     #    ##
                    0b10000000,    //     #
                    0b10000000,    //     #
                    0b01000000,    //      #
                    0b00100000};   //       #

iarduino_I2C_Matrix_8x8 disp;

void loop(void);

int main(int argc, char** argv)
{
	if (argc > 1)
		disp.changeBus(argv[1]);
	delay(500);
	disp.begin();
	disp.drawImage(image);
	for(;;)
		loop();
}

void loop()
{
	disp.angle(0);
	delay(100);
	disp.angle(90);
	delay(100);
	disp.angle(180);
	delay(100);
	disp.angle(270);
	delay(100);
}
