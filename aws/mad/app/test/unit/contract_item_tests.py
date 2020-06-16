import pytest
from pytest_mock import mocker

from app.src.contract_item import contract_item_api
from app.src.contract_item import contract_item_controller

def test_create_handler(mocker):
    quote_id = 1000
    mpan = 1111111111111
    known_response = None
    context = {}

    event = {
        "quote_id": quote_id,
        "mpan": mpan
    }

    mocker.patch.object(contract_item_controller, 'create')

    contract_item_controller.create.return_value = known_response

    response = contract_item_api.handler.create_handler(event=event, context=context)

    contract_item_controller.create.assert_called_once()

    contract_item_controller.create.assert_called_with(quote_id, mpan)

    assert(response == None)