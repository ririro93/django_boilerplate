from django import forms
from allauth.account.forms import LoginForm, SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm

class MyCustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'].label = False
        self.fields['login'].widget.attrs.update({
            'class': 'form-control',
            'id': 'user-email',
            'placeholder': 'Email'
        })

        self.fields['password'].label = False
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'id': 'user-password',
            'placeholder': 'Password'
        })

        self.fields['remember'].widget.attrs.update({
            'id': 'remember-checkbox',
        })
    
    
class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = False
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'user-email',
            'placeholder': 'Email'
        })

        self.fields['password1'].label = False
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'id': 'user-password',
            'placeholder': 'Password'
        })

        self.fields['password2'].label = False
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'id': 'user-confirm-password',
            'placeholder': 'Confirm Password'
        })

        self.fields['username'] = forms.CharField(
            required=False,
            label=False,
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'user-username',
                    'placeholder': 'Username (optional)'
                }
            )
        )

    def save(self, request):
        print('## request', request)
        username = self.cleaned_data.get('username')
        user = super(MyCustomSignupForm, self).save(request)
        print('## MyCustomSignupForm save user', user)
        return user
    
    
class MyCustomSocialSignupForm(SocialSignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSocialSignupForm, self).__init__(*args, **kwargs)

        self.fields['email'].label = False
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'user-email',
            'placeholder': 'Email'
        })

        self.fields['username'] = forms.CharField(
            required=False,
            label=False,
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'user-username',
                    'placeholder': 'Username (optional)'
                }
            )
        )

    def save(self, request):
        username = self.cleaned_data.get('username')
        user = super(MyCustomSocialSignupForm, self).save(request)
        print('## MyCustomSocialSignupForm save user', user)
        return user