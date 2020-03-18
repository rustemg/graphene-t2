# Disclaimer
Проект находится на ранней стадии разработки

# Как пользоваться?

## Обязательные поля в инпутах
```python
import graphene
from graphene_metafora import InputObjectType

class AddSomethingInput(InputObjectType):
    field1 = graphene.String(required=True)
    field2 = graphene.String(required=True)

class EditSomethingInput(AddSomethingInput):
    class Metafora:
        required = {
            False: '__all__', # или список полей
            True: ['id'],
        }
    
    id = graphene.ID()
```

### Примечания
* нет поддержки `graphene.Argument`
* порядок ключей (`True`, `False`) в параметре `required` важен. Изменения применяются в порядке их объявления


## Документирование изменений (`changes.py`)
Автоматически изменяет описание полей. Может использоваться для генерации документации.
```python
import graphene
from graphene_metafora import InputObjectType
from graphene_metafora.features.changes import Alter, Deprecate

class SomeInputType(InputObjectType):
    class Metafora:
        changes = [
            Deprecate('legacy_field1', '03/20', replaced_by='new_field1'),
            Deprecate('legacy_field2', '02/20', comment='Не используется'),
            Alter('new_field1', '03/20', required=True),
        ]

    legacy_field1 = graphene.String()
    legacy_field2 = graphene.String()
    new_field1 = graphene.String()

```


## Сортировка (`ordering.py`)
В классе-нследнике `ObjectType` нужно объявить класс `Metafora`.
Внутри него можно создать две переменные:
1. `can_order_by` - обязательный, список с названием полей, по которым можно производить сортировку;
2. `default_ordering` - необязательный, сортировка по-умолчанию, строка или список строк с названием полей.

Примеры:
```python
class Model1Type(DjangoObjectType):
       class Metafora:
           can_order_by = ['id']


class Model2Type(DjangoObjectType):
       class Metafora:
           can_order_by = ['id']
           default_ordering = 'id' # или '-id'


class Model3Type(DjangoObjectType):
       class Metafora:
           can_order_by = ['id', 'name', 'date_created']
           default_ordering = '-date_created', 'name' # или ['-date_created', 'name']
```

Класс с объявлением методов нужно отнаследовать от `graphene_metafora.Queries`, объявить вложенный класс `Metafora`.
Внутри объявить переменную `enable_ordering_for`. 

Возможны два вида значения:
1. `__auto__` - включает возможность сортировки, для методов для которых это возможно сделать;
2. список с названием полей

Ресолверы в качестве аргумента должны принимать `**kwargs` или `sort_by`.


```python
from graphene_metafora import Queries


class Query1(Queries):
    class Metafora:
        enable_ordering_for = '__auto__'
    
    items = graphene.List(Model1Type)

    def resolve_items(self, info, **kwargs):
        pass
    


class Query2(Queries):
    class Metafora:
        enable_ordering_for = ['items']
    
    items = graphene.List(Model1Type)

    def resolve_items(self, info, sort_by):
        pass
```


### Примечания
* Нет поддержки случаев, когда название поля в модели отличается от названия в API;
* Нет возможности сортировать по полям вложенных структур;
