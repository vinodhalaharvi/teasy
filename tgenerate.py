#===============================================================================
# Script provided by Vinod Halaharvi, email: vinod.halaharvi@gmail.com
# RTP Network Services, Inc. / 904-236-6993 ( http://www.rtpnet.net )
# DESCRIPTION: Simple templating engine 
#===============================================================================
import sys

__all__= ['TemplateHandler']

class TemplateHandler(object):

	"""docstring for TemplateHandler"""
	def __init__(self, ):
		super(TemplateHandler, self).__init__()
		self.evalString = ""

	def start(self, ch):
		"""docstring for start"""
		self.evalString = "" 

	def end(self, ch):
		"""docstring for end"""
		self.evalString = self.evalString[:-1]

	def add(self, ch):
		"""docstring for add"""
		self.evalString += ch

	def evaluate(self,):
		"""docstring for eval"""
		import sys
		from StringIO import StringIO
		buffer = StringIO()
		sys.stdout = buffer

		bases = ["object", ]
		className = "TemplateHandler"
		attributes = ["templateString","handler", ]
		methods = ["start", "end", "add",]

		c = compile(self.evalString, '<string>', 'exec')
		exec(c)
		sys.stdout = sys.__stdout__
		return (self.evalString, buffer.getvalue())


class EventDispatcher(object):

	"""docstring for EventDispatcher"""
	def __init__(self, templateString="", handler=None ):
		super(EventDispatcher, self).__init__()
		self.templateString = templateString
		self.handler = handler

	def getTemplatestring(self,):
		"""docstring for getTemplatestring"""
		return self.templateString

	def setTemplatestring(self, templateString):
		"""docstring for setTemplatestring"""
		self.templateString = templateString

	def parse(self, ):
		"""docstring for parse"""
		ch = prevch = ""
		for ch in self.templateString:
			if ch == '{' and prevch == '{':
				self.handler.start(ch)
			elif ch == '}' and prevch == '}':
				self.handler.end(ch)
				(evalString , replacement) = self.handler.evaluate()
				if not replacement:
					replacement = ""
				self.templateString = self.templateString.replace("{{%s}}" % evalString, replacement)
			else:
				self.handler.add(ch)
			prevch = ch 

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print "You need to provide at least one template file .. " 
		sys.exit(10)

	for templateFile in sys.argv[1:]:
		templateString = open(templateFile).read()
		b = EventDispatcher(templateString, TemplateHandler())
		b.parse()
		print b.getTemplatestring()


