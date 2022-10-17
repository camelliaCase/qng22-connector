# Technical Manual 
Version Number `0.6`

Welcome to the Quantum Next Generation 2022 Radar Challenge Beta Phase.

The following document contains key information  to execute  the challenge through the use of this python package. 

The technical requirement of The Challenge requires the user to connect to the simulator online to analyse the dataset and perform activities. This is achieved using REST and HTTP requests. 

This file is a wrapper for the standard Python `requests` package, taking common HTTP requests like `POST` and `GET` and doing the groundwork to configure requests for the simulator.

# Getting Started

## Installation Process
This package can be imported into any python script using the standard `import` feature. This document outlines the functions you need to call to invoke functions in the simulator, explanations about their parameters, their returns, and their place in the challenge. 

To install and use this package place the qe_radar.py file with your project and input into your solution: 
```python
import qe_radar
```
This will allow you to run the functions listed in `Documentation` that will help you engage with the server.

## Software Dependencies
`qe_radar.py` is a preconfigured wrapper for the `requests` module, which will need to be installed so you can engage with the simulator.
You can install `requests` using `pip` or your choice of package manager.
```
python -m pip install requests
```

# Documentation

## Valid Variables and Data Structures

As outlined in the problem brief, the variables used will have certain restrictions and expectations. Listed below is the structure of every variable, and can be used as reference in the later functions.

### Radar Configuration (Pulse, Measurement, Example)
* Pulse | List: Length 2
    * Start | Integer: 0-500000 us (microseconds)
    * End | Integer: 0-500000 us (microseconds)
* Measurement | List: Length 3
    * Start | Integer: 0-500000 us (microseconds)
    * End | Integer: 0-500000 us (microseconds)
    * Phase | Float: Radians
* Example Target | Integer: 0-999

#### **Example**: 
Configuration for a pulse that runs from `2 us` to `13 us`, with a measurement window from `5 us` to `6 us`, adjusted by `2.1 radians` against target `1`:

    ([2, 13], [5, 6, 2.1], 1)


### Results (Configuration, Estimates)
* Configurations | List: Length 1000
    * Pulses | List: Length > 0
        * Pulse | List: Length 2
            * Pulse Start | Integer: 0-500000 us (microseconds)
            * Pulse End | Integer: 0-500000 us (microseconds)
    * Measurements | List: Length > 0
        * Measurement | List: Length 3
            * Measure Start | Integer: 0-500000 us (microseconds)
            * Measure End | Integer: 0-500000 us (microseconds)
            * Phase | Float: radians
    * Example Target | Integer: 0-999 
* Estimates | List: Length 1000
    * Estimate | List: Length 4
        * Rabi |  Float: $1/10^5$ to $4$ Mrads
        * Detuning | Float: -24 to 24 krads
        * Time of Flight | Float: 6 to 670 us (microseconds)
        * Example Target | Integer: 0-999


#### **Example**:
Results for development dataset, showing only a few items for configurations and estimates:
```python
Configurations=[
    Example0=[
        Pulses=[[1, 20],[21, 100],[140, 500],[1000, 2000],[2000, 10000]...],
        Measurements=[[10, 36],[45, 99],[100, 300],[400, 800],[5000, 25000]...],
        Example=0
    ],
    Example1=[
        Pulses=[[1, 20],[21, 100],[140, 500],[1000, 2000],[2000, 10000]...],
        Measurements=[[10, 36],[45, 99],[100, 300],[400, 800],[5000, 25000]...],
        Example=1
    ],
    #...Example 2 to Example 999
],
Estimates=[
    Example0=[0.00453748376016974, -0.02249823109292496, 153.73902434863788, 0],
    Example1=[0.0002964523714059984, -0.015549490574576096, 643.6452780943542, 1],
    Example2=[0.000541916391029567, -0.017939610742308935, 549.3026779212704, 2],
    #...Example 3 to Example 999
]
```

## Development vs Testing
In `qe_radar` there are two class objects that determine which simulator/dataset you will be targeting with any function - `DevSimulator` and `TestSimulator`
In `DevSimulator`, the example targets are known to you, and can be gathered using the `.dataset( int )` function. This is to develop a technique that gets as close as possible to that target.
In `TestSimulator`, the example targets are unknown,  and you will test your technique and solution to produce an estimate of the targets. Your estimates will be used to create your score and your configurations will be assessed for their validity. 

## Development Phase

Before using any function in the `DevSimulator` class, you must first initialise an object of it and assign your authentication token, as this will be parsed by the server as proof of access and used to assign your results to the leaderboard. All simulator functions are then called from this created object. You can assign your authentication token during creation of the object by passing it as a parameter.
```python
simulator = qe_radar.DevSimulator("5128uhn15adwaf421")
```

### `authentication(token)`
Running this function updates the token to access the simulator and record your results.
#### **Example**:
```python
import qe_radar

sim = qe_radar.DevSimulator()
sim.authentication("5128uhn15adwaf421")
```

### `simulate(pulse, detect, example)`

Send a radar configuration of pulse and measurement to the simulator and receive a normalised signal.

#### **Example**:
Running the development simulator against target `81` with a pulse that runs from `0 us` to `10 us` and measures from `3 us` to `7 us`.
```python
import qe_radar

radar = qe_radar.DevSimulator("5128uhn15adwaf421")

pulse = [0,10]
detect = [3,7]

print(radar.simulate(pulse, detect, 81))

>>> 0.455132
```

### `dataset(example)`

Get the Rabi (Mrads), Detuning (Mrads), and Time of Flight (us) for the chosen example target.

#### **Example**:
Finding the details of the development target `1`
```python
import qe_radar

radar = qe_radar.DevSimulator("5128uhn15adwaf421")

print(radar.dataset(1))

>>> [0.0002964523714059984, -0.015549490574576096, 643.6452780943542]
```

### `validate(config, score)`

To provide Team's guidance on how they need to format their submission and if it their method produces a valid submission before the Testing stage.
#### **Example**:
```python
import qe_radar

radar = qe_radar.DevSimulator("5128uhn15adwaf421")

configs = [[[[0,10],[10,15],[18,45]...], [[2,8,1.1],[14,15,0.32],[30,40,0.82]...], 0],
            [[[0,10],[10,15],[18,45]...], [[2,8,1.1],[14,15,0.32],[30,40,0.82]...], 1],
            [[[0,10],[10,15],[18,45]...], [[2,8,1.1],[14,15,0.32],[30,40,0.82]...], 2]...]

score = [[0.00453748376016974, -0.02249823109292496, 153.73902434863788, 0],
        [0.0002964523714059984, -0.015549490574576096, 643.6452780943542, 1],
        [0.000541916391029567, -0.017939610742308935, 549.3026779212704, 2]...]

valid = radar.validate(configs, scores)
if valid == 'valid':
    print("Configuration and Scores are valid")
else:
    print(valid)

>>> 'Configuration Invalid, incorrect number of configs and scores.'
```

## Testing Phase

Before using any function in the Test Simulator class, you must first initialise an object of it and assign your authentication token. All functions are then called from this created object. You can assign your authentication token during creation of the object by passing it as a parameter.
```python
simulator = qe_radar.TestSimulator("5128uhn15adwaf421")
```

### `authentication(token)`
Running this function updates the token to access the simulator and record your results. 
#### **Example**:
```python
import qe_radar

sim = qe_radar.TestSimulator()
sim.authentication("5128uhn15adwaf421")
```

### `simulate(pulse, detect, example)`

Send a radar configuration of pulse and measurement to the simulator and receive a normalised signal.

#### **Example**:
Running the test simulator against target `34` with a pulse that runs from `12 us` to `18 us` and measures from `13 us` to `19 us`
```python
import qe_radar

radar = qe_radar.TestSimulator("5128uhn15adwaf421")

pulse = [12,18]
detect = [13,19]

print(radar.simulate(pulse, detect, 34))

>>> 0.455132
```

### `score(config, estimates)`

Submit results with the configurations used to produce the estimates and the estimates for all targets in the testing dataset with intention for them to be scored. The returned results will be the mean score across the three values, along with the standard deviation each of the three values.

#### **Example**:
```python
import qe_radar

configs = [[[[0,10],[10,15],[18,45]...], [[2,8,1.1],[14,15,0.32],[30,40,0.82]...], 0],
            [[[0,10],[10,15],[18,45]...], [[2,8,1.1],[14,15,0.32],[30,40,0.82]...], 1],
            [[[0,10],[10,15],[18,45]...], [[2,8,1.1],[14,15,0.32],[30,40,0.82]...], 2]...]

score = [[0.00453748376016974, -0.02249823109292496, 153.73902434863788, 0],
        [0.0002964523714059984, -0.015549490574576096, 643.6452780943542, 1],
        [0.000541916391029567, -0.017939610742308935, 549.3026779212704, 2]...]

radar = qe_radar.TestSimulator("5128uhn15adwaf421")

print(radar.score(configs, scores))

>>> [45, 1.2, 4.2, 0.2]
```