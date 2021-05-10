# Django Boilerplate Code
> this empty project includes the following

- Templates (bootstrap)
    - [x] navbar
    - [x] login template
    - [x] signup template
    - [x] logout template
        - [x] get rid of intermediate logout page
    - [x] profile template
    - [x] password change template
    - [x] verification email sent template
    - [x] reset password (when forgotten) template
    - [x] social signup template
    
- Authentication
    - [x] login with email
    - [x] 3rd party login
        - [tutorial](https://whizzoe.medium.com/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5) : just add OAuth ID + Secret via admin 
    - [x] social account full logout -> ask social account again for authorization
        - adding `action='reauthenticate'` param works except for github 
        - github probably doesn't provide this feature
    - [x] account verification email
        - [blog](https://code4human.tistory.com/83)
        - [tutorial](https://pythoneatstail.com/en/overview-all-articles/signup-and-password-reset-email-verification-allauth-django/)
    - [x] connecting 3rd party account with existing account
    - [x] reset password (when forgotten)


# Problems
## 1. username field
would like to use username as a non-unique nickname that can be set optionally during signup

### Problem
even if username field is set to `unique=False` in CustomUser Model, 
- django allauth's SignupForm -> clean method -> adapter.save_user()
    - grabs username by `data.get("username")`
    - checks if username is unique

### Solution
- change username field name to nickname
- add `ACCOUNT_USER_MODEL_USERNAME_FIELD = None` to settings.py
    - without this -> error because allauth uses username internally


# Customizable accounts related templates
- `Backend/Backend/templates/account/*`
- `Backend/Backend/templates/socialaccount/connections.html`
