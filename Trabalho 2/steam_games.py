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

MOST_REVIEWED_GAMES = [
    '620',
    '427520',
    '292030',
    '105600',
    '294100',
    '250900',
    '400',
    '413150',
    '10',
    '227300',
    '550',
    '460950',
    '48700',
    '253230',
    '219150',
    '238460',
    '264200',
    '213670',
    '646570',
    '252150',
    '698780',
    '424280',
    '736260',
    '220',
    '250320',
    '205100',
    '447530',
    '420530',
    '322330',
    '883710',
    '774171',
    '4000',
    '219740',
    '519860',
    '319630',
    '207610',
    '274190',
    '644560',
    '351640',
    '206440',
    '504230',
    '341800',
    '745880',
    '8930',
    '632360',
    '288160',
    '312990',
    '433340',
    '221640',
    '337340',
    '425580',
    '367520',
    '3590',
    '70',
    '203160',
    '851100',
    '212680',
    '206190',
    '420110',
    '204360',
    '240',
    '602520',
    '412830',
    '391540',
    '214560',
    '22380',
    '55230',
    '268910',
    '400910',
    '217980',
    '508440',
    '683320',
    '238320',
    '239030',
    '692850',
    '261570',
    '557340',
    '1118200',
    '107100',
    '387290',
    '247080',
    '8870',
    '435150',
    '113200',
    '943700',
    '339800',
    '588650',
    '367580',
    '432350',
    '413410',
    '312530',
    '557600',
    '531510',
    '324160',
    '35140',
    '1055540',
    '942970',
    '433950',
    '311690',
    '1250',
    '250760',
    '450540',
    '653530',
    '457140',
    '331470',
    '639790',
    '1064610',
    '223470',
    '511470',
    '996580',
    '261030',
    '236090',
    '499440',
    '413420',
    '1070710',
    '597220',
    '35720',
    '304430',	
    '558990',	
    '287980',	
    '200260',	
    '221380',	
    '9420',
    '242680',	
    '264710',	
    '333600',	
    '282140',	
    '881100',	
    '257510',	
    '411960',	
    '72850',
    '732430',	
    '102600',	
    '360740',	
    '440',
    '992310',	
    '260230',
    '41700',
    '322170',
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

def get_most_reviewed_games(n=len(MOST_REVIEWED_GAMES)):

    # If n is below 1, than set n to 0
    if n < 1: n = 0
    return MOST_REVIEWED_GAMES[:n]

'''
Function thar returns all the reviewed games
'''
def get_all_reviewed_games():

    # concat all the games
    games = []
    games.extend(TOP_GOOD_REVIEWS)
    games.extend(TOP_BAD_REVIEWS)

    return games