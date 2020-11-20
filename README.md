# GymToolMan
A python script based on [splinter](https://github.com/cobrateam/splinter) and [schedule](https://github.com/dbader/schedule) to register open activities in UWaterloo CIF during the pandemic

## Install Dependencies

### Chrome WebDriver

Chrome WebDriver is provided by Selenium2. To use it, you need to install Selenium2 via pip:

```
$ [sudo] pip install selenium
```

It’s important to note that you also need to have Google Chrome installed in your machine.
In order to use Google Chrome with Splinter, you need to setup Chrome webdriver properly. You can follow the [official guide](https://splinter.readthedocs.io/en/latest/drivers/chrome.html#) to do setup.

#### Mac OS X:

```
$ brew cask install chromedriver
```

### Install splinter and schedule

```
$ pip install splinter
$ pip install schedule
```
## User Info
Replace username and password with your own WATIAM username and password

## Usage
```
$ python GymToolMan.py
```
To run the script in the background
```
$ nohup python GymToolMan.py &
```

Register periodically at pre-determined intervals, see [schedule docs](https://schedule.readthedocs.io/en/stable/)

Optional: Set the timer to `xx:59` to log in in advance so the registration can begin as soon as the timer hits the hour.
