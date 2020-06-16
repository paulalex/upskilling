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

def test_read_handler(mocker):
    contract_item_id = 1000
    known_response = {
        "contract_item_id": contract_item_id,
        "quote_id": 100,
        "mpan": 2222222222222
    }

    context = {}

    event = {
        "contract_item_id": contract_item_id
    }

    mocker.patch.object(contract_item_controller, 'read')

    contract_item_controller.read.return_value = known_response

    response = contract_item_api.handler.read_handler(event=event, context=context)

    contract_item_controller.read.assert_called_once()

    contract_item_controller.read.assert_called_with(contract_item_id)

    assert(response == known_response)

def test_read_all_handler(mocker):
    known_response = [
        {
            "contract_item_id": 1000,
            "quote_id": 100,
            "mpan": 2222222222222
        }, {
            "contract_item_id": 1001,
            "quote_id": 101,
            "mpan": 3333333333333
        }
    ]

    context = {}

    event = {}

    mocker.patch.object(contract_item_controller, 'read_all')

    contract_item_controller.read_all.return_value = known_response

    response = contract_item_api.handler.read_all_handler(event=event, context=context)

    contract_item_controller.read_all.assert_called_once()

    contract_item_controller.read_all.assert_called_with()

    assert(response == known_response)

def test_update_handler(mocker):
    contract_item_id = 1000
    mpan = 4444444444444
    known_response = None

    context = {}

    event = {
        "contract_item_id": contract_item_id,
        "mpan": mpan
    }

    mocker.patch.object(contract_item_controller, 'update')

    contract_item_controller.update.return_value = known_response

    response = contract_item_api.handler.update_handler(event=event, context=context)

    contract_item_controller.update.assert_called_once()

    contract_item_controller.update.assert_called_with(contract_item_id, mpan)

    assert(response == known_response)

def test_delete_handler(mocker):
    contract_item_id = 1000
    known_response = None

    context = {}

    event = {
        "contract_item_id": contract_item_id
    }

    mocker.patch.object(contract_item_controller, 'delete')

    contract_item_controller.delete.return_value = known_response

    response = contract_item_api.handler.delete_handler(event=event, context=context)

    contract_item_controller.delete.assert_called_once()

    contract_item_controller.delete.assert_called_with(contract_item_id)

    assert(response == known_response)