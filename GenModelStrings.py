#
# A short script to generate a xxModel.strings for a given xx.xcdatamodel file.
#
from objc import YES, NO, NULL
from Foundation import *
from CoreData import NSManagedObjectModel
from os import popen as system, rmdir, remove
from optparse import OptionParser
from tempfile import mkdtemp
import sys

MOMC_PATH = '/Developer/usr/bin/momc'

if __name__ == '__main__':
	parser = OptionParser(usage='Usage: %prog [options] model', conflict_handler='resolve')
	parser.add_option('-h', '--help', action='help', 
		help='show this help message and exit')
	parser.add_option('-o', '--output', dest='outfile', 
		metavar='OUTFILE', help='write output to <file> instead of stdout')
	parser.add_option('-m', '--momc', dest='momc', default=MOMC_PATH, 
		metavar='MOMC', help='path to the momc binary (defaults to /Developer/usr/bin/momc)')
	
	(options, args) = parser.parse_args()
	
	if len(args) < 1:
		parser.error('you must provide a .xcdatamodel file')
	
	if options.outfile is not None:
		outfile = open(options.outfile, 'w')
	else:
		outfile = sys.stdout
	
	tmp = mkdtemp()
	mom = tmp + '/model.mom'
	print mom
	system('%s %s %s' % (options.momc, args[0], mom))

	model = NSManagedObjectModel.alloc().initWithContentsOfURL_(NSURL.fileURLWithPath_(mom))
	remove(mom)
	rmdir(tmp)
	
	descriptors = [NSSortDescriptor.sortDescriptorWithKey_ascending_('name', YES)]
	entities = model.entities().sortedArrayUsingDescriptors_(descriptors)
	
	for anEntity in entities:
		entityName = anEntity.name()
		outfile.write('"Entity/%s" = "%s";\n' % (entityName, entityName))
		properties = anEntity.properties().sortedArrayUsingDescriptors_(descriptors)
		for aProperty in properties:
			propertyName = aProperty.name()
			outfile.write('"Property/%s/Entity/%s" = "%s";\n' % (propertyName, entityName, propertyName))
		outfile.write('\n')
