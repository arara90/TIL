from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

# UserChangeForm을 상속받는 UserCustomChangeForm
class UserCustomChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model() #django.contrib.auth 소속임
        # 수정 가능한 필드 목록 지정
        fields = ('email', 'first_name', 'last_name')