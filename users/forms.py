from django import forms

from users.models import *

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user',]
        
    
    def save(self, commit=True):
        profile = super(UserProfileForm, self).save(commit=False)
        profile.profile_image = self.cleaned_data['profile_image']
        profile.first_name = self.cleaned_data['first_name']
        profile.last_name = self.cleaned_data['last_name']
        profile.birthdate = self.cleaned_data['birthdate']
        profile.gender = self.cleaned_data['gender']
        profile.bio = self.cleaned_data['bio']
        profile.date_of_profile_update = timezone.now()
        if commit:
            profile.save()
            return profile

# TOdo: i need to download an edit profile template so it kinda goes well with this



        