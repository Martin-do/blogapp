from django import forms
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field

from .models import Post, Author, Comment, User

# class UserForm(forms.ModelForm):
#     password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    # class Meta:
    #     model = User
    #     fields = [
    #         'first_name',
    #         'last_name',
    #         'username',
    #         'email',
    #         'password',
    #     ]

    #     def clean(self, *args, **kwargs):
    #         password1 = self.cleaned_data.get("password1")
    #         password2 = self.cleaned_data.get("password2")
    #         if password1 != password2:
    #             raise forms.ValidationError("Passwords does not match")
    #         email_qs = User.objects.filter(email=email)
    #         if email_qs.exists():
    #             raise forms.ValidationError("User with this Email already exist")
    #         return super(UserForm, self).clean(*args, **kwargs)
                
            
# class UserLoginForm(forms.ModelForm):
#     password = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
    
#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'password',
#         )
#     def clean(self, *args, **kwargs):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')

#         if username and password:
#             user = authenticate(username=username, password=password)
#             if not user:
#                 raise forms.ValidationError("This user does not exist")
#             if not user.check_password(password):
#                 raise forms.ValidationError("Incorrect Password")
#         return super(UserLoginForm, self).clean(*args, **kwargs)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body')

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.helper = FormHelper
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column(Field('title', placeholder="Title", css_class=""),css_class='form-group col-md-6 mb 0'),
                Column('author', css_class='form-group col-md-6 mb 0'),
                Column('body', css_class='form-group col-md-6 mb 0', placeholder="here"),
                # Column('body', css_class='form-control', row=4, placeholder='Type your Post'),
                css_class='form-row'
            ),
            

            Submit('submit', 'Save Post', css_class='btn-success')
        )
    

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs ={
        'class': 'form-control',
        'placeholder': 'Type your Comment',
        'id': 'usercomment',
        'rows': 4
    }))
    
    class Meta:
        model = Comment
        fields = ('content',)


class PasswordResetForm(forms.ModelForm):
    # username = 

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if username and email:
            user = authenticate(username=username, email=email)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect email")
        return super(PasswordResetForm, self).clean(*args, **kwargs)


    class Meta:
        model = User
        fields = ('username', 'email' )