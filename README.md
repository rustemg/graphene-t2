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
