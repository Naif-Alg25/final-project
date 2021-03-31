from django import forms
from django.forms import fields, widgets
from .models import Doctors, Evaluation, Groups, Projects, Students


class Doc(forms.ModelForm):
    class Meta:
        model= Doctors
        fields=['id_groups_fk']


        widgets ={
            'id_groups_fk':forms.Select(attrs={'class':'form-control'}),
        } 





class Distrbution(forms.ModelForm):
    class Meta:
        model= Evaluation
        fields=['id_doctor_fk', 'id_doctor_fk2', 'id_doctor_fk3']
#

        widgets ={
            'id_doctor_fk ':forms.Select(),
            'id_doctor_fk2':forms.Select(),
            'id_doctor_fk3':forms.Select(),
        } 
        



class CRN(forms.ModelForm):
    class Meta:
        model= Groups
        fields=['name_groups']


        widgets ={
            'name_Groups':forms.TextInput(attrs={'class':'form-control'}),
        } 




class Add_Idea(forms.ModelForm):
    class Meta:
        model =Projects
        fields=['name_projects','filled_projects','descriotion_projects','file_project','id_projects','id_Doctors_fk','status']

        widgets ={
            'id_projects':forms.TextInput(attrs={'class':'form-control'}),
            'name_projects':forms.TextInput(attrs={'class':'form-control'}),
            'filled_projects':forms.TextInput(attrs={'class':'form-control'}),
            'descriotion_projects':forms.TextInput(attrs={'class':'form-control'}),
            'file_project':forms.FileInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
        } 





class Stu(forms.ModelForm):
    class Meta:
        model= Students
        fields=['id_groups_fk']


        widgets ={
            'id_groups_fk':forms.Select(attrs={'class':'form-control'}),
        } 



class ChoiceIdea(forms.ModelForm):
    class Meta:
        model= Students
        fields=['id_groups_fk']
        widgets ={
            'id_groups_fk':forms.Select(attrs={'class':'form-control'}),
        } 
        









class dont_have_groupeFORM(forms.ModelForm):
    class Meta:
        model= Students
        fields=['name_Students']


        widgets ={
            'name_Students':forms.TextInput(attrs={'class':'form-control'}),
        } 





class UploadIdeaForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields=['name_projects','filled_projects','descriotion_projects','file_project','id_projects','status']

        widgets ={
            'id_projects':forms.TextInput(attrs={'class':'form-control'}),
            'name_projects':forms.TextInput(attrs={'class':'form-control'}),
            'filled_projects':forms.TextInput(attrs={'class':'form-control'}),
            'descriotion_projects':forms.TextInput(attrs={'class':'form-control'}),
            'file_project':forms.FileInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
        } 



class updeateForm(forms.ModelForm):
    class Meta:
        model= Students
        fields=['id_groups_fk']


        widgets ={
            'id_groups_fk':forms.Select(attrs={'class':'form-control'}),
        } 

        
class DoctorCreatingGroup(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ['name_groups']

        widgets = {
            #'id_groups':forms.TextInput(attrs={'class':'form-control'}),
            'name_groups':forms.TextInput(attrs={'class':'form-control'}),
            }
class Add_GRP(forms.ModelForm):
    class Meta:
        model = Students
        fields=['id_groups_fk']      
        
        widgets = { 'id_groups_fk':forms.Select(attrs={'class':'form-control'}),}
        


class Choose_group(forms.ModelForm):
    class Meta:
        model= Students
        fields=['id_groups_fk']
        widgets ={
            'id_groups_fk':forms.Select(attrs={'class':'form-control'}),
        } 

class InsertIdea(forms.ModelForm):
    class Meta:
        model = Projects
        fields=['name_projects','filled_projects','descriotion_projects','id_groups_fk']

        widgets ={
            'id_projects':forms.TextInput(attrs={'class':'form-control'}),
            'name_projects':forms.TextInput(attrs={'class':'form-control'}),
            'filled_projects':forms.TextInput(attrs={'class':'form-control'}),
            'descriotion_projects':forms.TextInput(attrs={'class':'form-control'}),
            'id_groups_fk':forms.Select(attrs={'class':'form-control'}),
        } 

class ChooseGroupDoctor(forms.ModelForm):

    class Meta:
        model  = Doctors
        fields = ['id_doctors','id_groups_fk']

        widgets = {
            'id_doctors':forms.Select(attrs={'class':'form-control'}),
            'id_groups_fk':forms.Select(attrs={'class':'form-control'})
            } 


class DoctorEvaluatingGroupForm (forms.ModelForm):
    class Meta:
        model =Evaluation
        fields=['id_evaluation','file_evaluation','file_evaluation_dr2','file_evaluation_dr3']

        widgets ={
            'id_evaluation':forms.Select(attrs={'class':'form-control'}),
            #'id_groups_fk':forms.Select(attrs={'class':'form-control'}),
            'file_evaluation':forms.FileInput(attrs={'class':'form-control'}),
            'file_evaluation_dr2':forms.FileInput(attrs={'class':'form-control'}),
            'file_evaluation_dr3':forms.FileInput(attrs={'class':'form-control'}),
            
        } 
