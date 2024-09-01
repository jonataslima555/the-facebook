from models import Client, Follow, db

# Função para listar usuários que o usuário ainda não segue
def list_available_users_to_follow(logged_client):
    # Seleciona todos os usuários que o usuário logado ainda não segue
    available_users = Client.select().where(
        (Client.id != logged_client.id) & 
        (Client.id.not_in(
            Follow.select(Follow.followee_id).where(Follow.follower == logged_client)
        ))
    )
    
    if available_users.exists():
        print("\nUsuários disponíveis para seguir:\n")
        for user in available_users:
            print(f"ID: {user.id}, Nome: {user.name}, Email: {user.email}")
    else:
        print("\nNenhum usuário disponível para seguir.")

# Função para seguir um usuário
def follow_user(logged_client):
    list_available_users_to_follow(logged_client)  # Lista os usuários disponíveis antes de pedir o ID

    followee_id = int(input("Digite o ID do usuário que você quer seguir: "))
    try:
        followee = Client.get(Client.id == followee_id)
        if logged_client.id == followee.id:
            print("Você não pode seguir a si mesmo.")
            return

        with db.atomic():
            Follow.create(
                follower=logged_client,
                followee=followee
            )
        print(f"Você está seguindo {followee.name}")
    except Client.DoesNotExist:
        print("Usuário não encontrado.")
    except Exception as e:
        print(f"Erro ao seguir usuário: {e}")
