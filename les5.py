import requests # взаимодействие с сетью
import os

url = 'https://geekbrains.ru/'

#response = requests.get(url)
#print(response.text)

#os.mkdir('test_mkdir')
#os.rmdir('test_mkdir')

print(os.listdir())
print(os.path.isdir('.gitignore')) # папка или нет

if __name__ == '__main__':
    pass

print(__name__)

def get_htm():
    url='https://geekbrains.ru/'
    response =requests.get(url)
    return response.text


def get_image(url):
    response = requests.get(url)
    return response.content

def save_image(file_path, image_bytes):
    with open(file_path, 'wb') as file:
        file.write(image_bytes)


def save_html_to_file(file_path, htm_text):
    with open(file_path, 'w', encoding='UTF-8') as file:
        file.write(html_text)


if __name__ == '__main__':
    img_url = 'https://arsenal-info.ru/img/1198779448/img_1.jpg'
    file_name = 'temp_gb_main.html'
    file_folder = os.path.dirname(__file__)
    file_path = os.path.join(file_folder, file_name)
    image_path = os.path.join(file_folder, 'img_1.jpg')
    html_text = get_htm()
    #save_html_to_file(file_path,html_text)

    img_bytes = get_image(img_url)
    save_image(image_path, img_bytes)

