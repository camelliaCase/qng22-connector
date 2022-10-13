# Technical Manual 
Version Number `0.3`

Welcome to the Quantum Next Generation 2022 Radar Challenge Beta Phase.
The follow document will contain key information that will ensure the you have a thorough understanding about how the challenge works from a coding perspective and ensure that in the event of issue, the reasoning for it should be easy to understand and work through.

This module is a wrapper for the standard Python `request` package, taking standard HTTPS requests like `POST` and `GET` and doing the legwork of making it as accessible as possible.

This system of keeping the simulator online will allow us to have the core logic be remote and ensure the fairness of this challenge.

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

# Valid Data Structures

## Radar Configurations (Pulse, Measurement, Example)
#### Variables
* Pulse | List
    * Start | Integer: 0-500000 us (microseconds)
    * End | Integer: 0-500000 us (microseconds)
* Measurement | List
    * Start | Integer: 0-500000 us (microseconds)
    * End | Integer: 0-500000 us (microseconds)
    * Phase | Float: radians
* Example Target | Integer: 0-999
```json
data: {
    "example": integer,
    "pulses": {
            "start": integer,
            "end": integer
    },
    "measurements": {
        "start": integer,
        "end": integer,
        "phase": float
    }
}
```
## Results (Configuration, Estimates)
#### Variables
* Configurations | List: 1000 size
    * Pulses | List: >1 size
        * Pulse | List: 2 size
            * Start | Integer: 0-500000 us (microseconds)
            * End | Integer: 0-500000 us (microseconds)
    * Measurements | List: >1 size
        * Measurement | List: 3 size
            * Start | Integer: 0-500000 us (microseconds)
            * End | Integer: 0-500000 us (microseconds)
            * Phase | Float: radians
    * Example Target | Integer: 0-999 
```json
data: {
    [
        "pulses": [
            "start": integer,
            "end": integer
        ],
        "measurements": [
            "start": integer,
            "end": integer,
            "phase": float
        ],
        "example": integer
    ]
}
```

#### Development vs Testing
In `qe_radar` there are two class objects that determine which simulator and dataset you will be targeting with any function - `DevSimulator` and `TestSimulator`
In `DevSimulator`, the example targets are known to you, and can be gathered using the `.dataset( int )` function. This is to encourage building and refining accurate models.
In `TestSimulator`, the example targets are unknown, this is because you will score on this dataset, and thus should only know how close you are on average to ensure it is your technique that is being measured, and not the replication of the actual data.

### Configuration

#### authentication(token)
Run this function before any other calls with the token assigned to your team, this will permit use of the simulator and allow your efforts to be correctly assigned to you.
```python
import qe_radar

sim = qe_radar.DevSimulator()
sim.authentication("5128uhn15adwaf421")
```
Or
```python
import qe_radar

sim = qe_radar.TestSimulator()
sim.authentication("5128uhn15adwaf421")
```

## Development Phase

Before using any function in the Development Simulator class, you must first create an object of it and assign your authentication token. All functions are then called from this created object. You can assign your authentication token during creation of the object by passing it as a parameter.
```python
simulator = qe_radar.DevSimulator("5128uhn15adwaf421")
```

### simulate(pulse, detect, example)
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
#### Example:
Finding the actual info of the development target `1`
```python
import qe_radar

radar = qe_radar.DevSimulator("5128uhn15adwaf421")

target_one = radar.dataset(1)
# target_one is (Rabi Frequency [Mrad/s], Doppler shift of returned pulse [Mrad/s], Time of flight of pulse in us)
```

### validate(config, score)
#### Example:
To provide advice to Teams on how they need to format their submission and if it their method produces a valid option.
```python
import qe_radar

radar = qe_radar.DevSimulator("5128uhn15adwaf421")

pulses = [[0,10],[10,15],[18,45]...]
detects = [[2,8],[14,15],[30,40]...]
examples = [0,1,2,3...]
configs = [pulses, detects, examples]

score = []

valid = radar.validate(configs, scores)
if valid:
    print("Configuration and Scores are valid")
else:
    print("Configuration and Scores are not valid")
```

## Testing Phase

Before using any function in the Test Simulator class, you must first create an object of it and assign your authentication token. All functions are then called from this created object. You can assign your authentication token during creation of the object by passing it as a parameter.
```python
simulator = qe_radar.TestSimulator("5128uhn15adwaf421")
```

### simulate(pulse, detect, example)
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
#### Example:
Scoring the accuracy of the test estimates while confirming that configuration is valid.
```python
import qe_radar

pulses = [[0,10],[10,15],[18,45]...]
detects = [[2,8],[14,15],[30,40]...]
examples = [0,1,2,3...]
configs = [pulses, detects, examples]

score = [] #need help with example data

radar = qe_radar.TestSimulator("5128uhn15adwaf421")

x = radar.score(configs, scores)
# x is [error code, accuracy average, error std for all three stats]
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