""" seriesproduct.py
Project euler #8.
Find the largest 13-digit product of a sequence in a
1000 digit number
"""

NM_STRING = ('731671765313306249192251196744265747423553'
             '491949349698352031277450632623957831801698'
             '480186947885184385861560789112949495459501'
             '737958331952853208805511125406987471585238'
             '630507156932909632952274430435576689664895'
             '044524452316173185640309871112172238311362'
             '229893423380308135336276614282806444486645'
             '238749303589072962904915604407723907138105'
             '158593079608667017242712188399879790879227'
             '492190169972088809377665727333001053367881'
             '220235421809751254540594752243525849077116'
             '705560136048395864467063244157221553975369'
             '781797784617406495514929086256932197846862'
             '248283972241375657056057490261407972968652'
             '414535100474821663704844031998900088952434'
             '506585412275886668811642717147992444292823'
             '086346567481391912316282458617866458359124'
             '566529476545682848912883142607690042242190'
             '226710556263211111093705442175069416589604'
             '080719840385096245544436298123098787992724'
             '428490918884580156166097919133875499200524'
             '063689912560717606058861164671094050775410'
             '022569831552000559357297257163626956188267'
             '0428252483600823257530420752963450')
NUM = int(NM_STRING)


def series_product(N, l):
    series = str(N).split('0')
    largest = 0
    for x in series:
        if len(x) < l:
            continue
        while len(x) >= l:
            i = prod(x[:l])
            if i > largest:
                largest = i
                ans = x[:l]
            x = x[1:]
    return (largest, ans)


def prod(s):
    total = 1
    for i in list(s):
        total = total * int(i)
    return total


if __name__ == "__main__":
    print(series_product(NUM, 4))
    print(series_product(NUM, 13))