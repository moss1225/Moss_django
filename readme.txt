1.���Moss_html��Moss_static�ļ��У�
	1.�޸�private_project/settings.py
		1.1TEMPLATES �е� DIRS Ϊ [BASE_DIR+"/Moss_html",BASE_DIR+"/Moss_static",],
	
2.����index��ҳ
	1.����Moss_html/index.html
	2.����private_project/view_index.py
	3.�޸�private_project/urls.py
		3.1 ���from private_project.view_index import hello���� hello����
		3.2 url("^$", hello),��http://127.0.0.1:8000/����hello����������index.html
		
3.����cafe����
	1.����Moss_html/cafe.html
	2.����private_project/view_cafe.py
	3.�޸�private_project/urls.py
		3.1 ���from private_project.view_cafe import cafe
		3.2 url("^cafe", cafe),
		
4.����ģ��
	1.����Moss_templates
		1.1�޸�TEMPLATES �е� DIRS Ϊ [BASE_DIR+"/Moss_html",BASE_DIR+"/Moss_static",BASE_DIR+"/Moss_templates",],
	2.����Moss_templates/base.htmlΪģ��ҳ
	3.����Moss_templates/templates1.html, Moss_templates/templates2.html
	4.����private_project/view_templates.py
	5�޸��޸�private_project/urls.py
		5.1 ���from private_project.view_templates import temp1, temp2
		5.2 url("^temp1", temp1),
		5.3 url("^temp2", temp2),