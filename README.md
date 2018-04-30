# Quantum Error Correction Project
Philippe M. Noël, Alaisha Sharma, Nicolas Weninger
---

Installations (MacOS):
---
In order to be able to run quantum computations on your local device, you must download the required packages and set up your IBM Q experience account and API key. Make sure you have Python 3.4 or higher (required by QuTip). Then, make sure that you have pip installed and that it is up to date and run:
```
pip install qiskit
pip install qutip
```
You must now set up your IBM Q account (in order to run the calculations not only as quantum simulations but on the actual IBM quantum computers):

1. Create your IBM Q Experience account by going to the following link. Click on sign-in and if you dont have an account sign-up for one. https://quantumexperience.ng.bluemix.net/qx/experience

2. Once you have a verified account, go to My Account and then the Advanced tab. Under API Token if you see undefined click on Regenerate to create your token.

3. Now, go to your directory on your local machine and create a new python file called Qconfig.py.

4. For this step, you must have qiskit already installed. Refer to the instructions above if you have not yet installed qiskit. In your empty Qconfig.py file, paste the following code (replacing the text in the single quotes of APItoken by our own API token from your IBM Q account):
```
APItoken='replace_this_with_your_IBMQ_API_token'
config = {"url": "https://quantumexperience.ng.bluemix.net/api"}
if APItoken is None:
    raise Exception("Please set your IBM Q access token in Qconfig.py")
```

5. You are done! You can save the file and use "import Qconfig" in each notebook file that you use to run calculations on IBM Q. To make sure that it worked, you can create a new jupyter notebook, enter the following code and run the notebook. If you see your API token and the url above, you are good to go!:
```
from qiskit import QuantumCircuit, QuantumProgram
import Qconfig
print(Qconfig.APItoken, Qconfig.config['url'])
```
---







must update here








ES170 Final Project - Exploring quantum error correction for small to large systems
