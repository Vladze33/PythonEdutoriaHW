from functools import reduce

class ListOperations:
    @staticmethod
    def sum(numbers):
        return reduce(ListOperations.sum_numeric_parse, numbers)

    @staticmethod
    def sum_numeric_parse(sum, val):
        try:
            return sum + float(val)
        # TODO: Handle another types
        # if isinstance(val, (tuple, list)):
        except Exception as e:
            raise(e)
