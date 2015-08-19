"""Utility functions used by multiple AVA apps.

Be careful not to import too many AVA modules here, as that could
create a recipe for annoying circular dependencies. It's fine to
import Django stuff or system libraries as needed.
"""

import django.contrib.auth.decorators


def is_ava_superuser(user):
    """True if the user is an AVA superuser.

    That is: they have the UserRights.is_admin attribute *and*
    the Django user.is_superuser.attribute.
    """
    return user.is_superuser and user.rights.is_admin


# Create a simple decorator that can be used to ensure
# a user is an AVA superuser before accessing a view.
# Based on user_passes_test.
#
# https://docs.djangoproject.com/en/1.8/topics/auth/default/#django.contrib.auth.decorators.user_passes_test
#
# The decorator can either be applied to a view in urls.py
# or it can be added to the view classes 'dispatch' method.
# See the django docs, as it's a little weird.
#
# https://docs.djangoproject.com/en/1.8/topics/class-based-views/intro/#decorating-in-urlconf
# https://docs.djangoproject.com/en/1.8/topics/class-based-views/intro/#decorating-the-class
#
# So on the one hand, I think that permissions should be defined in
# the view, but on the other hand, at the moment the way you do that
# (by defining dispatch() specifically so that you can decorate it) is
# *really* ugly, one of the ugliest things in Django.
require_ava_superuser = django.contrib.auth.decorators.user_passes_test(is_ava_superuser)

# To create additional permissions checks, it might be easiest to copy
# this model: Create a simple true/false function like
# 'is_ava_superuser' above, and then create a decorator for it like
# 'require_ava_superuser'.
