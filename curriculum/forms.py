from django import forms
from .models import Comment, Reply, Lesson,Standard,Subject
from django.utils.translation import gettext_lazy as _

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('name','course_code','video','ppt','Notes','Assignment')
        labels={'name':_('Topic')}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        labels = {"body":"Comment:"}

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'cols':70, 'placeholder':"Enter Your Comment"}),
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply_body',)

        widgets = {
            'reply_body': forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':10}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ReplyForm, self).__init__(*args, **kwargs)
        
        
class WeekForm(forms.ModelForm):
    class Meta:
        model= Standard
        fields=('name','description')
        
class SubjectForm(forms.ModelForm):
    class Meta:
        model= Subject
        fields=('subject_id','name','description')
        labels ={'subject_id':_('Course code'),'standard':_('Choose a week')}
