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
		1.1�޸�TEMPLATES �е� DIRS 
			Ϊ [BASE_DIR+"/Moss_html",BASE_DIR+"/Moss_static",BASE_DIR+"/Moss_templates",],
	2.����Moss_templates/base.htmlΪģ��ҳ
	3.����Moss_templates/templates1.html, Moss_templates/templates2.html
	4.����private_project/view_templates.py
	5�޸��޸�private_project/urls.py
		5.1 ���from private_project.view_templates import temp1, temp2
		5.2 url("^temp1", temp1),
		5.3 url("^temp2", temp2),
		
5.����Ӧ��
	1.�Ҽ������Ŀprivate_project(not is private_project/private_project), 
		�Ҽ��˵���Django�е��create application, 
	2.����Ӧ��appTest
	3.�޸�private_project/private_project
		1.private_project/private_project���޸�settings.py
		2.settings.py��INSTALLED_APPS ���appTest
	4.���ҳ��
		1.�޸�models.py, ��HttpResponse�������
		2.��private_project/urls�����import appTest.models 
		3.��private_project/urls�����url(r'^clock/', appTest.models.appView),

6.����js��css
	1.����Ӧ��JSorCSS
		-����Ӧ��application���巽��������ʾ5
		-����Moss_html/test_js_base.html, ��html������js/css
		-���moderls��appView����test_js_base.html
	2.�����ļ���static
		-����test.js��test.css
		-�޸�setting,��β�����:
			'''
			STATIC_URL = '/static/'
			STATICFILES_DIRS = (
   				os.path.join(os.path.dirname(__file__), '../static/').replace('\\','/'),
    		)
			'''
	3.�޸�urls
		-�����ļ�import settings
		-���url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_URL }),
		-Ŀ����static�е��ļ��þ�̬��ʽ���ã�����Python�ļ�
		-���url(r'^css/',JSorCSS.models.CSS_View),

7.Get������
	1.����Ӧ��get_post_method, ���巽���ο�����5.
	2.�����ļ���get_post_html
		-����ļ��з����ο�����һ
		-��д����ҳ��search_form.html
	2.��д���պ���get_post_method/search.py
		-search��������get����
		-search_form����ҳ��
	3.�޸�private_project/url

8.Post������
	1.�����޸�private_project/settings��MIDDLEWARE_CLASSES
		-���'django.middleware.csrf.CsrfViewMiddleware',
		-��ֹ������������'CSRF cookie not set'
	2.�ڷ���7�Ļ�����
		-���get_post_html/post.html
		-���get_post_method/search_post.py
	3.�޸�private_project/url