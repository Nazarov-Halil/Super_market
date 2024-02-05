def upload_avatar_for_user(instance, filename):
    return f'/avatar/{instance.username}/{filename}'


def upload_products(instance, filename):
    # Проверка и фильтрация данных
    safe_title = instance.product.title.replace('/', '')  # Или любые другие символы, которые не должны быть в пути
    return f"products/{safe_title}/{filename}"
