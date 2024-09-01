from models import *

# Função para criar postagens
def create_pb(client, name_publi, descr_publi):
    try:
        with db.atomic():
            Publication.create(
                client=client,
                name_publi=name_publi,
                descr_publi=descr_publi
            )
        print(f'Publicação criada: {name_publi}')
    except AttributeError as e:
        print(f'Erro {e}')

# Função para criar novas postagens
def post_pb(logged_client):
    name_public = input('Digite o assunto da publicação: ')
    descr_public = input('Digite a descrição da postagem: ')
    create_pb(logged_client, name_public, descr_public)

# Função para curtir uma publicação
def like_publi(client_id, publication_id):
    try:
        client = Client.get(Client.id == client_id)
        publication = Publication.get(Publication.id == publication_id)
        with db.atomic():
            Like.create(
                client=client,
                publication=publication
            )
        print(f"Publicação {publication_id} curtida pelo cliente {client_id}")
    except Exception as e:
        print(f"Erro ao curtir: {e}")

# Função para exibir todas as postagens e suas contagens de likes e seguidores
def view_all_posts():
    publications = Publication.select().order_by(Publication.created_at.desc())
    if publications.exists():
        print("Postagens disponíveis:\n")
        for publication in publications:
            try:
                client = publication.client
                like_count = publication.likes.count()
                follower_count = Follow.select().where(Follow.followee == client).count()
                print(f"ID: {publication.id}, Nome: {publication.name_publi}, Descrição: {publication.descr_publi}, Likes: {like_count}, Seguidores: {follower_count}")
            except Client.DoesNotExist:
                print(f"Cliente associado à publicação {publication.id} não encontrado.")
            except Exception as e:
                print(f"Erro ao exibir a publicação {publication.id}: {e}")
    else:
        print("Nenhuma postagem encontrada.")
    
    input("\nPressione Enter para voltar ao menu...")


# Função para exibir as postagens do usuário e das pessoas que ele segue
def view_user_posts_and_followed(logged_client):
    # Publicações do próprio usuário
    user_publications = Publication.select().where(Publication.client == logged_client).order_by(Publication.created_at.desc())

    # Publicações das pessoas que o usuário segue
    followed_publications = Publication.select().join(Client).join(Follow, on=(Client.id == Follow.followee)).where(Follow.follower == logged_client).order_by(Publication.created_at.desc())

    # Exibição das publicações do próprio usuário
    print("\nSuas Publicações:\n")
    if user_publications.exists():
        for publication in user_publications:
            like_count = publication.likes.count()
            print(f"ID: {publication.id}, Nome: {publication.name_publi}, Descrição: {publication.descr_publi}, Likes: {like_count}")
    else:
        print("Você ainda não tem publicações.")

    # Exibição das publicações das pessoas que o usuário segue
    print("\nPublicações das Pessoas que Você Segue:\n")
    if followed_publications.exists():
        for publication in followed_publications:
            like_count = publication.likes.count()
            print(f"ID: {publication.id}, Nome: {publication.name_publi}, Descrição: {publication.descr_publi}, Likes: {like_count}")
    else:
        print("Nenhuma publicação encontrada das pessoas que você segue.")
