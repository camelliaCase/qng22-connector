import requests

class DevSimulator (object):

    def __init__(self):
        self.token = ""
        self.URL = "https://qng22-sim.azurewebsites.net/dev"

    def authentication(self, token):
        self.token = token

    def simulator(self, pulse, detect, example):
        #creates JSON form data for HTTP request
        payload = {"pulse":[pulse[0],pulse[1]], "measurement":[detect[0], detect[1], detect[2]]}
        
        #sends data to site, stores in variable r
        r = self.post("/sim/"+example, payload)

        #return to user the actual value of the request, removing header and online data that is unneeded
        return r.text

    #Directly calls dev_data() in qe_radar
    def dataset(self, example):

        #sends data to site, stores in variable r
        r = self.get("/data/"+example)

        #return to user the actual value of the request, removing header and online data that is unneeded
        return r.text

    def validate(self, configs, estimates):
        
        payload = {"configuration":configs, "estimates":estimates}

        r = self.post("/validate", )
        return r.text

    def post(self, ref, payload):
        return requests.post(self.URL+ref, data=payload, headers={'Authorization': self.token})

    def get(self, ref, payload):
        return requests.get(self.URL+ref, data=payload, headers={'Authorization': self.token})

class TestSimulator(object):
    def __init__(self) -> None:
        self.token = ""
        self.URL = "https://qng22-sim.azurewebsites.net/test"

    def authentication(self, token):
        self.token = token

    def simulator(self, pulse, detect, example):
        #creates JSON form data for HTTP request
        payload = {"pulsestart":pulse[0], "pulseend":pulse[1], "detectstart":detect[0], "detectend":detect[1], "phase":detect[2], "example":example}
        
        #sends data to site, stores in variable r
        r = self.post("/sim", payload)

        #return to user the actual value of the request, removing header and online data that is unneeded
        return r.text

    def score(self, configs, estimates):
        payload = {"configuration":configs, "estimates":estimates}
        r = self.post("/score", payload)

    def post(self, ref, payload):
        return requests.post(self.URL+ref, data=payload, headers={'Authorization': self.token})

    def get(self, ref, payload):
        return requests.get(self.URL+ref, data=payload, headers={'Authorization': self.token})