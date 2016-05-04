1.添加Moss_html和Moss_static文件夹：
	1.修改private_project/settings.py
		1.1TEMPLATES 中的 DIRS 为 [BASE_DIR+"/Moss_html",BASE_DIR+"/Moss_static",],
	
2.创建index首页
	1.创建Moss_html/index.html
	2.创建private_project/view_index.py
	3.修改private_project/urls.py
		3.1 添加from private_project.view_index import hello引入 hello方法
		3.2 url("^$", hello),在http://127.0.0.1:8000/调用hello函数，返回index.html
		
3.创建cafe界面
	1.创建Moss_html/cafe.html
	2.创建private_project/view_cafe.py
	3.修改private_project/urls.py
		3.1 添加from private_project.view_cafe import cafe
		3.2 url("^cafe", cafe),
		
4.创建模板
	1.创建Moss_templates
		1.1修改TEMPLATES 中的 DIRS 
			为 [BASE_DIR+"/Moss_html",BASE_DIR+"/Moss_static",BASE_DIR+"/Moss_templates",],
	2.创建Moss_templates/base.html为模板页
	3.创建Moss_templates/templates1.html, Moss_templates/templates2.html
	4.创建private_project/view_templates.py
	5修改修改private_project/urls.py
		5.1 添加from private_project.view_templates import temp1, temp2
		5.2 url("^temp1", temp1),
		5.3 url("^temp2", temp2),
		
5.创建应用
	1.右键点击项目private_project(not is private_project/private_project), 
		右键菜单中Django中点击create application, 
	2.创建应用appTest
	3.修改private_project/private_project
		1.private_project/private_project中修改settings.py
		2.settings.py中INSTALLED_APPS 添加appTest
	4.添加页面
		1.修改models.py, 用HttpResponse输出界面
		2.在private_project/urls中添加import appTest.models 
		3.在private_project/urls中添加url(r'^clock/', appTest.models.appView),

6.引入js和css
	1.创建应用JSorCSS
		-创建应用application具体方法参照提示5
		-创建Moss_html/test_js_base.html, 在html中引入js/css
		-添加moderls中appView调用test_js_base.html
	2.创建文件夹static
		-创建test.js和test.css
		-修改setting,结尾处添加:
			'''
			STATIC_URL = '/static/'
			STATICFILES_DIRS = (
   				os.path.join(os.path.dirname(__file__), '../static/').replace('\\','/'),
    		)
			'''
	3.修改urls
		-引入文件import settings
		-添加url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_URL }),
		-目的是static中的文件用静态方式引用，而非Python文件
		-添加url(r'^css/',JSorCSS.models.CSS_View),

7.Get传参数
	1.创建应用get_post_method, 具体方法参考方法5.
	2.创建文件夹get_post_html
		-添加文件夹方法参考方法一
		-编写传参页面search_form.html
	2.编写接收函数get_post_method/search.py
		-search方法接收get参数
		-search_form调用页面
	3.修改private_project/url

8.Post传参数
	1.首先修改private_project/settings中MIDDLEWARE_CLASSES
		-添加'django.middleware.csrf.CsrfViewMiddleware',
		-防止跨域请求限制'CSRF cookie not set'
	2.在方法7的基础上
		-添加get_post_html/post.html
		-添加get_post_method/search_post.py
	3.修改private_project/url