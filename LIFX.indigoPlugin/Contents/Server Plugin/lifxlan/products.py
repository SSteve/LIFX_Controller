# coding=utf-8
product_map = {1: "LIFX Original 1000",
               3: "LIFX Color 650",
               10: "LIFX White 800 (Low Voltage)",
               11: "LIFX White 800 (High Voltage)",
               15: "LIFX Color 1000",
               18: "LIFX White 900 BR30 (Low Voltage)",
               19: "LIFX White 900 BR30 (High Voltage)",
               20: "LIFX Color 1000 BR30",
               22: "LIFX Color 1000",
               27: "LIFX A19",
               28: "LIFX BR30",
               29: "LIFX A19 Night Vision",
               30: "LIFX BR30 Night Vision",
               31: "LIFX Z",
               32: "LIFX Z",
               36: "LIFX Downlight",
               37: "LIFX Downlight",
               38: "LIFX Beam",
               39: "LIFX Downlight White To Warm",
               40: "LIFX Downlight",
               43: "LIFX A19",
               44: "LIFX BR30",
               45: "LIFX A19 Night Vision",
               46: "LIFX BR30 Night Vision",
               49: "LIFX Mini Color",
               50: "LIFX Mini White To Warm",
               51: "LIFX Mini White",
               52: "LIFX GU10",
               53: "LIFX GU10",
               55: "LIFX Tile",
               57: "LIFX Candle",
               59: "LIFX Mini Color",
               60: "LIFX Mini White To Warm",
               61: "LIFX Mini White",
               62: "LIFX A19",
               63: "LIFX BR30",
               64: "LIFX A19 Night Vision",
               65: "LIFX BR30 Night Vision",
               66: "LIFX Mini White",
               68: "LIFX Candle",
               70: "LIFX Switch",
               81: "LIFX Candle White To Warm",
               82: "LIFX Filament Clear",
               85: "LIFX Filament Amber",
               87: "LIFX Mini White",
               88: "LIFX Mini White",
               89: "LIFX Switch",
               90: "LIFX Clean",
               91: "LIFX Color",
               92: "LIFX Color",
               93: "LIFX Color A19 1100lm",
               94: "LIFX BR30",
               96: "LIFX Candle White To Warm",
               97: "LIFX A19",
               98: "LIFX BR30",
               99: "LIFX Clean",
               100: "LIFX Filament Clear",
               101: "LIFX Filament Amber",
               109: "LIFX A19 Night Vision",
               110: "LIFX BR30 Night Vision",
               111: "LIFX A19 Night Vision"
               }

# Identifies which products are lights.
light_products = [1, 3, 10, 11, 15, 18, 19, 20, 22, 27, 28, 29, 30, 31, 32, 36, 37, 38, 39, 40, 43, 44, 45, 46, 49, 50, 51, 52, 53, 55, 57, 59, 60, 61, 62, 63, 64, 65, 66, 68, 81, 82, 85, 87, 88, 90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 109, 110, 111]

# Identifies which products are switches.
switch_products = [70, 89]

features_map = {1: {                    # LIFX Original 1000
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                3: {                    # LIFX Color 650
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                10: {                    # LIFX White 800 (Low Voltage)
                    "color": False,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2700,
                    "max_kelvin": 6500,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                11: {                    # LIFX White 800 (High Voltage)
                    "color": False,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2700,
                    "max_kelvin": 6500,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                15: {                    # LIFX Color 1000
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                18: {                    # LIFX White 900 BR30 (Low Voltage)
                    "color": False,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                19: {                    # LIFX White 900 BR30 (High Voltage)
                    "color": False,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                20: {                    # LIFX Color 1000 BR30
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                22: {                    # LIFX Color 1000
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                27: {                    # LIFX A19
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                28: {                    # LIFX BR30
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                29: {                    # LIFX A19 Night Vision
                    "color": True,
                    "temperature": True,
                    "infrared": True,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                30: {                    # LIFX BR30 Night Vision
                    "color": True,
                    "temperature": True,
                    "infrared": True,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                31: {                    # LIFX Z
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": True,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                32: {                    # LIFX Z
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": True,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                36: {                    # LIFX Downlight
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                37: {                    # LIFX Downlight
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                38: {                    # LIFX Beam
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": True,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                39: {                    # LIFX Downlight White To Warm
                    "color": False,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                40: {                    # LIFX Downlight
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                43: {                    # LIFX A19
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                44: {                    # LIFX BR30
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                45: {                    # LIFX A19 Night Vision
                    "color": True,
                    "temperature": True,
                    "infrared": True,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                46: {                    # LIFX BR30 Night Vision
                    "color": True,
                    "temperature": True,
                    "infrared": True,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                49: {                    # LIFX Mini Color
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 1500,
                    "max_kelvin": 6500,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                50: {                    # LIFX Mini White To Warm
                    "color": False,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 1500,
                    "max_kelvin": 6500,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                51: {                    # LIFX Mini White
                    "color": False,
                    "temperature": False,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2700,
                    "max_kelvin": 2700,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                52: {                    # LIFX GU10
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                53: {                    # LIFX GU10
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                55: {                    # LIFX Tile
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": True,
                    "matrix": True,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                57: {                    # LIFX Candle
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": True,
                    "min_kelvin": 1500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                59: {                    # LIFX Mini Color
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                60: {                    # LIFX Mini White To Warm
                    "color": False,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 1500,
                    "max_kelvin": 4000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                61: {                    # LIFX Mini White
                    "color": False,
                    "temperature": False,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2700,
                    "max_kelvin": 2700,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                62: {                    # LIFX A19
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                63: {                    # LIFX BR30
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                64: {                    # LIFX A19 Night Vision
                    "color": True,
                    "temperature": True,
                    "infrared": True,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                65: {                    # LIFX BR30 Night Vision
                    "color": True,
                    "temperature": True,
                    "infrared": True,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                66: {                    # LIFX Mini White
                    "color": False,
                    "temperature": False,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2700,
                    "max_kelvin": 2700,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                68: {                    # LIFX Candle
                    "color": False,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": True,
                    "min_kelvin": 1500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                70: {                    # LIFX Switch
                    "color": False,
                    "temperature": False,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": None,
                    "max_kelvin": None,
                    "hev": False,
                    "relays": True,
                    "buttons": True},
                81: {                    # LIFX Candle White To Warm
                    "color": False,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2200,
                    "max_kelvin": 6500,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                82: {                    # LIFX Filament Clear
                    "color": False,
                    "temperature": False,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2100,
                    "max_kelvin": 2100,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                85: {                    # LIFX Filament Amber
                    "color": False,
                    "temperature": False,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2000,
                    "max_kelvin": 2000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                87: {                    # LIFX Mini White
                    "color": False,
                    "temperature": False,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2700,
                    "max_kelvin": 2700,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                88: {                    # LIFX Mini White
                    "color": False,
                    "temperature": False,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2700,
                    "max_kelvin": 2700,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                89: {                    # LIFX Switch
                    "color": False,
                    "temperature": False,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": None,
                    "max_kelvin": None,
                    "hev": False,
                    "relays": True,
                    "buttons": True},
                90: {                    # LIFX Clean
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": True,
                    "relays": False,
                    "buttons": False},
                91: {                    # LIFX Color
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                92: {                    # LIFX Color
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                93: {                    # LIFX Color A19 1100lm (UNDOCUMENTED)
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 1500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                94: {                    # LIFX BR30
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                96: {                    # LIFX Candle White To Warm
                    "color": False,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2200,
                    "max_kelvin": 6500,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                97: {                    # LIFX A19
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                98: {                    # LIFX BR30
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                99: {                    # LIFX Clean
                    "color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": True,
                    "relays": False,
                    "buttons": False},
                100: {                    # LIFX Filament Clear
                    "color": False,
                    "temperature": False,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2100,
                    "max_kelvin": 2100,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                101: {                    # LIFX Filament Amber
                    "color": False,
                    "temperature": False,
                    "infrared": False,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2000,
                    "max_kelvin": 2000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                109: {                    # LIFX A19 Night Vision
                    "color": True,
                    "temperature": True,
                    "infrared": True,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                110: {                    # LIFX BR30 Night Vision
                    "color": True,
                    "temperature": True,
                    "infrared": True,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False},
                111: {                    # LIFX A19 Night Vision
                    "color": True,
                    "temperature": True,
                    "infrared": True,
                    "multizone": False,
                    "chain": False,
                    "matrix": False,
                    "min_kelvin": 2500,
                    "max_kelvin": 9000,
                    "hev": False,
                    "relays": False,
                    "buttons": False}
                }
