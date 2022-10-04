from urllib import request
import requests

#Test Data
test_pulse = [500,5000]
test_detect = [200, 2000, 1]
test_example = 0

URL = "https://qng22-sim.azurewebsites.net"
DEV = "/dev"
TEST = "/test"
BOARD = "/results"

auth = ""

#Directly calls dev_sim() in qe_radar
def dev_sim(pulse, detect, example):
    #creates JSON form data for HTTP request
    payload = {"pulsestart":pulse[0], "pulseend":pulse[1], "detectstart":detect[0], "detectend":detect[1], "phase":detect[2], "example":example}
    
    #sends data to site, stores in variable r
    r = requests.post(URL+DEV+"/sim",data=payload)

    #return to user the actual value of the request, removing header and online data that is unneeded
    return r.text

#Directly calls dev_data() in qe_radar
def dev_data(example):
    #creates JSON form data for HTTP request
    payload = {"example":example}

    #sends data to site, stores in variable r
    r = requests.post(URL+DEV+"/data",data=payload)

    #return to user the actual value of the request, removing header and online data that is unneeded
    return r.text


#Directly calls test_sim() in qe_radar
def test_sim(pulse, detect, example):
    #creates JSON form data for HTTP request
    payload = {"pulsestart":pulse[0], "pulseend":pulse[1], "detectstart":detect[0], "detectend":detect[1], "phase":detect[2], "example":example}
    
    #sends data to site, stores the returned result in variable r
    r = requests.post(URL+TEST+"/sim",data=payload)

    #return to user the actual value of the request, removing header and online data that is unneeded
    return r.text

#packages the two arrays, config and score into a post and sends to server to be validated
def test_score(complete_config, complete_score):
    payload = {"configs":complete_config, "scores":complete_score}

    r = requests.post(URL+TEST+"/score", data=payload)

    return r.text
    #needs to be setup to export as array

#Exists for Testing
#d = dev_sim(test_pulse, test_detect, test_example)
#print(d)

def set_auth(authstring):
    auth = authstring