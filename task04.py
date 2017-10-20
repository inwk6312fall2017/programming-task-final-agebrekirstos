# import requests library
import requests

# import json library
import json

controller = 'sandboxapic.cisco.com'


# controller='devnetapi.cisco.com/sandbox/apic_em'

def getTicket():
    # put the ip address or dns of your apic-em controller in this url
    url = "https://" + controller + "/api/v1/ticket"

    # the username and password to access the APIC-EM Controller
    payload = {"username": "devnetuser", "password": "Cisco123!"}

    # Content type must be included in the header
    header = {"content-type": "application/json"}

    # Performs a POST on the specified url to get the service ticket
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)

    print(response)

    # convert response to json format
    r_json = response.json()

    # parse the json to get the service ticket
    ticket = r_json["response"]["serviceTicket"]

    return ticket


def getnetworkdevicecount(ticket):
	"""returns the network device count under the control of APIC-EM"""
	url = "https://" + controller + "/api/v1/network-device/count"

	# Content type as well as the ticket must be included in the header
	header = {"content-type": "application/json", "X-Auth-Token": ticket}

	# this statement performs a GET on the specified network device url
	response = requests.get(url, headers=header, verify=False)

	print("Number of Network Devices = ")
	#print(json.dumps(response.json(), indent=4, separators=(',', ': ')))

	r_json = response.json()
	print(r_json["response"])


theTicket=getTicket()
getnetworkdevicecount((theTicket))