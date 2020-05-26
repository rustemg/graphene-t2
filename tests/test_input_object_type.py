import graphene

from graphene_t2 import InputObjectType


class Parent(InputObjectType):
    field1 = graphene.Int()
    field2 = graphene.String()


class ChildAll(Parent):
    class T2Meta:
        required = {True: "__all__"}


class ChildByField(Parent):
    class T2Meta:
        required = {True: ["field2"]}


def test_required_all():
    assert ChildAll.field1.kwargs["required"]
    assert ChildAll.field2.kwargs["required"]


def test_required_by_field():
    assert not ChildByField.field1.kwargs.get("required", False)
    assert ChildByField.field2.kwargs["required"]
