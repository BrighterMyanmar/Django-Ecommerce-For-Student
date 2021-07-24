from django import forms
from .models import SubCat


class SubCatForm(forms.ModelForm) :
    class Meta :
        model = SubCat 
        fields = '__all__'
        labels = {
            "name" : "Sub Category Name",
            "parent": "Parent Category Name"
        }
    def __init__(self,*args,**kwargs) :
        super(SubCatForm,self).__init__(*args,**kwargs)
        self.fields["parent"].empty_label = 'Select'
        # self.fields["name"].required = False
        # self.fields["image"].required = False
        # self.fields["parent"].required = False
