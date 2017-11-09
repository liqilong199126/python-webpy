# python-webpy
python中的webpy框架搭建的小项目

- webpy框架只支持python2
- 下载源码后https://github.com/webpy/webpy/tarball/master 在命令行中运行 python2 setup.py install 安装成功

## URL映射
- URL完全匹配 

/index
- URL模糊匹配(不会传递给对应的处理函数)

/post/\d+
- URL带组匹配(传递给对应的处理函数)

/post/(\d+)



```
import web

urls = (
	'/index', 'index',
	'/blog/\d+', 'blog',
	'/(.*)', 'hello',
)
app = web.application(urls, globals())

class index:
	def GET(self):
		return 'index method'

class blog:
	def GET(self):
		return 'blog method'

	def POST(self):
		return 'blog post method'

class hello:
	def GET(self, name):
		return 'hello ' + name

if __name__=="__main__":
	app.run()
```

目录下运行 ```python2 url.py```

## 请求处理
![Snip20171109_3.png](https://i.loli.net/2017/11/09/5a03b7a9b8ad6.png)

- 请求参数获取

web.input()

- 请求头获取

web.ctx.env



```
import web

urls = (
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
		return open(r'request.html').read()

if __name__=="__main__":
	app.run()
```

目录下运行 ```python2 request.py```

## 响应处理

- 模板文件读取

render.index("参数")
- 结果数据获取

model.select("sql")
- URL跳转

web.seeother("/")

## 一个博客案例：https://github.com/sunchen009/chouyangblog


