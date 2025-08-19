# Django Referral  

[![PyPI version](https://img.shields.io/pypi/v/django-referral2.svg)](https://pypi.org/project/django-referral2/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  
[![Django](https://img.shields.io/badge/Django-4.0%2B-green.svg)](https://www.djangoproject.com/)  

A **reusable Django app** for implementing a referral system.  
It allows users to generate **unique referral links** and track sign-ups using those links.  

---

## ✨ Features  
- 🔗 Generate unique referral codes for each user  
- 👥 Track referrals during user sign-up  
- 🎁 Optionally reward users for successful referrals  
- 🍪 Cookie & middleware support for referral tracking  
- ⚡ Simple integration into existing Django projects  

---

## 📦 Installation  

### 1. Install the package  


```bash
pip install django-referral2
```


---

### 2. Add to `INSTALLED_APPS`

In `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'referral',  # Add this line
]
```

---

### 3. Run migrations

```bash
python manage.py migrate referral
```

---

### 4. (Optional) Enable Middleware

If you want cookie-based referral tracking:

```python
MIDDLEWARE = [
    ...
    'referral.middleware.ReferralMiddleware',
]
```

---

## 🚀 Usage

### Generate a referral link

If a user has `referral_code="ABC123"`, their referral link is:

```
https://yourdomain.com/signup?ref=ABC123
```

### Track sign-ups

When a new user signs up with a referral link:

* The app detects the referral code
* Links the new user to the referrer
* Saves the relationship in the database

---

## 🛠 Development Setup

Clone the repo and install dependencies:

```bash
git clone https://github.com/yourusername/django-referral-app.git
cd django-referral-app
pip install -r requirements.txt
```

<!-- Run tests:

```bash
pytest
``` -->

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<!-- ## 🔧 Code Example

Here's how to integrate referral tracking into your signup view:

```python
# models.py
from django.contrib.auth.models import User
from django.db import models
from referral.models import Referral

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Your custom fields here

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from referral.utils import get_referrer_from_request

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Get referrer from request (checks both GET params and cookies)
            referrer = get_referrer_from_request(request)
            if referrer:
                # Create referral relationship
                Referral.objects.create(
                    referrer=referrer,
                    referred_user=user
                )
            
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
``` -->

For a complete implementation example, check the [documentation](docs/implementation.md).