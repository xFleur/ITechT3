from GuessWord import GuessWord

RANDOM_NAME_1 = GuessWord('henk',
                          [
                              "Hij is kaal",
                              "Zijn achternaam is maathuis",
                              "Hij is een steen",
                              "Hij heeft een echte opa naam"
                              "Zijn step is geel met blauwe wielen (vet lelijk)",
                          ]
                          )
RANDOM_NAME_2 = GuessWord('barry',
                          [
                              "Hij is super hip",
                              "Hij houdt van disco dip op zijn ijsjes",
                              "Hij heeft nog nooit op een duikplank gestaan",
                              "Hij kent 7 verschillende katten feitjes",
                              "Zijn step is paars met rode wielen",
                          ]
                          )

RANDOM_COLOR_1 = GuessWord('paars',
                           [
                               "Het is niet geel",
                               "Het is niet oranje",
                               "Het lijkt op laars",
                               "Zijn step is rood met rode wielen"
                           ]
                           )

GAME_TOPIC_NAMES = [RANDOM_NAME_1, RANDOM_NAME_2]
GAME_TOPIC_COLORS = [RANDOM_COLOR_1]

KID_TOPICS_PLAYGROUND = ["names", "colors"]
KID_TOPICS_HOME = ["television", "sheep"]
ADOLESCENT_TOPICS_NETFLIX = ["alcohol", "drugs"]
ADOLESCENT_TOPICS_MUSIC = ["drugs", "drugs"]
ADULT_TOPICS_PIZZA = ["you", "do", "not", "want", "to", "know"]
ADULT_TOPICS_DINNER = ["you", "do", "", "want", "to", "know"]
