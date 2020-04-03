## DjangoBB - Discussion forum on Django

DjangoBB is a quick and simple forum which uses the Django Framework (written in Python language).
Abbreviation DjangoBB stands for **Django** **B**ulletin **B**oard.
DjangoBB is distributed under the BSD license.


## Features

 * the usage of various DBMS (MySQL, PostgreSQL, Oracle, SQLite)
 * the ease of integration into any Django project and the ease of installation
 * the usage of standard libraries for launching on conventional hostings with python support
 * user-friendly installation process
 * classic view of the forum like IPB, PhpBB, Punbb
 * easy forum setup
 * high speed
 * reliability

At the current stage of development the main object is the functional implementation of the PunBB forum, in the sequel it is projected to expand it significantly.

## Installation ##

Add DjangoBB and Haystack to your INSTALLED_APPS:

```python
INSTALLED_APPS = [
...
'haystack',
'djangobb_forum',
...
]
```
For testing a simple backend setting can be used for Haystack:

```python
HAYSTACK_CONNECTIONS = {
	'default': {
		'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
	},
}
```

Add the urls to your project

```python
urlpatterns = [
...
	path('forum/', include('djangobb_forum.urls')),
...
]
```

Now synchronise the database and collect the static files:

```bash
./manage.py migrate
./manage.py collectstatic
```

## Development ##

### Translation ###

http://www.transifex.net/projects/p/djangobb/

![translation progress](http://www.transifex.net/projects/p/djangobb/resource/default/chart/image_png)

[Howto add new translation?](https://bitbucket.org/slav0nic/djangobb/wiki/HowtoAddNewTranslation)
