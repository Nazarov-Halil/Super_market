def upload_avatar_for_user(instance, filename):
    return f'/avatar/{instance.username}/{filename}'


def upload_products(instance, filename):
    safe_title = instance.product.title.replace('/', '')
    return f"products/{safe_title}/{filename}"
