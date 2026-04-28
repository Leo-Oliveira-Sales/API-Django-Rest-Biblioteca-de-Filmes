from rest_framework.permissions import DjangoModelPermissions


# Controle total pelo admin
# Olha o método da requisição (GET, POST, etc.)
# Verifica se o usuário tem a permissão correspondente
# Permite ou bloqueia
class GlobalDefaultPermission(DjangoModelPermissions):
    pass
