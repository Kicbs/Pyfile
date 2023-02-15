'''import nmap
nm= nmap.PortScanner()
print(nm.scan('127.0.0.1','22-443'))
'''
'''
import numpy as np

arr = np.array([[1,2,3],[4,2,5]])
print('Array if of type: ', type(arr))


from cryptography.fernet import Fernet
key=Fernet.generate_key()
cipher_suite =Fernet(key)
cipher_text = cipher_suite.encrypt(b"Cyber Security")
plain_text = cipher_suite.decrypt(cipher_text)
print('Cipher generated: ',cipher_text)
'''
from cryptography.fernet import Fernet
key=Fernet.generate_key()
cipher_suite =Fernet(key)
cipher_text = cipher_suite.encrypt(b"Sumit Kumar")
print(cipher_text)