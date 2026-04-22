import webbrowser

music_links = {

    "happy": "https://www.youtube.com/watch?v=pIvf9bOPXIw&list=RDpIvf9bOPXIw&start_radio=1",
    "sad": "https://www.youtube.com/playlist?list=PLHuHXHyLu7BGi-vR7X6j_xh_Tt9wy7pNA",
    "angry": "https://www.youtube.com/watch?v=A3NTY8AjzK8&list=RDA3NTY8AjzK8&start_radio=1",
    "neutral": "https://www.youtube.com/watch?v=XTp5jaRU3Ws&list=RDEMj0weLcfSL_fmHFYGkc7UEQ&start_radio=1"

}


def recommend_music(emotion):

    if emotion in music_links:
        link = music_links[emotion]

    else:
        link = music_links["neutral"]

    webbrowser.open(link)