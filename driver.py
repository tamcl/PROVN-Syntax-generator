import sys, os
# sys.path.append('.')
from library.provnGenerator import provnGenerator

output_filepath = './output'
try:
    os.mkdir(output_filepath)
except:
    pass

generator = provnGenerator()
generator.openDocument()
generator.prefix('ex', 'http://example.com/survey/')
generator.prefix('s', 'http://schema.org/')
Bob = generator.agent('ex', 'Bob')#, {'prov:type': 'prov:Person', 's:email':'example@example.com'})
generator.endDocument( path=output_filepath)
