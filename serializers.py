from marshmallow import Schema, fields, pprint

class UserSchema(Schema):
    id      =   fields.Int()
    username = fields.Str()
    email    = fields.Str()
    created  = fields.DateTime()
    bio      = fields.Str()