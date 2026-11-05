import random

import pytest

from src.custom_stack_class import CustomStack
from src.number_asc_order import NumberAscOrder

MEGA_SENA_SIZE = 6


def mock_stack_with(mocker, drawn_numbers):
    """CustomStack mockada contendo `drawn_numbers` na ordem do sorteio (o último sorteado fica no topo)."""
    stack = mocker.Mock(spec=CustomStack)
    stack.size.return_value = len(drawn_numbers)
    stack.is_empty.side_effect = [False] * len(drawn_numbers) + [True]
    stack.pop.side_effect = list(reversed(drawn_numbers))
    return stack


def draw_numbers():
    return random.sample(range(1, 61), MEGA_SENA_SIZE)


class TestNumberAscOrder:
    """Casos de teste da classe NumberAscOrder."""

    # --- Cenário obrigatório 1: pilha de 6 posições com os 6 números sorteados (aleatoriamente) ---

    def test_sort_returns_drawn_numbers_in_ascending_order(self, mocker):
        drawn = draw_numbers()
        stack = mock_stack_with(mocker, drawn)

        result = NumberAscOrder().sort(stack)

        assert result == sorted(drawn)
        assert isinstance(result, list)
        assert stack.pop.call_count == MEGA_SENA_SIZE

    def test_sort_with_real_custom_stack(self):
        drawn = draw_numbers()
        stack = CustomStack(MEGA_SENA_SIZE)
        for number in drawn:
            stack.push(number)

        assert NumberAscOrder().sort(stack) == sorted(drawn)

    # --- Cenário obrigatório 2: pilha de 6 posições, vazia ---

    def test_sort_empty_stack_returns_empty_list(self, mocker):
        stack = mock_stack_with(mocker, [])

        assert NumberAscOrder().sort(stack) == []
        stack.pop.assert_not_called()

    def test_sort_with_real_empty_custom_stack(self):
        assert NumberAscOrder().sort(CustomStack(MEGA_SENA_SIZE)) == []

    # --- Verificações de entrada ---

    @pytest.mark.parametrize("invalid", [None, [3, 1, 2], "123", 42])
    def test_sort_rejects_non_custom_stack(self, invalid):
        with pytest.raises(TypeError):
            NumberAscOrder().sort(invalid)

    @pytest.mark.parametrize("bad_number", [0, 61, -5, 10.5, "7", True, None])
    def test_sort_rejects_invalid_mega_sena_number(self, mocker, bad_number):
        stack = mock_stack_with(mocker, [4, 15, bad_number, 23, 42, 59])

        with pytest.raises(ValueError):
            NumberAscOrder().sort(stack)

    def test_sort_rejects_repeated_numbers(self, mocker):
        stack = mock_stack_with(mocker, [4, 15, 15, 23, 42, 59])

        with pytest.raises(ValueError):
            NumberAscOrder().sort(stack)
