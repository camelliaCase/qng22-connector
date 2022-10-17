# Technical Manual 
Version Number `0.5`

Welcome to the Quantum Next Generation 2022 Radar Challenge Beta Phase.
The follow document will contain key information that will ensure the you have a thorough understanding about how the challenge works through the use of this package.

The technical requirement of the challenge requires the user to connect to the simulator online to perform behaviours and analyse the dataset. This is achieved using REST and HTTP requests.

This file is a wrapper for the standard Python `request` package, taking standard HTTPS requests like `POST` and `GET` and doing the legwork of making it configured for the simulator as neatly as possible.

# Getting Started

## Installation Process
This package can be imported into any python script and used with ease. Outlined in this document will be the functions you need to call to invoke behviours in the simulator, explanations about their parameters, their returns, and their place in the larger challenge.

To install and use this package simply place this file with your project and input this into your solution:
```python
import qe_radar
```
This will allow you to run the functions listed in `Documentation` that will easily help you engage with the server.

## Software Dependencies
As mentioned, the `qe_radar.py` is a preconfigured wrapper for the `requests` module, which will need to be installed so you can engage with the simulator.
You can install `requests` using pip
```
python -m pip install requests
```

# Documentation

## Valid Variables and Data Structures

As outlined in the problem brief, the variables used will have certain restrictions and expectations. Listed below is a detailing of every variable, and can be used as reference for the later functions.

### Radar Configuration (Pulse, Measurement, Example)
* Pulse | List: Length 2
    * Start | Integer: 0-500000 us (microseconds)
    * End | Integer: 0-500000 us (microseconds)
* Measurement | List : Length 3
    * Start | Integer: 0-500000 us (microseconds)
    * End | Integer: 0-500000 us (microseconds)
    * Phase | Float: Radians
* Example Target | Integer: 0-999

Example Configuration for a pulse that runs from `2 us` to `13 us`, with a measurement window from `5 us` to `6 us`, adjusted by `2.1 radians` against target `1`:

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
        * Rabi |  Float: M/Rads
        * Detuning | Float: M/Rads
        * Time of Flight | Float: > 0 us (microseconds)
        * Example Target | Integer: 0-999

Example Results for development dataset, showing only a few items for Configurations and Estimates:

```python
    Configurations=[
        Example0=[
            Pulses=[
                [1, 20],[21, 100],[140, 500],[1000, 2000],[2000, 10000],...
            ],
            Measurements=[
                [10, 36],[45, 99],[100, 300],[400, 800],[5000, 25000],...
            ],
            Example=0
        ],
        #...Example 2 to Example 999
        Example1=[
            Pulses=[
                [1, 20],[21, 100],[140, 500],[1000, 2000],[2000, 10000],...
            ],
            Measurements=[
                [10, 36],[45, 99],[100, 300],[400, 800],[5000, 25000],...
            ],
            Example=1
        ],
        #...Example 2 to Example 999
    ],
    Estimates=[
        Example0=[
            0.00453748376016974, -0.02249823109292496, 153.73902434863788, 0
        ],
        Example1=[
            0.0002964523714059984, -0.015549490574576096, 643.6452780943542, 1
        ],
        Example2=[
            0.000541916391029567, -0.017939610742308935, 549.3026779212704, 2
        ],
        #...Example 3 to Example 999
    ]
```

#### Development vs Testing
In `qe_radar` there are two class objects that determine which simulator/dataset you will be targeting with any function - `DevSimulator` and `TestSimulator`
In `DevSimulator`, the example targets are known to you, and can be gathered using the `.dataset( int )` function. This is to encourage building and refining accurate models.
In `TestSimulator`, the example targets are unknown, this is because you will score on this dataset, and thus should only know how close you are on average to ensure it is your technique that is being measured, and not the replication of the actual data.


### Configuration

## Development Phase

Before using any function in the Development Simulator class, you must first create an object of it and assign your authentication token, as this will be parsed by the server as proof of access and assign your results to the leaderboard. All simulator functions are then called from this created object. You can assign your authentication token during creation of the object by passing it as a parameter.
```python
simulator = qe_radar.DevSimulator("5128uhn15adwaf421")
```

### authentication(token)
Run this function before any other calls with the token assigned to your team, this will permit use of the simulator and allow your efforts to be correctly assigned to you.
```python
import qe_radar

sim = qe_radar.DevSimulator()
sim.authentication("5128uhn15adwaf421")
```

### simulate(pulse, detect, example)

Send a radar configuration of pulse and measurement to the simulator and receive a normalised signal.

#### Example:
Running the development simulator against target `81` with a pulse that runs from `0 us` to `10 us` and measures from `3 us` to `7 us`.
```python
import qe_radar

radar = qe_radar.DevSimulator("5128uhn15adwaf421")

pulse = [0,10]
detect = [3,7]

print(radar.simulate(pulse, detect, 81))

>>> 0.455132
```

### dataset(example)

Get the Rabi, Detuning, and Time of Flight for the chosen example target.

#### Example:
Finding the details of the development target `1`
```python
import qe_radar

radar = qe_radar.DevSimulator("5128uhn15adwaf421")

print(radar.dataset(1))

>>> [0.0002964523714059984, -0.015549490574576096, 643.6452780943542]
```

### validate(config, score)
#### Example:

To provide Team's guidance on how they need to format their submission and if it their method produces a valid submission before the Testing stage.

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

Before using any function in the Test Simulator class, you must first create an object of it and assign your authentication token. All functions are then called from this created object. You can assign your authentication token during creation of the object by passing it as a parameter.
```python
simulator = qe_radar.TestSimulator("5128uhn15adwaf421")
```

### authentication(token)
Run this function before any other calls with the token assigned to your team, this will permit use of the simulator and allow your efforts to be correctly assigned to you.
```python
import qe_radar

sim = qe_radar.TestSimulator()
sim.authentication("5128uhn15adwaf421")
```

### simulate(pulse, detect, example)

Send a radar configuration of pulse and measurement to the simulator and receive a normalised signal.

#### Example:
Running the test simulator against target `34` with a pulse that runs from `12 us` to `18 us` and measures from `13 us` to `19 us`
```python
import qe_radar

radar = qe_radar.TestSimulator("5128uhn15adwaf421")

pulse = [12,18]
detect = [13,19]

print(radar.simulate(pulse, detect, 34))

>>> 0.455132
```

### score(config, estimates)

Submit Results with the configurations used to produce the estimates and the estimates for all targets in the testing dataset with intention for them to be scored. Returned results will be the mean accuracy across all targets, along with the standard deviation for the three values.

#### Example:
Scoring the accuracy of the test estimates while confirming that configuration is valid.
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

# Build and Test
TODO: Describe and show how to build your code and run the tests. 

```shell
python -m pip install virtualenv
activate
(venv) python -m pip install requests
```

# Contribute
TODO: Explain how other users and developers can contribute to make your code better. 

If you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:
- [ASP.NET Core](https://github.com/aspnet/Home)
- [Visual Studio Code](https://github.com/Microsoft/vscode)
- [Chakra Core](https://github.com/Microsoft/ChakraCore)