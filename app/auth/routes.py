#app/auth/routes

from app.auth import auth

@auth.route("/index")
def index():
    return "I am a software engineer"
