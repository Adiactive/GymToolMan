# GymToolMan
A python script based on [splinter](https://github.com/cobrateam/splinter) and [schedule](https://github.com/dbader/schedule) to register open activities in UWaterloo CIF during the pandemic

## Install Dependencies
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
