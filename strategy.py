"""
This files crates strategy template

"""

from abc import ABCMeta, abstractmethod

class Strategy(object):

	__metaclass__ = ABCMeta


	@abstractmethod
	def handle_data():

		pass
