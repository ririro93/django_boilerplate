# Django Boilerplate Code
> this empty project includes the following

- Templates (bootstrap)
    - navbar
- Authentication
    - login with email
    - 3rd party login

# Problems

## 1. username field
would like to user username as a non-unique nickname that can be optionally set during signup

### Problem
even if username field is set to unique=False in CustomUser Model, 
- django allauth's SignupForm -> clean method -> adapter.save_user
    - grabs username by data.get("username")
    - checks if username is unique

### Solution
- change username field name to nickname
- add `ACCOUNT_USER_MODEL_USERNAME_FIELD = None` to settings.py
    - without this -> error because allauth uses username internally
