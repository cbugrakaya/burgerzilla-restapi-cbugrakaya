# veri tabanı ile ilgili yapacağımız işlemleri tutmak için yazılmıştır.
# from datetime import datetime
# from flask import current_app
# from flask_jwt_extended import create_access_token

# from app import db
# # from app.utils import message, err_resp, internal_err_resp
# from app.models.user import

from datetime import datetime
from email import message
from flask import current_app
from flask_jwt_extended import create_access_token

from app import db
from app.utils import message,err_resp, internal_err_resp
from app.models.users import Users
from app.models.schemas import UsersSchema

user_schema = UsersSchema()

# Customer Register and Login Service
class AuthCustService:
    @staticmethod
    def login(data):
        email = data.get('email')
        password = data.get('password')
        try:
            if not (user := Users.query.filter_by(email=email).first()):
                pass
                return err_resp('Email herhangi bir hesapla uyuşmadı',"email_404",404)
            elif user and user.verify_password(password):
                user_info = user_schema.dump(user)
                access_token = create_access_token(identity=user.id)
                resp = message('True', 'Giriş başarılı')
                resp['access_token'] = access_token
                resp['user'] = user_info
                return resp,200
            return err_resp('Email veya şifre hatalı',"email_password_404",404)

        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def register(data):
        email = data.get('email')
        fullname = data.get('fullname')
        password = data.get('password')
        
        if Users.query.filter_by(email=email).first():
            return err_resp('Bu email adresi kullanılıyor',"email_409",409)
        elif Users.query.filter_by(fullname=fullname).first():
            return err_resp('Bu kullanıcı adı kullanılıyor',"username_409",409)
        try:
            # kullanıcı oluştu
            user = Users(email=email,
                            fullname=fullname,
                            password=password,
                            role_type=1)
            db.session.add(user) # kullanıcı veri tabanına ekleniyor
            db.session.commit() # veri tabanına eklenen kullanıcı kaydediliyor

            user_info = user_schema.dump(user) # user modeli json formatına dönüştürülüyor
            access_token = create_access_token(identity=user.id) # token oluşturuluyor
            resp = message('True', 'Kayıt başarılı') # mesaj oluşturuluyor
            resp['access_token'] = access_token # token ekleniyor
            resp['user'] = user_info # user bilgisi ekleniyor
            return resp,200 # 200 dönüyor
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()


# Restaurant Register and Login Service
class AuthResService():
    @staticmethod
    def login(data):
        email = data.get('email')
        password = data.get('password')
        try:
            if not (user := Users.query.filter_by(email=email).first()):
                pass
                return err_resp('Email herhangi bir hesapla uyuşmadı',"email_404",404)
            elif user and user.verify_password(password):
                user_info = user_schema.dump(user)
                access_token = create_access_token(identity=user.id)
                resp = message('True', 'Giriş başarılı')
                resp['access_token'] = access_token
                resp['user'] = user_info
                return resp,200
            return err_resp('Email veya şifre hatalı',"email_password_404",404)

        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def register(data):
        email = data.get('email')
        fullname = data.get('fullname')
        password = data.get('password')
        
        if Users.query.filter_by(email=email).first():
            return err_resp('Bu email adresi kullanılıyor',"email_409",409)
        elif Users.query.filter_by(fullname=fullname).first():
            return err_resp('Bu kullanıcı adı kullanılıyor',"username_409",409)
        try:
            # kullanıcı oluştu
            user = Users(email=email,
                            fullname=fullname,
                            password=password,
                            role_type=2)
            db.session.add(user) # kullanıcı veri tabanına ekleniyor
            db.session.commit() # veri tabanına eklenen kullanıcı kaydediliyor

            user_info = user_schema.dump(user) # user modeli json formatına dönüştürülüyor
            access_token = create_access_token(identity=user.id) # token oluşturuluyor
            resp = message('True', 'Kayıt başarılı') # mesaj oluşturuluyor
            resp['access_token'] = access_token # token ekleniyor
            resp['user'] = user_info # user bilgisi ekleniyor
            return resp,200 # 200 dönüyor
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()