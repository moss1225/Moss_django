1.���Moss_html��Moss_static�ļ��У�
	1.�޸�private_project/settings.py
		1.1TEMPLATES �е� DIRS Ϊ [BASE_DIR+"/Moss_html",BASE_DIR+"/Moss_static",],
	
2.����index��ҳ
	1.����Moss_html/index.html
	2.����private_project/view_index.py
	3.�޸�private_project/urls.py
		3.1 ���from private_project.view_index import hello���� hello����
		3.2 url("^", hello),��http://127.0.0.1:8000/����hello����������index.html
	