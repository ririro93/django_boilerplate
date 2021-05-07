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

        self.fields['nickname'] = forms.CharField(
            required=False,
            label=False,
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'user-nickname',
                    'placeholder': 'Username (optional)'
                }
            )
        )

    def save(self, request):
        nickname = self.cleaned_data.get('nickname')
        user = super(MyCustomSignupForm, self).save(request)
        if nickname == '':
            print('no nickname set')
            user.nickname = 'no username'
            user.save()
        print('## new user signup:', user)
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

        self.fields['nickname'] = forms.CharField(
            required=False,
            label=False,
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'user-nickname',
                    'placeholder': 'Username (optional)'
                }
            )
        )

    def save(self, request):
        nickname = self.cleaned_data.get('nickname')
        user = super(MyCustomSocialSignupForm, self).save(request)
        if nickname == '':
            print('no nickname set')
            user.nickname = 'no username'
            user.save()
        print('## new social user signup:', user)
        return user