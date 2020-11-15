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

Bob = generator.agent('ex', 'Bob',{'prov:type': 'prov:Person', 's:email':'example@example.com'})

analysis = generator.activity('ex', 'analysis')
surveying = generator.activity('ex', 'surveying')

dataset = generator.entity('ex','dataset')
results = generator.entity('ex', 'results')
survey_response = generator.entity('ex','survey_response',{'s:size':2})

generator.wasGeneratedBy(results, analysis)
generator.wasGeneratedBy(dataset, surveying)

generator.used(analysis,dataset)
generator.used(surveying, survey_response)

generator.wasAssociatedWith(analysis,Bob)

generator.wasInformedBy(analysis, surveying)

generator.endDocument( path=output_filepath)
