# RaspberryPiZero 2.13in Display
This projects uses a single RaspberryPi Zero (v1) and a Waveshare 2.13" display, both connected via soldered GPIO-Hat. Languages used will be Python (C also possible).

! Disclaimer: The libraries used here are not made by me. Those are the original library files from Waveshare (see below for sources). Any modifications will be annoted.

## Next Steps and Roadmap
- [x] Text Examples: show single and multiple line texts
- [x] Image Examples: show pictures and modify pictures before show
- [x] Draw Examples: draw lines, circles and rectangles
- [x] Simple Card: a digital vCard you can always carry along and show off
- [x] Slideshow: Show multiple slides in a row repeatingly
- [ ] Partial Display Updates: only update partial display parts instead the whole screen
- [x] digital vCard with multiple pages, sliding and QR Codes
- [x] start scripts with autostart while booting up
- [ ] get and show different RaspberryPi Stats

## Set up your RPi
For the 2.13" display the RaspberryPi Zero fits perfect as they match each others size quite well. 
With a proper cover you can get a nice display case you can place nearly everywhere without risking your hardware to get harmed. 

Install Raspbian or any other linux you like on your SD Card and set up your SSH connection. SSH will be the prefered way to connect up your RPi.
Working mainly on your home network, it can be handy to set up your pi with a local hostname like `raspberrypi.local` so you can reach it with `ssh username@raspberrypi.local` even if the RPis IP changes.

### Connect your display
If you got the display or display hat without pinheader you have to connect it by hand.
Pin connections can be viewed in `\py_lib\epdconfig.py` and here:
```
EPD    =>    Jetson Nano/RPI(BCM)
VCC    ->    3.3
GND    ->    GND
DIN    ->    10(SPI0_MOSI)
CLK    ->    11(SPI0_SCK)
CS     ->    8(SPI0_CS0)
DC     ->    25
RST    ->    17
BUSY   ->    24
```

## Use with python
### Install libraries
In order to access the display trough python you need some extra libraries:
```bash
sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install python3-pil
sudo pip3 install RPi.GPIO
```

### Basic and test use
The waveshare team already made some example code you can get from [Waveshare Github](https://github.com/waveshare/e-Paper) or look inside the `py_examples` folder (a small copy of the waveshare repo with changes).

To run a script simply type: `sudo python epd_2in9bc_test.py` and switch the file name to what you want to start.
 
## Use with C
You need to compile the program, this will generate the executable file. After that you can run the executable to start your programm
```bash
make
sudo ./epd
```

If you modify the program, you need to re-compile 
```bash
make clear
make
```

## Library Structure
- \c_lib\Config\: hardware interface layer files
- \c_lib\GUI\: basic image processing functions
- \c_lib\Fonts\: for some commonly used ascii fonts
- \c_lib\E-paper\: the ink screen driver functions

## Autostart
to autostart any of your programms you can choose between different options:
1. cron: set a crontab lik `@reboot python3 /home/user/vcard.py`
2. bashrc: add to your local bashrc: `python3 /home/user/vcard.py`

make sure to only start one programm that accesses your display!

## Sources
Display drivers and information from [Waveshare Wiki](https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT)

RaspberryPi Zero info from [raspberrypi.org/](https://www.raspberrypi.org/)