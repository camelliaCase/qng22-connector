Version Number `0.3`

# Introduction 
Welcome to the Quantum Next Generation 2022 Radar Challenge Beta Phase. I hope you are as excited to tinker with this as I was to build it.
The follow document will contain key information that will ensure the you have a thorough understanding about how the challenge works from a technical perspective and ensure that in the event of issue, the reasoning for it should be easy to understand and work around.
We are all proficient and smart, so let's do our best to aid each other in this process.

This module is a wrapper for the standard Python `request` package, taking standard HTTPS requests like `POST` and `GET` and doing the legwork of making it as accessible as possible.

This system of keeping the simulator online will allow us to have the core operations be hidden and ensure the fairness of this challenge.

# QA and Security Testers [Section Removed From Production]
Until the launch of the Challenge, the server will be running in several stages to isolate and develop the core components of the code.

1. INFRASTRUCTURE - Azure Web Services, V.Net, MySQL Database, Backups and Scalablity
2. DEVELOPMENT PHASE - HTTPS, Token Access, Simulator Load Testing, Record Keeping `<- WE ARE HERE`
3. TEST PHASE - HTTPS, Token Access, Simulator Load Testing, Record Keeping, Scoring, Validation
4. SITE-SIM CONNECTION - Site-Sim Account Sync, Leaderboard
5. NICE TO HAVE - Past Activities via Site, See other Team score breakdowns

Testers, Trialers and Security Assessors are encouraged to pursue and hammer, pull, overload, or pry at any of the components in the current and past stages. Progression should occur rather quickly along the stages, and this GitHub will remain updated with the latest released version and the ReadMe will be changed accordingly.

Dummy token data will be listed at the bottom of this section.

## Stage 1 - INFRASTRUCTURE

The entire Challenge is hosted in Microsoft Azure Web App Services, with two containers for the WordPress site (https://qng22.azurewebsites.net) and the Simulator (https://qng22-sim.azurewebsites.net). A third instance is created to host the MySQL server that will be handling the content for WordPress. This is so accounts share a single source for both instances, and the data in the simulator can be read eventually by the website for features like the Leaderboard.

## Stage 2 - DEVELOPMENT PHASE `<- WE ARE HERE`
The site will be populated with dummy user and authentication data, and the only active connection points will be the development data set and the development simulator, this is to recreate the first half of the challenge, and to assess potential issues with load, record keeping, or the client side code.

## Stage 3 - TESTING PHASE
The connectors will be turned on for the Test side of the challenge, allowing the client code to access the Testing Simulator and use the scoring/validation functions. This will continue to use the dummy login data and tokens from Phase 2

## Stage 4 - SITE-SIM CONNECTION
This will replace the dummy access data that remains isolated to the simulator and instead use login data shared between the WordPress and Simulator. Users at this stage can create an account, generate a key, reset their password, and generate another key. This will ensure user privacy can be secured by the user. Additionally data that has been kept by the simulator can now be read by the site and will produce a live leaderboard based on the scores input into the Database.

## Stage 5 - NICE TO HAVE
These are various activities that will allow users and the site to read select data from the database to create a more dynamic experience, will be expounded upon later.


## DUMMY AUTHENTICATION

### Alpha
Token: 

### Bravo
Token: 

### Charlie
Token: 

### Delta
Token: 

### Echo
Token: 

### Foxtrot
Token: 


# Getting Started

1. Understand the Challenge
2. Read FAQ and Resources
3. Download Python Package and Technical Guide
4. Develop your solution using the simulator
5. Test and validate your results
6. Submit your results
7. Pitch your solution

## Installation Process
This package can be imported into any python script and used with ease. Outlined in this readme will be the functions you need to call to invoke behviours in the simulator, explanations about their parameters, their returns, and their place in the larger challenge.

To install this package simply place this file with your project and input this into your solution:
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
#### Development vs Testing
In `qe_radar` there are two prefixes that determine which dataset you will be targeting with any function.
`dev` and `test`
In `dev`, the example targets are known to you, and can be gathered using the `dev_data()` function. This is to encourage building and refining accurate models.
In `test`, the example targets are unknown, this is because you will score on this dataset, and thus should only know how close you are on average to ensure it is your technique that is being measured, and not the replication of the actual data.

### Configuration
#### set_auth(token)
Run this function before any other calls with the token assigned to your team, this will permit use of the simulator and allow your efforts to be correctly assigned to you.
```python
import qe_radar

qe_radar.set_auth("5128uhn15adwaf421")
```

## Development Phase

### dev_sim (pulse, detect, example)
#### Example:
Running the development simulation against target `81` with a pulse that runs from `0 us` to `10 us` and measures from `3 us` to `7 us`.
```python
import qe_radar

pulse = [0,10]
detect = [3,7]

x = qe_radar.dev_sim(pulse, detect, 81)
# where x is a result between 0 and 1
```

### dev_data(example)
#### Example:
Finding the actual info of the development target `1`
```python
import qe_radar

x = qe_radar.dev_data(1)
# x is (Rabi Frequency [Mrad/s], Doppler shift of returned pulse [Mrad/s], Time of flight of pulse in us)
```

### dev_score(config, score)
#### Example:
To provide an accuracy measurement for Teams so they can understand the scoring system and how they need to format their submission.
```python
import qe_radar

pulses = [[0,10],[10,15],[18,45]...]
detects = [[2,8],[14,15],[30,40]...]
examples = [0,1,2,3...]
configs = [pulses, detects, examples]

score = [] #need help with example data

x = qe_radar.test_score(configs, scores)
# x is [error code, accuracy average, error std for all three stats]

x = qe_radar.dev_score()
```

## Testing Phase

### test_sim(pulse, detect, example)
#### Example:
Running the assessed simulation against target `34` with a pulse that runs from `12 us` to `18 us` and measures from `13 us` to `17 us`.
```python
import qe_radar

pulse = [12,18]
detect = [13,17]

x = qe_radar.test_sim(pulse, detect, 34)
# where x is a result between 0 and 1
```

### test_score(config, score)
#### Example:
Scoring the calculated test and ensuring config is accurate.
```python
import qe_radar

pulses = [[0,10],[10,15],[18,45]...]
detects = [[2,8],[14,15],[30,40]...]
examples = [0,1,2,3...]
configs = [pulses, detects, examples]

score = [] #need help with example data

x = qe_radar.test_score(configs, scores)
# x is [error code, accuracy average, error std for all three stats]
```

# Build and Test
TODO: Describe and show how to build your code and run the tests. 

```shell
python -m pip install virtualenv
activate
(venv) python -m pip install requests
```

Currently planned here is a step by step first time config with installation of python, installation of modules like venv/virtual environment, running venv, and installation of dependent files like requests

Additionally, I would like to list the process of opening, saving and closing the project, since most tutorials treat that as common knowledge.

# Contribute
TODO: Explain how other users and developers can contribute to make your code better. 

If you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:
- [ASP.NET Core](https://github.com/aspnet/Home)
- [Visual Studio Code](https://github.com/Microsoft/vscode)
- [Chakra Core](https://github.com/Microsoft/ChakraCore)