def sqlalchemy_entity_to_dict(entity):
    if not entity:
        return None
    return {column.name: getattr(entity, column.name) for column in entity.__table__.columns}