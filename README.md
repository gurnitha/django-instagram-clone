# DJANGO INSTAGRAM CLONE
Belajar membuat aplikasi INSTAGRAM berdasarkan tutorial Desphixs di Youtube

Github: https://github.com/gurnitha/django-instagram-clone
Youtube: https://www.youtube.com/watch?v=qw5ZEvylQBA&list=PL_KegS2ON4s7aVgtk-UI6jaXazt6KyntZ


#### 0. Membuat repositori di Github

        modified:   .gitignore
        modified:   README.md


#### 1. Apa yang akan kita buat?

        modified:   README.md


#### 2. Membuat proyek Django dengan nama 'Config'

        new file:   Config/__init__.py
        new file:   Config/asgi.py
        new file:   Config/settings.py
        new file:   Config/urls.py
        new file:   Config/wsgi.py
        modified:   README.md
        new file:   manage.py


#### 3. Membuat app Django dengan nama 'App/Post'

        new file:   App/Post/__init__.py
        new file:   App/Post/admin.py
        new file:   App/Post/apps.py
        new file:   App/Post/migrations/__init__.py
        new file:   App/Post/models.py
        new file:   App/Post/tests.py
        new file:   App/Post/views.py
        modified:   README.md


#### 4. Register 'App/Post' pada Config/settings.py

        modified:   App/Post/apps.py
        modified:   Config/settings.py


#### 5. Setup Config/settings.py

        modified:   Config/settings.py
        modified:   README.md


#### 6. Membuat requirements.txt file

        > pip list

        Package             Version
		------------------- -------
		asgiref             3.7.2
		crispy-bootstrap4   2022.1
		Django              4.2.2
		django-crispy-forms 2.0
		pip                 23.1.2
		setuptools          56.0.0
		sqlparse            0.4.4
		typing_extensions   4.6.3
		tzdata              2023.3

		> pip freeze > requirements.txt

        modified:   README.md
        new file:   requirements.txt


#### 7. Membuat homepage: views, templates, urls dan static files

        new file:   App/Post/urls.py
        modified:   App/Post/views.py
        modified:   Config/urls.py
        modified:   README.md
        new file:   static/assets1/default-user.png
        new file:   static/assets1/default.jpg
        ...
        new file:   static/assets3/images/login-img.jpg
        new file:   static/default.jpg
        new file:   templates/base.html
        new file:   templates/index.html


#### 8. Membuat models: Tag, Post, Follow, Stream, migrations, superuser dan add post

        modified:   App/Post/admin.py
        new file:   App/Post/migrations/0001_initial.py
        modified:   App/Post/models.py
        modified:   README.md
        new file:   media/user_1/architecture-5339245_1920.jpg

        :)


#### 9. Memodifikasi homepage

        modified:   README.md
        new file:   static/house.jpg
        modified:   templates/base.html
        modified:   templates/index.html