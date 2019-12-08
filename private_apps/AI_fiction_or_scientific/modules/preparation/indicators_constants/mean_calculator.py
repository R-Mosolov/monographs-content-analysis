import fiction_indicators
import scientific_indicators


def calculate_mean():
    TEXT__SIGN_REL = (fiction_indicators.TEXT__SIGN_REL - scientific_indicators.TEXT__SIGN_REL) * 0.5
    SENTENCE__WORD = (fiction_indicators.SENTENCE__WORD - scientific_indicators.SENTENCE__WORD) * 0.5
    WORD__LETTER = (fiction_indicators.WORD__LETTER - scientific_indicators.WORD__LETTER) * 0.5
    TEXT__ADJECTIVE = (fiction_indicators.TEXT__ADJECTIVE - scientific_indicators.TEXT__ADJECTIVE) * 0.5
    TEXT__DIALOG = (fiction_indicators.TEXT__DIALOG - scientific_indicators.TEXT__DIALOG) * 0.5

    TEXT__MARKER_SKAZAL = (fiction_indicators.TEXT__MARKER_SKAZAL - scientific_indicators.TEXT__MARKER_SKAZAL) * 0.5
    TEXT__MARKER_SKAZALA = (fiction_indicators.TEXT__MARKER_SKAZALA - scientific_indicators.TEXT__MARKER_SKAZALA) * 0.5
    TEXT__MARKER_GOVORIT = (fiction_indicators.TEXT__MARKER_GOVORIT - scientific_indicators.TEXT__MARKER_GOVORIT) * 0.5
    TEXT__MARKER_GOVORIL = (fiction_indicators.TEXT__MARKER_GOVORIL - scientific_indicators.TEXT__MARKER_GOVORIL) * 0.5
    TEXT__MARKER_SPROSIL = (fiction_indicators.TEXT__MARKER_SPROSIL - scientific_indicators.TEXT__MARKER_SPROSIL) * 0.5

    if TEXT__SIGN_REL < 0:
        TEXT__SIGN_REL *= -1
    if SENTENCE__WORD < 0:
        SENTENCE__WORD *= -1
    if WORD__LETTER < 0:
        WORD__LETTER *= -1
    if TEXT__ADJECTIVE < 0:
        TEXT__ADJECTIVE *= -1
    if TEXT__DIALOG < 0:
        TEXT__DIALOG *= -1

    if TEXT__MARKER_SKAZAL < 0:
        TEXT__MARKER_SKAZAL *= -1
    if TEXT__MARKER_SKAZALA < 0:
        TEXT__MARKER_SKAZALA *= -1
    if TEXT__MARKER_GOVORIT < 0:
        TEXT__MARKER_GOVORIT *= -1
    if TEXT__MARKER_GOVORIL < 0:
        TEXT__MARKER_GOVORIL *= -1
    if TEXT__MARKER_SPROSIL < 0:
        TEXT__MARKER_SPROSIL *= -1

    return [round(TEXT__SIGN_REL, 2),
            round(SENTENCE__WORD, 2),
            round(WORD__LETTER, 2),
            round(TEXT__ADJECTIVE, 2),
            round(TEXT__DIALOG, 2),

            round(TEXT__MARKER_SKAZAL, 3),
            round(TEXT__MARKER_SKAZALA, 3),
            round(TEXT__MARKER_GOVORIT, 3),
            round(TEXT__MARKER_GOVORIL, 3),
            round(TEXT__MARKER_SPROSIL, 3)]

print(calculate_mean())
