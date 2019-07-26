# the import section
import webapp2
import jinja2
import os
import random


# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# other functions should go above the handlers or in a separate file
def getSkin(tone):
	if tone == "tone1":
		skinTone = "https://cdn.glitch.com/5328b537-3bd7-4315-bf2d-b7a1dff7e629%2Fpixil-frame-0%20(19).png?v=1563989532432"

	elif tone == "tone2":
		skinTone = "https://cdn.glitch.com/5328b537-3bd7-4315-bf2d-b7a1dff7e629%2Fpixil-frame-0%20(18).png?v=1563989532387"

	elif tone == "tone3":
		skinTone = "https://cdn.glitch.com/5328b537-3bd7-4315-bf2d-b7a1dff7e629%2Fpixil-frame-0%20(20).png?v=1563989532476"

	return skinTone

def getHair(hair):
	if hair == "hair1":
		hairStyle = "https://cdn.glitch.com/5328b537-3bd7-4315-bf2d-b7a1dff7e629%2Fpixil-frame-0%20(4).png?1563989596036"

	elif hair == "hair2":
		hairStyle = "https://cdn.glitch.com/5328b537-3bd7-4315-bf2d-b7a1dff7e629%2Fpixil-frame-0%20(5).png?1563989596089"

	elif hair == "hair3":
		hairStyle = "https://cdn.glitch.com/5328b537-3bd7-4315-bf2d-b7a1dff7e629%2Fpixil-frame-0%20(7).png?1563989596228"

	elif hair == "hair4":
		hairStyle = "https://cdn.glitch.com/5328b537-3bd7-4315-bf2d-b7a1dff7e629%2Fpixil-frame-0%20(6).png?1563989596289"

	return hairStyle
	
def getShirt(shirt):	
	if shirt == "ss1":
		shirtType = "https://cdn.glitch.com/5328b537-3bd7-4315-bf2d-b7a1dff7e629%2Fpixil-frame-0%20(14).png?1563989596596"

	elif shirt == "ss2":
		shirtType = "https://cdn.glitch.com/5328b537-3bd7-4315-bf2d-b7a1dff7e629%2Fpixil-frame-0%20(12).png?1563989597155"

	elif shirt == "ss3":
		shirtType = "https://cdn.glitch.com/5328b537-3bd7-4315-bf2d-b7a1dff7e629%2Fpixil-frame-0%20(13).png?1563989597321"

	elif shirt == "ls1":
		shirtType = "https://cdn.glitch.com/5328b537-3bd7-4315-bf2d-b7a1dff7e629%2Fpixil-frame-0%20(15).png?1563989597240"

	elif shirt == "ls2":
		shirtType = "https://cdn.glitch.com/5328b537-3bd7-4315-bf2d-b7a1dff7e629%2Fpixil-frame-0%20(16).png?1563989597410"

	elif shirt == "ls3":
		shirtType = "https://cdn.glitch.com/5328b537-3bd7-4315-bf2d-b7a1dff7e629%2Fpixil-frame-0%20(17).png?1563989597530"

	return shirtType


def getPants(pants):
	if pants == "s1":
		pantsType = "https://cdn.glitch.com/5328b537-3bd7-4315-bf2d-b7a1dff7e629%2Fpixil-frame-0%20(9).png?1563989596347"

	elif pants == "s2":
		pantsType = "https://cdn.glitch.com/5328b537-3bd7-4315-bf2d-b7a1dff7e629%2Fpixil-frame-0%20(8).png?1563989596442"

	elif pants == "s3":
		pantsType = "N/A"

	elif pants == "j1":
		pantsType = "https://cdn.glitch.com/5328b537-3bd7-4315-bf2d-b7a1dff7e629%2Fpixil-frame-0%20(10).png?1563989596521"

	elif pants == "j2":
		pantsType = "https://cdn.glitch.com/5328b537-3bd7-4315-bf2d-b7a1dff7e629%2Fpixil-frame-0%20(11).png?1563989596680"

	elif pants == "j3":
		pantsType = "N/A" 

	return pantsType 

# the handler section
class MainHandler(webapp2.RequestHandler):
  	def get(self):
  		welcome_template = the_jinja_env.get_template('templates/welcome.html')
		self.response.write(welcome_template.render())

class AvatarHandler(webapp2.RequestHandler):
	def get(self):
		create_template = the_jinja_env.get_template('templates/avatar.html')
		self.response.write(create_template.render())

class ResultsHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hi!')

	def post(self):
		results_template = the_jinja_env.get_template('templates/results.html')
		skinTone = getSkin(self.request.get('Skin'))
		hairStyle = getHair(self.request.get('Hair'))
		shirtType = getShirt(self.request.get('Shirt'))
		print(self.request.get('Shirt'))
		pantsType = getPants(self.request.get('Pants'))
		avatar = {
		"avSkin": skinTone,
		"avHair": hairStyle,
		"avShirt": shirtType,
		"avPants": pantsType
		}
		self.response.write(results_template.render(avatar))


class QuizHandler(webapp2.RequestHandler):
	def get(self):
		quiz_template = the_jinja_env.get_template('templates/quiz.html')
		self.response.write(quiz_template.render())

class InfoHandler(webapp2.RequestHandler):
	def get(self):
		info_template = the_jinja_env.get_template('templates/info.html')
		self.response.write(info_template.render())
		


# the app configuration section	
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', MainHandler),
  ('/avatar', AvatarHandler),
  ('/quiz', QuizHandler),
  ('/results', ResultsHandler),
  ('/info', InfoHandler)
  ], debug=True)