Для запуска приложения необходимо иметь установленными git, docker и docker-compose.
#######################################################
#                                                     #
#                  Ссылки на ресурсы                  #
#  Git: https://git-scm.com/, https://github.com/     #
#  Docker, docker -compose: https://www.docker.com/   #
#                                                     #
#######################################################

Для скачивания и запуска через docker-compose необходимо:
1. Создать каталог для приложения (например c:\task\)
2. Открыть командную строку (cmd.exe) и перейи в указанный каталог (cd c:\task\)
3. Выполнить последовательно следующие команды:
	- git clone https://github.com/strax88/news.git
	- cd ./news
	- docker-compose build
	- docker-compose up
4. После выполнения данных комманд в консоле будет отображена следующая информация:
	###########################################################
	#                                                         #
	# Creating network "news_default" with the default driver #
	# Creating news_web_1 ... done                            #
	# Attaching to news_web_1                                 #
	# web_1  | Watching for file changes with StatReloader    #
	#                                                         #
	###########################################################

Для работы с API необходимо использовать следующие адреса:
http://localhost:9000/api/v1/news/category/create/ - Создание категорий (POST запрос: {"name": "Обязательное поле.", "color": <int:1..4>});
http://localhost:9000/api/v1/news/category/all/ - Список всех категорий (GET запрос);
http://localhost:9000/api/v1/news/category/detail/<int:pk> - Работа с категорией (GET, PUT, DELETE);
http://localhost:9000/api/v1/news/create/ - Создание новости (POST запрос: {"name":"Обязательное поле.", "short_description":"Обязательное поле.", "full_description":"Обязательное поле.", "news_category":<int:news_category_id>});
http://localhost:9000/api/v1/news/all/ - Список всех новостей (GET запрос);
http://localhost:9000/api/v1/news/detail/<int:pk> - Работа с новостью (GET, PUT, DELETE);
http://localhost:9000/api/v1/news/by_category/<int:news_category_id> - Список новостей с фильтрацией по категориии (GET запрос, требуется идентификатор категории);