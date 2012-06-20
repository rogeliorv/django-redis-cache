from setuptools import setup

setup(
    name = "django-redis-cache",
    url = "http://github.com/rogeliorv/django-redis-cache/", # Based on previous work of Sean Bleier
    author = "@rogeliorv",
    author_email = "rog@rogeliorv.com",
    version = "0.9.5",
    packages = ["redis_cache"],
    description = "Redis Cache Backend for Django",
    install_requires=['redis>=2.4.5',],
    classifiers = [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)
