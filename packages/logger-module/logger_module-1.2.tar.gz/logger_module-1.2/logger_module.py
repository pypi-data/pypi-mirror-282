__version__ = '1.2'


import os
import json
from datetime import datetime

class Logger_module:

	def __init__(self, log_file_path: str, component_name: str):
		self.log_file_path = log_file_path
		self.component_name = component_name

	def append_log(self, log_entry: dict):	
		log_dir = os.path.dirname(self.log_file_path)
		if not os.path.exists(log_dir):
			os.makedirs(log_dir)

		try:
			with open(self.log_file_path, "a+") as log_file:
				log_file.write(json.dumps(log_entry) + "\n")
				print(json.dumps(log_entry))
		except Exception as e:
			print(e)


	def log_status(self, status: str, message: str = ""):
		
		log_entry = {
			"timestamp": str(datetime.now()),
			"component": self.component_name,
			"status": status,
			"message": message
		}

		self.append_log(log_entry)
