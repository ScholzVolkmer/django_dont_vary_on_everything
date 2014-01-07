django-dont-vary-on-everything is a library to give remove all vary headers. 

The ``Vary`` header
===================

The ``Vary`` HTTP response header is used by caching systems to know what HTTP request headers to cache this page based on. A typical Vary header might look like this: ``Vary: Accept-Language, Cookie``, which means that requests to that URL with the same ``Accept-Language`` and ``Cookie`` field can use the cached value. In this example, we say that "The page varies on 'Cookie' and 'Accept-Language'. It does not vary on 'User-Agent'".

Installation
============

  
To use it you *must* put ``RemoveVaryHeadersMiddleware`` in your ``MIDDLEWARE_CLASSES`` and it must be below ``UpdateCacheMiddleware`` and above other middleware classes. Ideally put it straight under ``UpdateCacheMiddleware``.

    MIDDLEWARE_CLASSES = ( 
        ….
        'django.middleware.cache.UpdateCacheMiddleware',
        'django_dont_vary_on_everything.middleware.RemoveVaryHeadersMiddleware',
        …
    )

Usage
=====

Thats it. It will try to remove all vary headers.


Caveats
=======

Sending an incorrect cached page can be very embarassing. People might be able to see other people's logged in and personal details. Ensure you know what you're doing.

If this is to strict, take a look at django-dont-vary-on.



Thanks
=======

Thanks to https://github.com/rory/django-dont-vary-on for providing inspiration and a basis for this library.