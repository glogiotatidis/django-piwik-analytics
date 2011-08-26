from distutils.core import setup


setup(name='piwik_analytics',
      version='0.1',
      description='A simple Django application to integrate Piwik Analytics into your projects',
      author='Giorgos Logiotatidis',
      author_email='seadog@sealabs.net',
      url='http://github.com/glogiotatidis/django-piwik-analytics/tree/master',
      packages=['piwik_analytics', 'piwik_analytics.templatetags'],
      package_data={'piwik_analytics': ['templates/google_analytics/*.html']},
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: AGPL License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
