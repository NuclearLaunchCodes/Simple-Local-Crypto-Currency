from datetime import datetime
from Currency.block import Block

import socket


data={
	'Ben':0,
	'Brandon': 0,
	'Dawn': 0,
	'Jacob': 0,
	'Gwen': 0
}


class Block_Chain:
	def __init__(self) -> None:
		self.chain=[]
		self.current_data=[]
		self.index=0

	def Construct_Block(self) -> None:
		now=datetime.now()

		block=Block(index=self.index, data=self.current_data, time=now.strftime("%a %d %b %Y, %I:%M:%S%p"))

		block_of_string=block.Create_Block()
		encrypted_block, key = block.Encrypt_Block(block_of_string)
		encrypted_block_confirmed, is_done = block.Check_If_Done(block_of_string, encrypted_block, key)

		if is_done:
			data[self.current_data[0]['Name']]+=1
			self.chain.append(encrypted_block_confirmed)
			self.current_data.clear()
			return
		else:
			print(encrypted_block_confirmed)

	def New_Data(self, name) -> None:
		self.current_data.append({'Sender': socket.gethostbyname(socket.gethostname()), 'Name': name})
