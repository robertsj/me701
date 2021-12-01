# Raspberry Pi and Embedded Linux

## Summary

Students will connect to a Raspberry Pi preconfigured with Raspberry Pi OS and 
navigate the embedded Linux operating system.



## Resources

 - Derek Malloy, *Exploring Raspberry Pi: Interfacing to the Real World with Embedded Linux*, Wiley (2016)
 - [Exploring Raspberry Pi - Companion Site](http://exploringrpi.com/)
 - [Raspberry Pi Software](https://www.raspberrypi.com/software/)
 - Search Youtube for Raspberry Pi

##  Evidence of Student Learning

  - Students will connect to the Raspberry Pi via SSH and blink the LED.
  - Students will connect to the Raspberry Pi desktop using the VNC Viewer.

## Learning Plan


### Before Lecture

  - Watch [this overview of Raspberry Pi](https://www.youtube.com/watch?v=EKPobkb1N6o)
    and this [related video](https://www.youtube.com/watch?v=p40OetppIDg) about the 
    differences between Rasperry Pi and Arduino.  Based on your knowledge of 
    Arduino (from ME 400, etc.) and the bit you now know about Raspberry Pi,
    what are the "pros" and "cons" for each board?

### During Lecture

  0. Acquire assigned "kit" that includes:

     - Raspberry Pi Zero W (RPi0)
     - 5V 2A power supply
     - Clear case
     - Micro SD card (and full-size adapter)
     - Micro-USB hub (OTG)
     - USB A (male-to-male) cable
     - Micro-USB to USB-A cable

     Install RPi0 in the provided case before moving on.

  1. Install the latest version of the Raspberry Pi OS on the Micro SD card.  Then, to enable the 
     use of "gadget" mode, edit the two files `config.txt` and `cmdline.txt` and create the `ssh` file
     as described [here for Windows](https://desertbot.io/blog/headless-pi-zero-ssh-access-over-usb-windows)
     and [here for Mac OS](https://desertbot.io/blog/ssh-into-pi-zero-over-usb).  For both Windows and
     Mac OS, you *may* need to install the RNDIS driver to support ethernet through the USB.  For Windows,
     [check this out](https://www.factoryforward.com/pi-zero-w-headless-setup-windows10-rndis-driver-issue-resolved/), 
     and for Mac OS, [try this](https://www.joshuawise.com/horndis).

  2. Connect RPi0 to laptop computer using the micro-USB to USB-A cable.   The data port (to connect to the hub) is toward the middle.

  3. **Optionally**, power the RPi0 with the included power supply.  The power port is toward the edge.
     I don't *think* this will hurt anything, but I've read that two voltage sources may be bad.  You definitely
     need the power supply for standalone deployment where the RPi0 needs access to the USB port for data, peripherals, etc.

  4. Open up a `bash` terminal.  The SD card has been configured to enable SSH and the "USB gadget" mode.  Hence,
     you should be able to log onto the RPi0 by executing:

     ```
     ssh pi@raspberrypi.local
     ```

     The default password is `raspberry`.


  5. List the names associated with and the "triggers" available for the on-board LED by executing:

     ```
     ls /sys/class/leds/led0/
     cat /sys/class/leds/led0/trigger
     ```

     (Which trigger is set?)

     Set the trigger to `none` by executing

     ```
     echo none |sudo tee /sys/class/leds/led0/trigger
     ```

     Then, turn the LED on by executing

     ```
     echo 255 |sudo tee /sys/class/leds/led0/brightness
     ```

     To turn it off, do the same with `0` in place of `255`.

  6. Finally, install [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) for your
     system.  For Windows machines, use the Windows version (not Linux).  Play around a bit.


### After Lecture

   - [Video, Lecture, 11/29/2021](https://mediasite.k-state.edu/mediasite/Play/3b2f017eec374e21b2e1ec1dc1ba89d81d)  

### Jeremy's Notes

   Lots of issues, of course, but I think the revisions above should fix most problems for most folks.