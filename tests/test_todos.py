import factory.fuzzy

from pytodo.models import Todo, TodoState


def test_create_todo(client, token):
    response = client.post(
        '/todos/',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'title': 'Test todo',
            'description': 'Test todo description',
            'state': 'draft',
        },
    )
    assert response.json() == {
        'id': 1,
        'title': 'Test todo',
        'description': 'Test todo description',
        'state': 'draft',
    }


class TodoFactory(factory.Factory):
    class Meta:
        model = Todo

        title = factory.Faker('text')
        description = factory.Faker('text')
        state = factory.fuzzy.FuzzyChoice(TodoState)
        user_id = 1
