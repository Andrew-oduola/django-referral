Django Referral Documentation
=============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api
   models
   signals
   middleware


Key Features
============

* **Unique Referral Codes**: Automatically generate unique referral codes for each user.
* **Referral Link Tracking**: Track sign-ups using unique referral links with cookie support.
* **Middleware Integration**: Optional middleware for seamless referral tracking during user registration.
* **Flexible Reward System**: Easily extendable to implement custom reward logic for successful referrals.
* **Simple Integration**: Designed as a reusable Django app for easy integration into existing projects.
* **Cookie-Based Tracking**: Maintains referral information across sessions using cookies.
* **Database Relationships**: Stores referral relationships between users in the database.
* **Clean API**: Simple utility functions for generating codes and retrieving referrers.

.. note::
   For detailed setup instructions, see the :ref:`installation` page.

Quick Start
===========

1. Install the package:

   .. code-block:: bash

      pip install django-referral2

2. Add to your ``INSTALLED_APPS``:

   .. code-block:: python

      INSTALLED_APPS = [
          # ...
          'referral',
      ]

3. Run migrations:

   .. code-block:: bash

      python manage.py migrate referral

4. Generate referral links: ``https://yourdomain.com/signup?ref=ABC123``

API Reference
=============

The package provides several key components:

* **Models**: ``Referral`` model for storing referral relationships
* **Middleware**: ``ReferralMiddleware`` for automatic referral tracking
* **Utils**: Functions like ``get_referrer_from_request()`` and ``generate_referral_code()``
* **Signals**: Custom signals for referral-related events

License
=======

This project is licensed under the `MIT License <https://opensource.org/licenses/MIT>`_.

.. |mit| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: LICENSE
   :alt: MIT License

|mit| See the `LICENSE <https://github.com/Andrew-oduola/django-referral/blob/main/LICENSE>`_ file for details.

Contributing
============

Contributions are welcome! If you find any issues or have suggestions for improvements:

1. Fork the repository
2. Create a feature branch: ``git checkout -b feature/amazing-feature``
3. Commit your changes: ``git commit -m 'Add amazing feature'``
4. Push to the branch: ``git push origin feature/amazing-feature``
5. Open a pull request

Please ensure your code follows the project's style guidelines and includes appropriate tests.

Support
=======

If you encounter any problems or have questions:

* Check the :ref:`usage` guide for common solutions
* Search existing `GitHub Issues <https://github.com/Andrew-oduola/django-referral/issues>`_
* Open a new issue with detailed information about your problem

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`