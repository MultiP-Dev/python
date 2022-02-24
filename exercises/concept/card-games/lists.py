def get_rounds(number):
    """Create a list containing the current and next two round numbers.

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """

    pass


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate a list of round numbers with the other, joining them into one bigger list.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    pass


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    pass


def card_average(hand):
    """Get the average of the list of card values.

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    pass


def approx_average_is_average(hand):
    """Get the average of the list of card values using either the first and last index values, or the 'middle' card.

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """

    pass


def average_even_is_average_odd(hand):
    """Check if the even indexed card values and odd indexed card values share the same average.

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    pass


def maybe_double_last(hand):
    """Check if the hand has a Jack at its last index -- if so, its value is multiplied by two.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    pass
