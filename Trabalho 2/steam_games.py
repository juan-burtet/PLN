'''
25 WORST REVIEWED GAMES
'''
TOP_BAD_REVIEWS = [
    "201510", # Flatout 3
    "267600", # Airport Simulator 2014
    "292630", # Uriel's Chasm
    "47700", # Command and Conquer 4: Tiberian Twilight
    "246090", # Spacebase DF-9
    "227160", # Kinetic Void
    "412400", # GASP
    "357770", # The District
    "282560", # RollerCoaster Tycoon World
    "247950", # Sacred 3
    "221020", # Towns
    "232810", # Godus
    "730310", # DYNASTY WARRIORS 9
    "390340", # Umbrella Corps
    "271500", # Sniper Art of Victory
    "47400", # Stronghold 3
    "577800", # NBA 2K18
    "352950", # Better Late Than DEAD
    "1089350", # NBA 2K20
    "409510", # Genesis Online
    "273770", # Game Tycoon 1.5
    "313010", # Cities XXL
    "344040", # Voxelized
    "330350", # Robotex
    "410210", # Ampersand
]

'''
25 BEST REVIEWED GAMES
'''
TOP_GOOD_REVIEWS = [
    "620", # Portal 2
    "292030", # The Witcher 3: Wild Hunt
    "105600", # Terraria
    "427520", # Factorio
    "413150", # Stardew Valley
    "550", # Left 4 Dead 2
    "227300", # Euro Truck Simulator 2
    "10", # Counter Strike
    "250900", # The Binding of Isaac: Rebirth
    "400", # Portal
    "294100", # RimWorld
    "48700", # Mount & Blade: Warband
    "4000", # Garry's Mod
    "698780", # Doki Doki Literature Club
    "219150", # Hotline Miami
    "238460", # BattleBlock Theater
    "322330", # Don't Starve Together
    "253230", # A Hat in Time
    "220", # Half-Life 2
    "213670", # South Park: The Stick of Truth
    "646570", # Slay the Spire
    "319630", # Life is Strange
    "460950", # Katana ZERO
    "205100", # Dishonored
    "219740", # Don't Starve
]

'''
Function that returns the n bad rewiewed games
'''
def get_bad_reviewed_games(n=len(TOP_BAD_REVIEWS)):

    # If n is below 1, than set n to 0
    if n < 1: n = 0
    return TOP_BAD_REVIEWS[:n]

'''
Function that returns the n good reviewed games
'''
def get_good_reviewed_games(n=len(TOP_BAD_REVIEWS)):

    # If n is below 1, than set n to 0
    if n < 1: n = 0
    return TOP_GOOD_REVIEWS[:n]

'''
Function thar returns all the reviewed games
'''
def get_all_reviewed_games():

    # concat all the games
    games = []
    games.extend(TOP_GOOD_REVIEWS)
    games.extend(TOP_BAD_REVIEWS)

    return games

"brazilian"