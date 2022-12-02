# Technical Manual 
Version Number `1.5`


# IMPORTANT UPDATES

New features have been added to the Connector, along with numerous fixes that have been identified by teams participating in the challenge.
1. Mass Simulation Requests

It was a clear sticking point in the second Q&A and now for the final stretch of the challenge it is ready to go. Documentation for the new function has been added down below and can be run on either DevSimulator or TestSimulator using the `.mass_simulate()` function.

2. Mass Dataset Requests

While I was there I figured it would be faster to do this. You can now request the all `1000` dataset targets in one go rather than creating a loop and requesting each of the thousand, one at a time.

3. Fixes to test simulate, Google Colab, and other minor issues

Since the start of the challenge the connector has received many small changes to support requests of teams and to fix issues our own testing didn't catch. Downloading this most recent version will ensure that all identified issues are resolved.


# Introduction

Welcome to the Quantum Next Generation 2022 Radar Challenge

The following document contains key information  to execute  the challenge through the use of this python package. 

The technical requirement of The Challenge requires the user to connect to the simulator online to analyse the dataset and perform activities. This is achieved using REST and HTTP requests. 

This file is a wrapper for the standard Python `requests` package, taking common HTTP requests like `POST` and `GET` and doing the groundwork to configure requests for the simulator.

# Getting Started

Python Version Required: `3.9+` 

## Installation Process
This package can be imported into custom python script using the standard `import` feature. The documentation will outline the functions you need to call to invoke functions in the simulator, as well as providing explanations about their parameters, their returns, and their role in the challenge. 

To install and use this package, download/clone and place the qe_radar.py file within your project folder:
```bash
example-qng22-team-solution-folder
|   qng22-solution.py
|   qe_radar.py
```
 and input into your custom python script:
```python
import qe_radar
```
This will allow you to run the functions listed in `Documentation` that will help you engage with the simulation server.

## Software Dependencies
`qe_radar.py` is a preconfigured wrapper for the `requests` module, which will need to be installed so you can engage with the simulator.
You can install `requests` *(if you do not already have it)* using `pip` or your choice of package manager.
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

    [2, 13], [5, 6, 2.1], 1


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
            * Phase | Float: 0 to 2*pi radians
    * Example Target | Integer: 0-999 
* Estimates | List: Length 1000
    * Estimate | List: Length 4
        * Rabi |  Float: $1/10^4$ to $13$ Mrads
        * Detuning | Float: $-24$ to $24$ krads
        * Time of Flight | Float: $6$ to $335$ us (microseconds)
        * Example Target | Integer: 0-999


#### **Example**:
Results for development dataset, showing only a few items for configurations and estimates:
```python
Configurations=[
    Example0=[
        Pulses=[[Start=Int, End=Int]],
        Measurements=[[Start=Int, End=Int, Phase=Float]],
        ExampleID=Int
    ],
    Example1=[
        Pulses=[[Start=Int, End=Int]],
        Measurements=[[Start=Int, End=Int, Phase=Float]],
        ExampleID=Int
    ],
    #...Configuration for Example 2 to Example 999
],
Estimates=[
    Estimate0=[Rabi=Float, Detuning=Float, T_Flight=Float, ExampleID=Int],
    Estimate1=[Rabi=Float, Detuning=Float, T_Flight=Float, ExampleID=Int],
    Estimate2=[Rabi=Float, Detuning=Float, T_Flight=Float, ExampleID=Int],
    #...Estimate for Examples 3 to 999
]
```
```python
[
    [
        [[1, 20],[21, 100],[140, 500],[1000, 2000],[2000, 10000]...],
        [[10, 36, 0],[45, 99, 0],[100, 300, 0],[400, 800, 0],[5000, 25000, 0]...],
        0
    ],
    [
        [[1, 20],[21, 100],[140, 500],[1000, 2000],[2000, 10000]...],
        [[10, 36, 0],[45, 99, 0],[100, 300, 0],[400, 800, 0],[5000, 25000, 0]...],
        1
    ],
    #...Configuration for Example 2 to Example 999
],
[
    [0.00453748376016974, -0.02249823109292496, 153.73902434863788, 0],
    [0.0002964523714059984, -0.015549490574576096, 643.6452780943542, 1],
    [0.000541916391029567, -0.017939610742308935, 549.3026779212704, 2],
    #...Estimate for Examples 3 to 999
]
```

## Development vs Testing
In `qe_radar` there are two class objects that determine which simulator/dataset you will be targeting with any function - `DevSimulator` and `TestSimulator`
In `DevSimulator`, the example targets are known to you, and can be gathered using the `.dataset( int )` function. This is to develop a technique that gets as close as possible to that target.
In `TestSimulator`, the example targets are unknown,  and you will test your technique and solution to produce an estimate of the targets. Your estimates will be used to create your score and your configurations will be assessed for their validity. 

## Error Handling
In the event of fault, there should be an Exception raised from the code that if not accounted for, will break any recursive functions. This may not be the fault of the your own code, and clarity on what caused the issue will be noted in the text of the Exception. 
Speaking broadly for the underlying HTTP infrastructure being used, if it is a 4XX error code, then usually it is a failure of connection or compatability between the user and simulator. If it is a 500 error code, then it is a failure on the server end and an alert will be sent to the team to immediately rectify the fault.

## Development Phase

Before using any function in the `DevSimulator` class, you must first initialise an object of it and assign your authentication token, as this will be parsed by the server as proof of access and used to assign your results to the leaderboard. All simulator functions are then called from this created object. You can assign your authentication token during creation of the object by passing it as a parameter.
#### **Example**: Use your own token in place of the `ecc80c9e-025d-4b01-b748-37d98d24f4fb`
```python
simulator = qe_radar.DevSimulator("ecc80c9e-025d-4b01-b748-37d98d24f4fb")
```

### `authentication(token)`
Running this function updates the token to access the simulator and record your results.
#### **Example**:
```python
import qe_radar

dev_radar = qe_radar.DevSimulator()
dev_radar.authentication("[Replace this with your token]")
```

### `simulate(pulse, measure, example)`

Send a radar configuration of pulse and measurement to the simulator and receive a normalised signal.

#### **Example**:
Running the development simulator against target `81` with a pulse that runs from `0 us` to `10 us` and measures from `3 us` to `7 us` adjusted by phase 0.
```python
import qe_radar

dev_radar = qe_radar.DevSimulator("[Replace this with your token]")

pulse = [0,10]
measure = [3,7,0]

print(dev_radar.simulate(pulse, measure, 81))

>>> 0.455132
```

### `mass_simulate(configurations)`

Send a series of radar configurations for any number of example targets to be calculated concurrently, built to resolve issues found with high volume `simulate()` functions

#### **Example**:
Running the development simulator against targets `0`, `1` and `2` with a series of pulses and measurement windows. 
**Note**: If your pulse array and measurement array are not the same length, the target will be skipped and returned as an empty array.

*This uses the same structure as the configuration variable used for scoring.*


```python
import qe_radar

dev_radar = qe_radar.DevSimulator("[Replace this with your token]")

configurations = [[[[0,10],[10,15],[18,45]], [[2,8,1.1],[14,15,0.32],[30,40,0.82]], 0],
            [[[0,10],[10,15],[18,45]], [[2,8,1.1],[14,15,0.32],[30,40,0.82]], 1],
            [[[0,10],[10,15],[18,45]], [[2,8,1.1],[14,15,0.32],[30,40,0.82]], 2]
    ]

print (dev_radar.mass_simulate(configurations))

>>> [[[0.4862452504328871, 0.44162776172386153, 0.4698766184129937], 0],
        [[0.6225279509448354, 0.5342460580864783, 0.5543953308621907], 1],
        [[0.6180526680838897, 0.46747499721776037, 0.7819312044113694],2]]
```


### `dataset(example)`

Get the Rabi (Mrads), Detuning (Mrads), and Time of Flight (us) for the chosen example target.

#### **Example**:
Finding the details of the development target `1`
```python
import qe_radar

dev_radar = qe_radar.DevSimulator("[Replace this with your token]")

print(dev_radar.dataset(1))

>>> [0.0002964523714059984, -0.015549490574576096, 643.6452780943542]
```

### `mass_dataset()`

Get the Rabi (Mrads), Detuning (Mrads), and Time of Flight (us) for all `1000` example targets.

#### **Example**:
Finding the details of all the development targets
```python
import qe_radar

dev_radar = qe_radar.DevSimulator("[Replace this with your token]")

print(dev_radar.mass_dataset())

>>> [[0.028673456087970624, 0.020654261919863595, 114.56192252357387], [0.004362934265967196, 0.002677350985962326, 294.4095906800092], [8.695558202400441, -0.014455475799572943, 6.826695544782684], [0.0035707199667561473, 0.005648601112502126, 275.9207207606593], [0.00571397602555852, 0.018227046293772402, 300.03252768384533], [0.010949375111358607, 0.019777267521890768, 175.52652141984706], [0.104468109897097, -0.020920991278669906, 69.4709382036059]...
```

### `validate_config(configuration)`

To provide Team's guidance on how they need to format their submission and if their method produces a valid configuration list structure before submission in the Testing stage.

It does not confirm if the configuration list has all thousand (needed) entries or if estimates are formatted correctly.

#### **Example**:
```python
import qe_radar

dev_radar = qe_radar.DevSimulator("[Replace this with your token]")

configs = [[[[0,10],[10,15],[18,45]...], [[2,8,0],[14,15,0],[30,40,0]...], 0],
            [[[0,10],[10,15],[18,45]...], [[2,8,0],[14,15,0],[30,40,0]...], 2],
            [[[0,10],[10,15],[18,45]...], [[2,8,0],[14,15,0],[30,40,0]...], 1]...]

print(dev_radar.validate_config(configs))

>>> 'Submitted configurations are unordered'
>>> False
```

### `validate_estimate(estimates)`

To provide Team's guidance on how they need to format their submission and if their method produces a valid estimate list structure before submission in the Testing stage.

It does not confirm if the estimate list has all thousand (needed) entries or if configurations are formatted correctly.

#### **Example**:
```python
import qe_radar

dev_radar = qe_radar.DevSimulator("[Replace this with your token]")

estimates = [[0.00453748376016974, -0.02249823109292496, 153.73902434863788, 0],
        [0.0002964523714059984, -0.015549490574576096, 643.6452780943542, 2],
        [0.000541916391029567, -0.017939610742308935, 549.3026779212704, 1]...]


print(dev_radar.validate_estimate(estimates))

>>> 'Submitted estimates are unordered'
>>> False
```

## Testing Phase

Before using any function in the Test Simulator class, you must first initialise an object of it and assign your authentication token. All functions are then called from this created object. You can assign your authentication token during creation of the object by passing it as a parameter.

#### **Example**: Use your own token in place of the `ecc80c9e-025d-4b01-b748-37d98d24f4fb`
```python
simulator = qe_radar.TestSimulator("ecc80c9e-025d-4b01-b748-37d98d24f4fb")
```

### `authentication(token)`
Running this function updates the token to access the simulator and record your results. 
#### **Example**:
```python
import qe_radar

test_radar = qe_radar.TestSimulator()
test_radar.authentication("[Replace this with your token]")
```

### `simulate(pulse, measure, example)`

Send a radar configuration of pulse and measurement to the simulator and receive a normalised signal.

#### **Example**:
Running the test simulator against target `34` with a pulse that runs from `12 us` to `18 us` and measures from `13 us` to `19 us` adjusted by phase 0.
```python
import qe_radar

test_radar = qe_radar.TestSimulator("[Replace this with your token]")

pulse = [12,18]
measure = [13,19,0]

print(test_radar.simulate(pulse, measure, 34))

>>> 0.455132
```

### `mass_simulate(configurations)`

Send a series of radar configurations for any number of example targets to be calculated concurrently, built to resolve issues found with high volume `simulate()` functions

#### **Example**:
Running the test simulator against targets `0`, `1` and `2` with a series of pulses and measurement windows. 
**Note**: If your pulse array and measurement array are not the same length, the target will be skipped and returned as an empty array.

*This uses the same structure as the configuration variable used for scoring.*


```python
import qe_radar

test_radar = qe_radar.TestSimulator("[Replace this with your token]")

configurations = [[[[0,10],[10,15],[18,45]], [[2,8,1.1],[14,15,0.32],[30,40,0.82]], 0],
            [[[0,10],[10,15],[18,45]], [[2,8,1.1],[14,15,0.32],[30,40,0.82]], 1],
            [[[0,10],[10,15],[18,45]], [[2,8,1.1],[14,15,0.32],[30,40,0.82]], 2]
    ]

print (test_radar.mass_simulate(configurations))

>>> [[[0.4862452504328871, 0.44162776172386153, 0.4698766184129937], 0],
        [[0.6225279509448354, 0.5342460580864783, 0.5543953308621907], 1],
        [[0.6180526680838897, 0.46747499721776037, 0.7819312044113694],2]]
```

### `score(configurations, estimates)`

Submit results with estimates for all targets in the testing dataset and the configurations used to produce the estimates; with intention for them to be scored. The returned results will be Score (mean squared score with the success approaching 0), precision (standard deviations for Rabi, Detuning and Time of Flight) and accuracy (means for Rabi, Detuning and Time of Flight). If the submission is misconfigured the issues will be printed and score() will return None.

#### **Example**:
```python
import qe_radar

configs = [[[[0,10],[10,15],[18,45]...], [[2,8,0],[14,15,0],[30,40,0]...], 0],
            [[[0,10],[10,15],[18,45]...], [[2,8,0],[14,15,0],[30,40,0]...], 1],
            [[[0,10],[10,15],[18,45]...], [[2,8,0],[14,15,0],[30,40,0]...], 2]...]

estimates = [[0.00453748376016974, -0.02249823109292496, 153.73902434863788, 0],
        [0.0002964523714059984, -0.015549490574576096, 643.6452780943542, 1],
        [0.000541916391029567, -0.017939610742308935, 549.3026779212704, 2]...]

test_radar = qe_radar.TestSimulator("[Replace this with your token]")

print(test_radar.score(configs, estimates))

>>> [45, [1.2, 4.2, 0.2], [0.5, 2.1, 1.1]] # [ Score, [Precision (STD)], [Accuracy (Mean)] ]
```