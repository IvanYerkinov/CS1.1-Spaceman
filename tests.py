import spaceman


def test_guessLetterTrue():
    cl = spaceman.gameEn("test")
    assert not cl.guessLetter('t')


def test_guessLetterFalse():
    cl = spaceman.gameEn("test")
    assert cl.guessLetter("aa") is True


def test_badGuessIncrease():
    cl = spaceman.gameEn("test")
    cl.guessLetter('a')
    assert cl.nIncGuess == 1


def test_guessLoadWord():
    cl = spaceman.gameEn("test")
    assert len(cl.word) == 4


test_guessLoadWord()
test_guessLetterTrue()
test_guessLetterFalse()
test_badGuessIncrease()
