from django.urls import include, path

from . import views

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("", views.home, name="homepage"),
    path("xss", views.xss, name="xss"),
    path("xssL", views.xss_lab, name="xss_lab"),
    path("xssL1", views.xss_lab, name="xss_lab"),
    path("sql", views.sql, name="sql"),
    path("sql_lab", views.sql_lab, name="sql_lab"),
    path("sql_lab1", views.sql_lab, name="sql_lab"),
    path("insec_des", views.insec_des, name="insec_des"),
    path("insec_des_lab", views.insec_des_lab, name="insec_des_lab"),
    path("xxe", views.xxe, name="xxe"),
    path("xxe_lab", views.xxe_lab, name="xxe_lab"),
    path("xxe_see", views.xxe_see, name="xxe_see"),
    path("xxe_parse", views.xxe_parse, name="xxe_parse"),
    path("auth_lab", views.auth_lab, name="auth_lab"),
    path("auth_lab/signup", views.auth_lab_signup, name="auth_lab_signup"),
    path("auth_lab/login", views.auth_lab_login, name="auth_lab_login"),
    path("auth_lab/logout", views.auth_lab_logout, name="auth_lab_logout"),
    path("auth", views.auth_home, name="auth_home"),
    path("ba", views.ba, name="Broken Access Control"),
    path("ba_lab", views.ba_lab, name="Broken Access Control Lab"),
    path("data_exp", views.data_exp, name="data_exp"),
    path("data_exp_lab", views.data_exp_lab, name="data_exp_lab"),
    path("robots.txt", views.robots, name="robots.txt"),
    path("500error", views.error, name="500error"),
    path("cmd", views.cmd, name="Command Injection"),
    path("cmd_lab", views.cmd_lab, name="Command Injection Lab"),
    path("bau", views.bau, name="Broken Authe"),
    path("bau_lab", views.bau_lab, name="LAB"),
    path("login_otp", views.login_otp, name="OTP Login"),
    path("otp", views.Otp, name="OTP Verification"),
    path("sec_mis", views.sec_mis, name="Security Misconfiguration"),
    path("sec_mis_lab", views.sec_mis_lab, name="Security Misconfiguration Lab"),
    path("secret", views.secret, name="Secret key for A6"),
    path("a9", views.a9, name="A9"),
    path("a9_lab", views.a9_lab, name="A9 LAb"),
    path("get_version", views.get_version, name="Get Version"),
    path("a10", views.a10, name="A10"),
    path("a10_lab", views.a10_lab, name="A10 LAb"),
    path("debug", views.debug, name="debug"),
]
