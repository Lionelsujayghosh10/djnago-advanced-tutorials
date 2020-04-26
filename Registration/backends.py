from .models import Users
import logging
from django.contrib.auth.hashers import check_password
# from django.contrib.auth.backends import BaseBackend
from django.utils.timezone import now


#todo: last_login need to update
class MyAuthBackend():
    def authenticate(self, email, password): 
        try:
            user = Users.objects.get(email=email,is_delete=0)
            password_status = check_password(password, user.password)
            if password_status == True:
                # user.last_login = now
                # user.save()
                return user
            else:
                return None
        except Users.DoesNotExist:
            logging.getLogger("error_logger").error("user with login %s does not exists " % login)
            return None
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None



    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(user_id=user_id)
            if user.is_delete == 0:
                return user
            return None
        except UserModel.DoesNotExist:
            logging.getLogger("error_logger").error("user with %(user_id)d not found")
            return None