import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import os
from dotenv import load_dotenv


 

def main():
    #Credenciais
    load_dotenv()
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET') 

    # Autenticação
    try: 
        credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        sp = spotipy.Spotify(client_credentials_manager=credentials)
        print('Autenticado com sucesso')
    except:
        print('Erro de Autenticação')


    artist_names = ['Raimundos', 'Capital Inicial', 'Supla']
    artists_info = []

    # Buscando informação de artista
    if len(artist_names) == 0:
        print('Não houve artista preenchido para busca')
    else:
        try:
            #Artista Detalhes
            for artist_name in artist_names:
                results = sp.search(q='artist:' + artist_name, type='artist')
                
                if results['artists']['items']:
                    artist = results['artists']['items'][0]
                    artist_info = {
                        'id': artist['id'],
                        'Nome do artista': artist['name'],
                        'Popularidade': artist['popularity'],
                        'Número_de_seguidores': artist['followers']['total'],
                        'Genero': artist['genres'],
                        'Imagem':artist['images'][0]['url'],
                        'Link do Spotify': artist['external_urls']['spotify'],
                        'Álbuns': []
                    }

                    # Albuns detalhes
                    albums = sp.artist_albums(artist['id'], album_type='album', limit=50)   
                    for album in albums['items']:
                        album_info = {
                            'Nome do álbum': album['name'],
                            'Data de lançamento': album['release_date'],
                            'Link do álbum': album['external_urls']['spotify']
                        }
                        artist_info['Álbuns'].append(album_info)

                    artists_info.append(artist_info)
                else:
                    print(f'Artista "{artist_name}" não encontrado.')

            df = pd.DataFrame(artists_info)

            file_path = os.getenv('FILE_PATH')
            if os.path.exists(file_path):
                os.remove(file_path)
            
            df.to_csv(file_path, index=False, encoding='utf-8')
            print(f"Sucesso: Processo de extração concluído")
        except:
            print(f"Error: Processo de extração não finalizado")

if __name__ == "__main__":
    main()
 
