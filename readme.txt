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
		1.1修改TEMPLATES 中的 DIRS 为 [BASE_DIR+"/Moss_html",BASE_DIR+"/Moss_static",BASE_DIR+"/Moss_templates",],
	2.创建Moss_templates/base.html为模板页
	3.创建Moss_templates/templates1.html, Moss_templates/templates2.html
	4.创建private_project/view_templates.py
	5修改修改private_project/urls.py
		5.1 添加from private_project.view_templates import temp1, temp2
		5.2 url("^temp1", temp1),
		5.3 url("^temp2", temp2),