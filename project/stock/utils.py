def get_branch_slug(instance):
    return f"{instance.name}-{instance.manager.email.split('@')[0]}"  # -{str(instance.uid).split('-')[0]}"


def get_stock_slug(instance):
    return f"{instance.content_type}-{instance.object_id}"