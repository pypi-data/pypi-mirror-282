// Данный пример выводит изображения myImage_1 и myImage_2.
#include "../iarduino_I2C_Matrix_8x8.h"
//#include <cstdint>
#include <cstdlib>
#include <iostream>
typedef unsigned char byte;
                                                                 // Создаём изображение "смайлик".
byte myImage_1[8] = { 0b00111100,                                //                        ####
                      0b01000010,                                //                       #    #
                      0b10100101,                                //                      # #  # #
                      0b10000001,                                //                      #      #
                      0b10100101,                                //                      # #  # #
                      0b10011001,                                //                      #  ##  #
                      0b01000010,                                //                       #    #
                      0b00111100 };                              //                        ####
                                                                 // Создаём изображение "телевизор".
byte myImage_2[8] = { 0b01000100,                                //                       #   #
                      0b00101000,                                //                        # #
                      0b00010000,                                //                         #
                      0b11111111,                                //                      ########
                      0b10000011,                                //                      #     ##
                      0b10000011,                                //                      #     ##
                      0b10000011,                                //                      #     ##
                      0b11111111 };                              //                      ########
iarduino_I2C_Matrix_8x8 disp;

void loop(void);

int main(int argc, char** argv)
{
    if(argc > 1) {
	    disp.changeBus(argv[1]);
    }
    delay(500);
    disp.begin();
    for (;;) {
	    loop();
    }
}

void loop()
{
	disp.drawImage(myImage_1);
	delay(2000);
	disp.drawImage(myImage_2);
	delay(2000);
}
