import web
import MySQLdb
import MySQLdb.cursors

render = web.template.render('templates') 

urls = (
	'/article', 'article',
	'/index', 'index',
	'/blog/\d+', 'blog',
	'/(.*)', 'hello',
)
app = web.application(urls, globals())

class index:
	def GET(self):
		query = web.input()
		return query

class blog:
	def POST(self):
		data = web.input()
		return data

	def GET(self):
		return web.ctx.env
		
class hello:
	def GET(self, name):
		return render.test()

class article:
	def GET(self):
		conn = MySQLdb.connect(host='localhost', user='root', passwd='root', db='test', port=3306, cursorclass=MySQLdb.cursors.DictCursor)
		cur = conn.cursor()
		cur.execute('select * from articles')
		r = cur.fetchall()
		cur.close()
		conn.close()
		print r
		return render.article(r)

if __name__=="__main__":
	app.run()