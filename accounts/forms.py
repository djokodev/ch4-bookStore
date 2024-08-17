from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm): #herite du formulaire de la creation d'utilisateur par defaut
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )

class CustomUserChangeForm(UserChangeForm): #herite du formulaire de mis a jour par defaut
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )
