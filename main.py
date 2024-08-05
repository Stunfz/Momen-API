from MomentAPI import MomentAPI

api_key = ""  # Ваш API-ключ
api = MomentAPI(api_key)

# Генерация текста
text_response = api.generate_text("")
print(text_response)

# Генерация изображения
image_response = api.generate_image("")
print(image_response)