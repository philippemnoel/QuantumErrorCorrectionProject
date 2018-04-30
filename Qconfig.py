APItoken='ae5d442ca2080840aa5326539bc153d62bd0e8ee72860d49890b04b0fa7a64cba6b46565ee0b6643fa0832f268ea3ce99316e23fc47f0d03309e826b5862c3d5'
config = {"url": "https://quantumexperience.ng.bluemix.net/api"}
if APItoken is None:
    raise Exception("Please set your IBM Q access token in Qconfig.py")
