import game_starter


def test_is_word_guessed():
    assert game_starter.is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']) == False
    assert game_starter.is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']) == True
    assert game_starter.is_word_guessed('carrot', ['b', 'g', 'd', 'z', 'w', 'y', 'v', 'm', 'i', 'k']) == False
    assert game_starter.is_word_guessed('lettuce', ['k', 'v', 'a', 'e', 'n', 'd', 'b', 'f', 'u', 'c']) == False
    assert game_starter.is_word_guessed('pineapple', []) == False
    assert game_starter.is_word_guessed('mangosteen', ['z', 'x', 'q', 'm', 'a', 'n', 'g', 'o', 's', 't', 'e', 'e', 'n']) == True


def test_get_guessed_word():
    assert game_starter.get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']) == '_ pp_ e'
    assert game_starter.get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']) == 'durian'
    assert game_starter.get_guessed_word('grapefruit', ['k', 'm', 'b', 'j', 'e', 'w', 's', 'z', 'u', 'x']) == '_ _ _ _ e_ _ u_ _ '
    assert game_starter.get_guessed_word('coconut', ['w', 'l', 'i', 'p', 'c', 'u', 'j', 'h', 'v', 'z']) == 'c_ c_ _ u_ '
    assert game_starter.get_guessed_word('banana', []) == '_ _ _ _ _ _ '
    assert game_starter.get_guessed_word('broccoli', ['e', 'c', 'g', 'u', 'r', 'x', 's', 'a', 'p', 'j']) == '_ r_ cc_ _ _ '


def test_get_available_letters():
    assert game_starter.get_available_letters(['e', 'i', 'k', 'p', 'r', 's']) == 'abcdfghjlmnoqtuvwxyz'
    assert game_starter.get_available_letters([]) == 'abcdefghijklmnopqrstuvwxyz'
    assert game_starter.get_available_letters(['r', 'y', 'd', 'u', 't']) == 'abcefghijklmnopqsvwxz'
    assert game_starter.get_available_letters(['t', 'w', 'v', 'b', 'k', 'n']) == 'acdefghijlmopqrsuxyz'
    assert game_starter.get_available_letters(['a']) == 'bcdefghijklmnopqrstuvwxyz'
    assert game_starter.get_available_letters(['p', 'r', 'f', 'd', 'k', 'h', 'c', 'a', 'i', 'y', 'w', 'b']) == 'egjlmnoqstuvxz'