from machine import Pin, Timer, I2C, PWM

cd_symbols = {'0': '00011000',
              '1': '11011110',
              '2': '00110100',
              '3': '10010100',
              '4': '11010010',
              '5': '10010001',
              '6': '00010001',
              '7': '11011100',
              '8': '00010000',
              '9': '10010000',
              'a': '01010000',
              'b': '00010011',
              'c': '00111001',
              'd': '00010110',
              'e': '00110001',
              '-': '11110111',
              'None': '11111111',
              '.': '11101111'}
    
class CD4094():
   
    def __init__(self, clock_pin=14, data_ping=13, strobe_pin=12, pwm_pin=15, pwm_freq=1000, pwm_duty=0xffff, number_of_ics=4):
        self.number_of_ics = number_of_ics
        self.cd_clock = Pin(clock_pin, Pin.OUT)
        self.cd_data = Pin(data_ping, Pin.OUT)
        self.cd_strobe = Pin(strobe_pin, Pin.OUT)
        self.cd_pwm = PWM(Pin(pwm_pin))
        self.cd_pwm.freq(pwm_freq)
        self.cd_pwm.duty_u16(pwm_duty)
        self.red = 0
        self.cd_strobe.value(0)
        
    def write(self, data=0, red=0, pwm_duty=0xffff):
        '''Translating data {str or int} into str of 0/1 and clock them into CD4094. 4 * 7 seg + d.p accounts for 32 values, + 1 for extra LED (red) for Q_s on last IC'''
        self.red = red
        self.cd_strobe.value(0)
        self.cd_pwm.duty_u16(pwm_duty)
        self.data_formated = '1' * 8 * self.number_of_ics + str(1-self.red) # Works as buffer and is prefilled to clear display in case len(data) < 4.
        for s in str(data):
            if s in cd_symbols:
                if s == '.':
                    data_list = list(self.data_formated)
                    data_list[-5] = '0' # Set decimal point.
                    self.data_formated = ''.join(data_list)
                else:
                    self.data_formated += cd_symbols[s]
            else:
                self.data_formated += cd_symbols['None']
        self.data_formated = self.data_formated[-(self.number_of_ics*8 + 1):]
        for d in self.data_formated:
            b = int(d)
            self.cd_clock.value(0)
            self.cd_data.value(b)
            self.cd_clock.value(1)
        self.cd_strobe.value(1)
        

def main():        
    cd = CD4094()
    counter = 0
    while True:
        cd.write(counter, red=1, pwm_duty = (0xffff//1))
        counter = (counter + 1) % 9999
        
    


# call main
if __name__ == '__main__':
    main()
