from django import forms

from users.models import *

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user', 'date_of_profile_update']
        
    
    def save(self, commit=True):
        profile = super(UserProfileForm, self).save(commit=False)
        profile.user = self.request.user
        profile.profile_image = self.cleaned_data['profile_image']
        profile.first_name = self.cleaned_data['first_name']
        profile.last_name = self.cleaned_data['last_name']
        profile.birthdate = self.cleaned_data['birthdate']
        profile.gender = self.cleaned_data['gender']
        profile.bio = self.cleaned_data['bio']
        if commit:
            profile.save()
            return profile


        