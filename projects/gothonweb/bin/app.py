import web

urls = (
	'/hello', 'Index'
	)

app = web.application(urls, globals())

render = web.template.render('templates/', base = "layout")

class Index:
	def GET(self):
		return render.hello_form()

	def POST(self):
		form = web.input(name = "Nobody", greet = "Hello") # get data from the browser using 'input'
		#if form.greet:
		greeting = "%s, %s" % (form.greet, form.name)
		return render.index(greeting = greeting)
		#else:
		#	return "ERROR: greet is required"

if __name__ == "__main__":
	app.run()
