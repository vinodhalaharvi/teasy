### Sample Usage
	python tgenerate.py templatefile1 [more template files]

### Here is a simple template file
	class {{print className,}}({{print ", ".join([base for base  in bases]), }}):

		"""docstring for {{print className,}}"""
		def __init__(self,  {{print ", ".join([attribute for attribute  in attributes]), }}):
			super({{print className, }}, self).__init__()
	{{
	for attribute in  attributes: 
		print """\t\tself.%s = %s""" % (attribute , attribute)
	}}

	{{
	for method in  methods: 
		print '\t"""docstring for %s """' % method
		print """\tdef %s(self,):\n\t\tpass""" % method
		print
	}}


### Rendering the template in the way shown below 
	python tgenerate.py testTemplate.txt

### yields the following output below
	class TemplateHandler(object):

		"""docstring for TemplateHandler"""
		def __init__(self,  templateString, handler):
			super(TemplateHandler, self).__init__()
			self.templateString = templateString
			self.handler = handler


		"""docstring for start """
		def start(self,):
			pass

		"""docstring for end """
		def end(self,):
			pass

		"""docstring for add """
		def add(self,):
			pass
