import requests
import pandas as pd
from io import StringIO


#           | multiplier matrix 18*18
#           → defence →                                                                                     # ↓ attack ↓
matrix = [  # |nor |fir |wat |ele |gra |ice |fig |poi |gro |fly |psy |bug |roc |gho |dra |dar |ste |fai
              [1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0.5, 0,   1,   1,   0.5, 1],     # normal
              [1,   0.5, 0.5, 1,   2,   2,   1,   1,   1,   1,   1,   2,   0.5, 1,   0.5, 1,   2,   1],     # fire
              [1,   1,   0.5, 1,   0.5, 1,   1,   1,   2,   1,   1,   1,   2,   1,   0.5, 1,   1,   1],     # water
              [1,   1,   2,   0.5, 0.5, 1,   1,   1,   0,   2,   1,   1,   1,   1,   0.5, 1,   1,   1],     # electric
              [1,   0.5, 2,   1,   0.5, 1,   1,   0.5, 2,   0.5, 1,   0.5, 2,   1,   0.5, 1,   0.5, 1],     # grass
              [1,   0.5, 0.5, 1,   2,   0.5, 1,   1,   2,   2,   1,   1,   1,   1,   2,   1,   0.5, 1],     # ice
              [2,   1,   1,   1,   1,   2,   1,   0.5, 1,   0.5, 0.5, 0.5, 2,   0,   1,   2,   2,   0.5],   # fighting
              [1,   1,   1,   1,   2,   1,   1,   0.5, 0.5, 1,   1,   1,   0.5, 0.5, 1,   1,   0,   2],     # poison
              [1,   2,   1,   2,   0.5, 1,   1,   2,   1,   0,   1,   0.5, 2,   1,   1,   1,   2,   1],     # ground
              [1,   1,   1,   0.5, 2,   1,   2,   1,   1,   1,   1,   2,   0.5, 1,   1,   1,   0.5, 1],     # flying
              [1,   1,   1,   1,   1,   1,   2,   2,   1,   1,   0.5, 1,   1,   1,   1,   0,   0.5, 1],     # psychic
              [1,   0.5, 1,   1,   2,   1,   0.5, 0.5, 1,   0.5, 2,   1,   1,   0.5, 1,   2,   0.5, 0.5],   # bug
              [1,   2,   1,   1,   1,   2,   0.5, 1,   0.5, 2,   1,   2,   1,   1,   1,   1,   0.5, 1],     # rock
              [0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   1,   1,   2,   1,   0.5, 1,   1],     # ghost
              [1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   1,   0.5, 0],     # dragon
              [1,   1,   1,   1,   1,   1,   0.5, 1,   1,   1,   2,   1,   1,   2,   1,   0.5, 1,   0.5],   # dark
              [1,   0.5, 0.5, 0.5, 1,   2,   1,   1,   1,   1,   1,   1,   2,   1,   1,   1,   0.5, 2],     # steel
              [1,   0.5, 1,   1,   1,   1,   2,   0.5, 1,   1,   1,   1,   1,   1,   2,   2,   0.5, 1]      # fairy
          ]

# Pokemon types
types = {
    "Normal"   : 0,
    "Fire"     : 1,
    "Water"    : 2,
    "Electric" : 3,
    "Grass"    : 4,
    "Ice"      : 5,
    "Fighting" : 6,
    "Poison"   : 7,
    "Ground"   : 8,
    "Flying"   : 9,
    "Psychic"  : 10,
    "Bug"      : 11,
    "Rock"     : 12,
    "Ghost"    : 13,
    "Dragon"   : 14,
    "Dark"     : 15,
    "Steel"    : 16,
    "Fairy"    : 17
}

# Types for special attacks
special_attack = [
    "Water",
    "Grass",
    "Fire",
    "Ice",
    "Electric",
    "Psychic"
]


# def calculate multiplier
def multiplier(attack_type, defence_type):
    return matrix[types[attack_type]][types[defence_type]]


# def find the best multiplier for normal or dual type pokemon
def best_multiplier(pokemon_attack, pokemon_defend):

    mul_1_1, mul_1_2, mul_2_1, mul_2_2, = 1, 1, 1, 1
    stab_1, stab_2, = 1, 1

    mul_1_1 = multiplier(pokemon_attack.TYPE1, pokemon_defend.TYPE1)
    stab_1 = 1.5 if pokemon_attack.TYPE1 == pokemon_defend.TYPE1 else 1

    if pd.notnull(pokemon_attack.TYPE2) and pd.isnull(pokemon_defend.TYPE2):  # pokemon_1 is dual type
        mul_2_1 = multiplier(pokemon_attack.TYPE2, pokemon_defend.TYPE1)
        stab_2 = 1.5 if pokemon_attack.TYPE2 == pokemon_defend.TYPE1 else 1
        return (pokemon_attack.TYPE1, mul_1_1 * stab_1)  \
            if mul_1_1 * stab_1 >= mul_2_1 * stab_2 \
            else (pokemon_attack.TYPE2, mul_2_1 * stab_2)
    if pd.notnull(pokemon_defend.TYPE2): # pokemon_2 is dual type
        mul_1_2 = multiplier(pokemon_attack.TYPE1, pokemon_defend.TYPE2)
        stab_1 = 1.5 if pokemon_attack.TYPE1 == pokemon_defend.TYPE2 else stab_1
        if pd.notnull(pokemon_attack.TYPE2): # both are dual type
            mul_2_2 = multiplier(pokemon_attack.TYPE1, pokemon_defend.TYPE2)
            stab_2 = 1.5 if pokemon_attack.TYPE2 == pokemon_defend.TYPE2 else stab_2
            return (pokemon_attack.TYPE1, mul_1_1 * mul_1_2 * stab_1) \
                if mul_1_1 * mul_1_2 * stab_1 >= mul_2_1 * mul_2_2 * stab_2 \
                else (pokemon_attack.TYPE2, mul_2_1 * mul_2_2 * stab_2)
        return pokemon_attack.TYPE1, mul_1_1 * mul_1_2 * stab_1
    return pokemon_attack.TYPE1, mul_1_1 * stab_1


# calculate damage score
# desc: calculates best attack damage
#       an attacking pokemon can deal
#       against the defending pokemon
def score(pokemon_attack, pokemon_defend):

    attack_type, mult = best_multiplier(pokemon_attack, pokemon_defend)

    special = False
    if attack_type in special_attack:
        special = True

    attack = pokemon_attack.SP_ATK if special else pokemon_attack.ATK
    defence = pokemon_defend.SP_DEF if special else pokemon_defend.DEF

    # simplified damage formula with given data
    total = (attack/defence) * mult
    return total


def main():

    gist_url = "https://gist.github.com/simsketch/1a029a8d7fca1e4c142cbfd043a68f19"
    raw_url = gist_url.replace("gist.github.com", "gist.githubusercontent.com") + "/raw"
    response = requests.get(raw_url)

    if response.status_code == 200:
        print("Gist Content:\n")
        data = StringIO(response.text)
        df = pd.read_csv(data, usecols=range(22), skipfooter=7, engine='python')
        # last seven lines of data removed as they
        # have more fields than actual columns

        pokemon_count = len(df.index)

        damage_score = []

        for row_x in df.itertuples():         # attacker
            x_total = 0
            for row_y in df.itertuples():     # defender
                print(row_y.NAME)
                x_total += score(row_x, row_y)

            # takes total best possible damage
            # by attacking (X) pokemon and divides
            # it by pokemon count
            damage_score.append(x_total/pokemon_count)

        df['DAMAGE_SCORE'] = damage_score

        df.to_csv('output.csv', index=False)
        df.to_excel('output.xlsx', index=False)

    else:
        print(f"Failed to fetch gist. Status code: {response.status_code}")


if __name__ == "__main__":
    main()
