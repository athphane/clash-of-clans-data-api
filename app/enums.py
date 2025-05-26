from enum import Enum
from operator import inv


class TableType(str, Enum):
    details = "details"
    stats = "stats"


class Troops(str, Enum):
    barbarian = "barbarian"
    archer = "archer"
    giant = "giant"
    goblin = "goblin"
    wall_breaker = "wall_breaker"
    balloon = "balloon"
    wizard = "wizard"
    healer = "healer"
    dragon = "dragon"
    pekka = "pekka"
    baby_dragon = "baby_dragon"
    miner = "miner"
    electro_dragon = "electro_dragon"
    yeti = "yeti"
    dragon_rider = "dragon_rider"
    electro_titan = "electro_titan"
    root_rider = "root_rider"
    thrower = "thrower"
    minion = "minion"
    hog_rider = "hog_rider"
    valkyrie = "valkyrie"
    golem = "golem"
    witch = "witch"
    lava_hound = "lava_hound"
    bowler = "bowler"
    ice_golem = "ice_golem"
    headhunter = "headhunter"
    apprentice_warden = "apprentice_warden"
    druid = "druid"
    furnace = "furnace"

class Spells(str, Enum):
    lightning = "lightning_spell"
    heal = "heal_spell"
    rage = "rage_spell"
    jump = "jump_spell"
    freeze = "freeze_spell"
    clone = "clone_spell"
    invisibility = "invisibility_spell"
    recall = "recall_spell"
    revive = "revive_spell"
    poison = "poison_spell"
    earthquake = "earthquake_spell"
    haste = "haste_spell"
    skeleton = "skeleton_spell"
    bats = "bat_spell"
    overgrowth = "overgrowth_spell"
    