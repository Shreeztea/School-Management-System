from django import forms

from students.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "age", "address","course","document","profile_picture"]
        
        widgets = {
            "name" :forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "email" :forms.EmailInput(
                    attrs={
                        "class": "form-control",
                    }
                ),
            "age" : forms.NumberInput(
                    attrs={
                        "class": "form-control",
                    }
                ),

            "address" : forms.TextInput(
                    attrs={
                        "class": "form-control",
                    }
                ),

            "course" : forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "document": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),
            "profile_picture": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),
        }

    def clean_age(self):
        age = self.cleaned_data["age"]

        if age < 16:
            raise forms.ValidationError(
                "Student must be at least 16 years old."
            )

        return age

    def clean(self):
        cleaned_data = super().clean()

        age = cleaned_data.get("age")
        address = cleaned_data.get("address")

        if age and age < 18 and address == "Kathmandu":
            raise forms.ValidationError(
                "Students under 18 cannot have Kathmandu as their address."
            )

        return cleaned_data