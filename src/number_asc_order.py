from src.custom_stack_class import CustomStack

MIN_NUMBER = 1
MAX_NUMBER = 60


class NumberAscOrder:

    def sort(self, stack):
        """Coleta os números da Mega-Sena armazenados em `stack` e os retorna em ordem crescente.

        A pilha é consumida: todos os elementos são removidos com pop().
        """
        if not isinstance(stack, CustomStack):
            raise TypeError("stack deve ser uma CustomStack")

        numbers = []
        while not stack.is_empty():
            number = stack.pop()
            self._validate(number, numbers)
            numbers.append(number)

        return sorted(numbers)

    def _validate(self, number, collected):
        # bool é subclasse de int, então é rejeitado explicitamente
        if isinstance(number, bool) or not isinstance(number, int):
            raise ValueError(f"número da Mega-Sena inválido: {number!r}")
        if not MIN_NUMBER <= number <= MAX_NUMBER:
            raise ValueError(f"número da Mega-Sena fora do intervalo {MIN_NUMBER}-{MAX_NUMBER}: {number}")
        if number in collected:
            raise ValueError(f"número da Mega-Sena repetido: {number}")
