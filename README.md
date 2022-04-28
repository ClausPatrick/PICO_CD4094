# PICO_CD4094
Shift register CD4094 to 7 segment display via MicroPython

All shift registers are daisy changed (DataIn to Q's) and last register's Q's is connected to a seperate red LED.
Mappings from typed values to binary values corresponding to the LEDs in the 7 segment are in cd_symbols dict and obviously only correspond to the specific displays used here (5011 BB) in CA. 
Class function write accepts int, float or str and will process decimal point. If a character is not found in the dictionary, the display will be set dark for this character.
Example will count to 10000, running through all integers on the display with varying brightness.
