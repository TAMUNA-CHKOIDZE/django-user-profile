from django import forms

from profiles.models import Post, Profile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']
        labels = {
            'caption': '',
            'image': 'Photo'
        }
        widgets = {
            'caption': forms.Textarea(
                attrs={'rows': 3, 'placeholder': "What's on your mind?", 'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super().clean()
        caption = cleaned_data.get('caption')
        image = cleaned_data.get('image')

        if not caption and not image:
            raise forms.ValidationError("Please provide text or upload an image.")
        return cleaned_data


class CoverUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_cover']
