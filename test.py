from __future__ import print_function
import os
import struct

class FitFile(object):
	def __init__(self, pathname):
		self.pathname = pathname
		self._parse_header()

	def _parse_header(self):
		self.filesize = os.path.getsize(self.pathname)
		with open(self.pathname, 'rb') as f:
			header_bytes = f.read(12)
			self.header_size, self.fit_version, \
			self.profile_version, self.data_size, \
			self.data_type = struct.unpack('2BHI4s', header_bytes)

	def __repr__(self):
		return '%s byte %s file' % (self.data_size, self.data_type)


fitfiles = list()
for root, dirs, files in os.walk('data'):
	for name in files:
		fitfiles.append(FitFile(os.path.join(root,name)))
