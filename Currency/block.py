from cryptography.fernet import Fernet as F
from os.path import isfile


class Block:
	def __init__(self, index, data, time) -> None:
		self.index=index
		self.data=data
		self.time=time

	def Create_Block(self) -> None:
		block_of_string="{}<>{}<>{}".format(self.index, self.data, self.time)

		file=isfile(r"/home/senshimow/Desktop/key.key")

		if file:
			pass
		else:
			self.Create_Key()

		return block_of_string

	def Create_Key(self) -> None:
		key=F.generate_key()
		file=open(r"/home/senshimow/Desktop/key.key", 'w')
		file.write(key.decode())
		file.close()

	def Encrypt_Block(self, block_of_string) -> None:
		file=open(r"/home/senshimow/Desktop/key.key", 'r')
		key=file.read()
		file.close()

		encrypted_block=F(key.encode()).encrypt(block_of_string.encode())

		return encrypted_block, key

	def Check_If_Done(self, block_of_string, encrypted_block, key) -> None:
		decrypted_block=F(key.encode()).decrypt(encrypted_block).decode()

		if decrypted_block == block_of_string:
			self.index+=1
			return encrypted_block, True
		else:
			return "Failed Encryption", False
