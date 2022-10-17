from xmlrpc.client import Boolean
import requests

class DevSimulator (object):

    def __init__(self):
        self.token = ""
        self.URL = "https://qng22-sim.azurewebsites.net/dev"

    def authentication(self, token: str):
        """Updates the access token used by the simulator connector"""
        self.token = token

    def simulate(self, pulse: list[int], measure: list, example: int) -> float:
        """
        Runs the provided configuration into the simulator and returns a normalised signal as a float
        
        Keyword arguments:
        pulse -- paired list with start and end of pulse in us (0-500,000)
        measure -- list with start and end of the measurement window in us (0-500 000) and phase in radians
        example -- id of example chosen for the simulation (0-999)
        """
        #creates JSON form data for HTTP request
        payload = {"pulse":[pulse[0],pulse[1]], "measurement":[measure[0], measure[1], measure[2]]}
        
        #sends data to site, stores in variable r
        r = self.post(str(example), payload)

        #return to user the actual value of the request, removing header and online data that is unneeded
        return r.text

    #Directly calls dev_data() in qe_radar
    def dataset(self, example) -> list:
        """Requests the Rabi, Detuning, and Time of Flight for the chosen example target."""
        #sends data to site, stores in variable r
        r = self.get(str(example))

        #return to user the actual value of the request, removing header and online data that is unneeded
        return r.text

    def validate(self, configs: list, estimates: list) -> str:
        
        payload = {"configuration":configs, "estimates":estimates}

        r = self.post(payload, "/validate")
        return r.text

    def post(self, payload, ref=""):
        return requests.post(self.URL+ref, data=payload, headers={'Authorization': self.token})

    def get(self, ref=""):
        return requests.get(self.URL+ref, headers={'Authorization': self.token})

class TestSimulator(object):
    def __init__(self) -> None:
        self.token = ""
        self.URL = "https://qng22-sim.azurewebsites.net/test"

    def authentication(self, token: str):
        self.token = token

    def simulate(self, pulse: list[int], measure:list, example:int):
        #creates JSON form data for HTTP request
        payload = {"pulsestart":pulse[0], "pulseend":pulse[1], "measurestart":measure[0], "measureend":measure[1], "phase":measure[2], "example":example}
        
        #sends data to site, stores in variable r
        r = self.post(payload)

        #return to user the actual value of the request, removing header and online data that is unneeded
        return r.text

    def score(self, configs:list, estimates:int):
        payload = {"configuration":configs, "estimates":estimates}
        r = self.post(payload, "/score")

    def post(self, payload, ref=""):
        return requests.post(self.URL+ref, data=payload, headers={'Authorization': self.token})

    def get(self, ref=""):
        return requests.get(self.URL+ref, headers={'Authorization': self.token})