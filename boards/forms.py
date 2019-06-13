from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    
    title = forms.CharField(
        label = '제목',
        widget= forms.TextInput(attrs={
            'placeholder': 'Enter the title',
        })
    )

    content = forms.CharField(
        label= '내용',
        widget = forms.Textarea(attrs={
            'plceholder': 'Enter the text',
        })

    )

    class Meta:     # 데이터를 설명하기 위한 데이터 (메타데이터)
        model = Board
        fields = ('title', 'content', )



'''
class BoardForm(forms.Form):
    title = forms.CharField(
        max_length=50,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class':'title',
                'placeholder': 'Enter the title'

            }
        )

    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'content-type',
                'rows': 5,
                'cols': 50,
                'placeholder': 'Enter the content',
            }
        )

    )
'''