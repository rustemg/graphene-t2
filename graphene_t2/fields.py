import ast

import graphene


class ObjectID(graphene.ID):
    parse_value = int
