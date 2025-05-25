from enum import Enum


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
