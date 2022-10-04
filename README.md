# Legend
## Sub Header
### Sub Sub Header
`variable text`

    Code inline

# Introduction 
TODO: Give a short introduction of your project. Let this section explain the objectives or the motivation behind this project. 
Welcome to the Quantum Next Generation 2022 Radar Challenge Beta Phase. I hope you are as excited to tinker with this as I was to build it.
The follow document will contain key information that will ensure the you have a thorough understanding about how the challenge works from a technical perspective and ensure that in the event of issue, the reasoning for it should be easy to understand and work around.
We are all proficient and smart, so let's do our best to aid each other in this process.

This module is a wrapper for the standard Python `request` package, taking standard HTTPS requests like `POST` and `GET` and doing the legwork of making it as accessible as possible.

This system of keeping the simulator online will allow us to have the core operations be hidden and ensure the fairness of this challenge.

# Getting Started
TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:

## Installation Process
This package can be imported into any python script and used with ease. Outlined in this readme will be the functions you need to call to invoke behviours in the simulator, and explanations about their parameters, their returns, and their place in the larger challenge.

To install this package simply place this file with your project and write this into your solution:

    import qe_radar

This will allow you to run the functions listed in `Documentation` that will easily help you engage with the server.

## Software Dependencies
As mentioned, the `qe_radar.py` is a preconfigured wrapper for the `request` module, which will need to be imported so you can engage with the simulator.

## Latest Releases
Version Number 0.2

# Documentation

## Development Phase

`dev_sim (pulse, detect, example)`
#### Example:
Running the development simulation against target `81` with a pulse that runs from `0 us` to `10 us` and measures from `3 us` to `7 us`.
```python
import qe_radar

pulse = [0,10]
detect = [3,7]

x = qe.radar.dev_sim(pulse, detect, 81)
# where x is a result between 0 and 1
```

`dev_data(example)`
Example:
    Where we want to find the actual info of the development target 1
```python
import qe_radar

x = qe.radar.dev_data(1)
# x is (Rabi Frequency [Mrad/s], Doppler shift of returned pulse [Mrad/s], Time of flight of pulse in us)
```

## Testing Phase

`test_sim`
Example:
    Running the assessed simulation against target 34 with a pulse that runs from 12us to 18us and measures from 13us to 17us.
```python
import qe_radar

pulse = [12,18]
detect = [13,17]

x = qe.radar.test_sim(pulse, detect, 34)
# where x is a result between 0 and 1
```

`test_score`
Example:
    Where we want to find the actual info of the development target 1
```python
import qe_radar

x = qe.radar.dev_data(1)
# x is (Rabi Frequency [Mrad/s], Doppler shift of returned pulse [Mrad/s], Time of flight of pulse in us)
```

## Leaderboard and Results


# Build and Test
TODO: Describe and show how to build your code and run the tests. 


# Examples


# Contribute
TODO: Explain how other users and developers can contribute to make your code better. 

If you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:
- [ASP.NET Core](https://github.com/aspnet/Home)
- [Visual Studio Code](https://github.com/Microsoft/vscode)
- [Chakra Core](https://github.com/Microsoft/ChakraCore)