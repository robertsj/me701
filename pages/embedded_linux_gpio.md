# Raspberry Pi and GPIOs

## Summary

Students will explore ways to connect to the physical world using the general-purpose
input/output (GPIO) pins.


## Resources

 - [`RPi.GPIO` documentation](https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/)

 You will want access to a pin map like this one:

 <img src="rpi_gpio.png">

![my caption](rpi_gpio.png)

##  Evidence of Student Learning

  - students will demonstrate working GPIO output using the led indicator
  - students will demonstrate working GPIO input using the caveman switch
  - students will demonstrate software PWM by using a low-cost voltage display

## Learning Plan


### Before Lecture

  - Prepare your "kit" for the day:
     
      1. RPiZ with loaded micro SD card
      2. micro-USB to USB-A cable (instructor has some)
      3. mini bread board

  -  Collect the following from the instructor before class starts:

      1. one LED
      2. one resistor
      3. one voltage indicator
      4. four male-to-female jumpers (or equivalent)

     We may need to share depending on attendance and my supplies!      

  - Skim the `RPi.GPIO` documentation linked above.  It's the easiest 
    way to use Python to control the GPIO, but it is quite limited.
    However, for our purposes, it's totally sufficient I think!

### During Lecture 

  0. Go over any issues with drivers and accessing the RPi0 via SSH and VNC.

  1. Connect your RPi0 and connect either by SSH or by VNC.  (With VNC, you can
     open the built-in text editor for some light coding.  For more development,
     you'll want to code off of the Pi and transfer via SSH, GitHub, etc.)

  2. Clone the [repository](https://github.com/me701/rpi_gpio_demo) for today on your RPi0.
  
  3. Do the things.


### After Lecture

   - [Video, Lecture, 12/01/2021](https://mediasite.k-state.edu/mediasite/Play/6b6e65d9ad6c4715867d602c03ff4c221d)  

### Jeremy's Notes

  We used most of the time to finish debugging the Pi connection.  Everyone should go through these exercises on their own time
  and be ready to demonstrate them next time.


