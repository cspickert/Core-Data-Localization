#
# A short script to generate a xxModel.strings for a given xx.xcdatamodel file.
#
from objc import YES, NO, NULL
from Foundation import *
from CoreData import *
from os import popen as system

MOMC = '/Xcode4/usr/bin/momc'

model_in = '/path/to/Model.xcdatamodel'
model_out = '/tmp/model.mom'
system('%s %s %s' % (MOMC, model_i, model_out))

model = NSManagedObjectModel.alloc().initWithContentsOfURL_(NSURL.fileURLWithPath_(model_out))
alphaSort = [NSSortDescriptor.sortDescriptorWithKey_ascending_('name', YES)]
for anEntity in model.entities().sortedArrayUsingDescriptors_(alphaSort):
	print '"Entity/%s" = "%s";' % (anEntity.name(), anEntity.name())
	for aProperty in anEntity.properties().sortedArrayUsingDescriptors_(alphaSort):
		print '"Property/%s/Entity/%s" = "%s";' % (aProperty.name(), anEntity.name(), aProperty.name())
	print
