# Quantum Error Correction Project – QEC for small to large systems
Philippe Noël, Alaisha Sharma, Nicolas Weninger
---

Installations (MacOS):
---
In order to be able to run quantum computations on your local device, you must download the required packages and set up your IBM Q experience account and API key. Make sure you have Python 3.4 or higher (required by QuTip). Then, make sure that you have pip installed and that it is up to date and run:
```
pip install qiskit
pip install qutip
pip install IBMQuantumExperience
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
Project Overview
---
We recreated and explored the curcuits as given in Quantum Error Correction for Beginners (Devitt et al.), specifically, the X and Z flip 3-qubit codes and the X and Z flip 9-qubit codes. We then used these error-corrected qubits as a basis to run the Deutsch-Josza algorithm and analyze the error frequencies between the error-corrected and non-error-corrected versions. Lastly, we experimented theoretically on a larger scale system which is too large to be ran on an actual quantum computer. We then exexuted our circuits as follows:

1. Run the theoretical simulation with a local quantum simulator as a control experiment.

2. Run the theoretical simulation with a local quantum simulator with an induced error.

3. Run the circuit on an IBM Q computer without the error correction in place.

4. Run the circuit on an IBM Q computer with the error corrction in place.

After demonstrating these simple errors for the individual X and Z flips, we have combined the error correction schemes to operate on both X and Z flips, following the same schema as above, and we have run an instance of the Deutsch-Joza algorithm with our error correction scheme on IBM Q's 16-qubit computer. This is the largest quantum computer we have access to, so all other work on our larger system has been theoretical and ran solely on the quantum simulator.
