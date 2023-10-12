land_cover_dict_2021 = {
    "Tree cover": {
        "color": "#006400",
        "value": 10,
    },
    "Shrubland": {
        "color": "#ffbb22",
        "value": 20,
    },
    "Grassland": {
        "color": "#ffff4c",
        "value": 30,
    },
    "Cropland": {
        "color": "#f096ff",
        "value": 40,
    },
    "Built-up": {
        "color": "#fa0000",
        "value": 50,
    },
    "Bare / sparse vegetation": {
        "color": "#b4b4b4",
        "value": 60,
    },
    "Snow and ice": {
        "color": "#f0f0f0",
        "value": 70,
    },
    "Permanent water bodies": {
        "color": "#0064c8",
        "value": 80,
    },
    "Herbaceous wetland": {
        "color": "#0096a0",
        "value": 90,
    },
    "Mangroves": {
        "color": "#00cf75",
        "value": 95,
    },
    "Moss and lichen": {
        "color": "#fae6a0",
        "value": 100,
    },
}



globcover_2009_dict = {
    "11":	"Post-flooding or irrigated croplands",
    "14":	"Rainfed croplands",
    "20":	"Mosaic cropland (50-70%) / vegetation (grassland, shrubland, forest) (20-50%)",
    "30":	"Mosaic vegetation (grassland, shrubland, forest) (50-70%) / cropland (20-50%)",
    "40":	"Closed to open (>15%) broadleaved evergreen and/or semi-deciduous forest (>5m)",
    "50":	"Closed (>40%) broadleaved deciduous forest (>5m)",
    "60":	"Open (15-40%) broadleaved deciduous forest (>5m)",
    "70":	"Closed (>40%) needleleaved evergreen forest (>5m)",
    "90":	"Open (15-40%) needleleaved deciduous or evergreen forest (>5m)",
    "100":	"Closed to open (>15%) mixed broadleaved and needleleaved forest (>5m)",
    "110":	"Mosaic forest-shrubland (50-70%) / grassland (20-50%)",
    "120":	"Mosaic grassland (50-70%) / forest-shrubland (20-50%)",
    "130":	"Closed to open (>15%) shrubland (<5m)",
    "140":	"Closed to open (>15%) grassland",
    "150":	"Sparse (>15%) vegetation (woody vegetation, shrubs, grassland)",
    "160":	"Closed (>40%) broadleaved forest regularly flooded - Fresh water",
    "170":	"Closed (>40%) broadleaved semi-deciduous and/or evergreen forest regularly flooded - saline water",
    "180":	"Closed to open (>15%) vegetation (grassland, shrubland, woody vegetation) on regularly flooded or waterlogged soil - fresh, brackish or saline water",
    "190":	"Artificial surfaces and associated areas (urban areas >50%) GLOBCOVER 2009",
    "200":	"Bare areas",
    "210":	"Water bodies",
    "220":	"Permanent snow and ice",
    "230":	"Unclassified",
}

forrest_2009 = [
    # "Post-flooding or irrigated croplands",
    # "Rainfed croplands",
    "Mosaic cropland (50-70%) / vegetation (grassland, shrubland, forest) (20-50%)",
    "Mosaic vegetation (grassland, shrubland, forest) (50-70%) / cropland (20-50%)",
    "Closed to open (>15%) broadleaved evergreen and/or semi-deciduous forest (>5m)",
    "Closed (>40%) broadleaved deciduous forest (>5m)",
    "Open (15-40%) broadleaved deciduous forest (>5m)",
    "Closed (>40%) needleleaved evergreen forest (>5m)",
    "Open (15-40%) needleleaved deciduous or evergreen forest (>5m)",
    "Closed to open (>15%) mixed broadleaved and needleleaved forest (>5m)",
    "Mosaic forest-shrubland (50-70%) / grassland (20-50%)",
    "Mosaic grassland (50-70%) / forest-shrubland (20-50%)",
    "Closed to open (>15%) shrubland (<5m)",
    "Closed to open (>15%) grassland",
    "Sparse (>15%) vegetation (woody vegetation, shrubs, grassland)",
    "Closed (>40%) broadleaved forest regularly flooded - Fresh water",
    "Closed (>40%) broadleaved semi-deciduous and/or evergreen forest regularly flooded - saline water",
    "Closed to open (>15%) vegetation (grassland, shrubland, woody vegetation) on regularly flooded or waterlogged soil - fresh, brackish or saline water",
    # "Artificial surfaces and associated areas (urban areas >50%) GLOBCOVER 2009",
    # "Bare areas",
    # "Water bodies",
    # "Permanent snow and ice",
    # "Unclassified",
]

forrest_2015 = [
    # 'Unknown. No or not enough satellite data available.',
    # 'Shrubs. Woody perennial plants with persistent and woody stems\nand without any defined main stem being less than 5 m tall. The\nshrub foliage can be either evergreen or deciduous.\n',
    # 'Herbaceous vegetation. Plants without persistent stem or shoots above ground\nand lacking definite firm structure. Tree and shrub cover is less\nthan 10 %.\n',
    # 'Cultivated and managed vegetation / agriculture. Lands covered with temporary crops followed by harvest\nand a bare soil period (e.g., single and multiple cropping systems).\nNote that perennial woody crops will be classified as the appropriate\nforest or shrub land cover type.\n',
    # 'Urban / built up. Land covered by buildings and other man-made structures.',
    # 'Bare / sparse vegetation. Lands with exposed soil, sand, or rocks and never has\nmore than 10 % vegetated cover during any time of the year.\n',
    # 'Snow and ice. Lands under snow or ice cover throughout the year.',
    # 'Permanent water bodies. Lakes, reservoirs, and rivers. Can be either fresh or salt-water bodies.',
    'Herbaceous wetland. Lands with a permanent mixture of water and herbaceous\nor woody vegetation. The vegetation can be present in either salt,\nbrackish, or fresh water.\n',
    'Moss and lichen.',
    'Closed forest, evergreen needle leaf. Tree canopy >70 %, almost all needle leaf trees remain\ngreen all year. Canopy is never without green foliage.\n',
    'Closed forest, evergreen broad leaf. Tree canopy >70 %, almost all broadleaf trees remain\ngreen year round. Canopy is never without green foliage.\n',
    'Closed forest, deciduous needle leaf. Tree canopy >70 %, consists of seasonal needle leaf\ntree communities with an annual cycle of leaf-on and leaf-off\nperiods.\n',
    'Closed forest, deciduous broad leaf. Tree canopy >70 %, consists of seasonal broadleaf\ntree communities with an annual cycle of leaf-on and leaf-off periods.\n',
    'Closed forest, mixed.',
    'Closed forest, not matching any of the other definitions.',
    'Open forest, evergreen needle leaf. Top layer- trees 15-70 % and second layer- mixed of shrubs\nand grassland, almost all needle leaf trees remain green all year.\nCanopy is never without green foliage.\n',
    'Open forest, evergreen broad leaf. Top layer- trees 15-70 % and second layer- mixed of shrubs\nand grassland, almost all broadleaf trees remain green year round.\nCanopy is never without green foliage.\n',
    'Open forest, deciduous needle leaf. Top layer- trees 15-70 % and second layer- mixed of shrubs\nand grassland, consists of seasonal needle leaf tree communities with\nan annual cycle of leaf-on and leaf-off periods.\n',
    'Open forest, deciduous broad leaf. Top layer- trees 15-70 % and second layer- mixed of shrubs\nand grassland, consists of seasonal broadleaf tree communities with\nan annual cycle of leaf-on and leaf-off periods.\n',
    'Open forest, mixed.',
    'Open forest, not matching any of the other definitions.',
    # 'Oceans, seas. Can be either fresh or salt-water bodies.'
]

forrest_2019 = [
    # 'Unknown. No or not enough satellite data available.',
    # 'Shrubs. Woody perennial plants with persistent and woody stems\nand without any defined main stem being less than 5 m tall. The\nshrub foliage can be either evergreen or deciduous.\n',
    # 'Herbaceous vegetation. Plants without persistent stem or shoots above ground\nand lacking definite firm structure. Tree and shrub cover is less\nthan 10 %.\n',
    # 'Cultivated and managed vegetation / agriculture. Lands covered with temporary crops followed by harvest\nand a bare soil period (e.g., single and multiple cropping systems).\nNote that perennial woody crops will be classified as the appropriate\nforest or shrub land cover type.\n',
    # 'Urban / built up. Land covered by buildings and other man-made structures.',
    # 'Bare / sparse vegetation. Lands with exposed soil, sand, or rocks and never has\nmore than 10 % vegetated cover during any time of the year.\n',
    # 'Snow and ice. Lands under snow or ice cover throughout the year.',
    # 'Permanent water bodies. Lakes, reservoirs, and rivers. Can be either fresh or salt-water bodies.',
    'Herbaceous wetland. Lands with a permanent mixture of water and herbaceous\nor woody vegetation. The vegetation can be present in either salt,\nbrackish, or fresh water.\n',
    'Moss and lichen.',
    'Closed forest, evergreen needle leaf. Tree canopy >70 %, almost all needle leaf trees remain\ngreen all year. Canopy is never without green foliage.\n',
    'Closed forest, evergreen broad leaf. Tree canopy >70 %, almost all broadleaf trees remain\ngreen year round. Canopy is never without green foliage.\n',
    'Closed forest, deciduous needle leaf. Tree canopy >70 %, consists of seasonal needle leaf\ntree communities with an annual cycle of leaf-on and leaf-off\nperiods.\n',
    'Closed forest, deciduous broad leaf. Tree canopy >70 %, consists of seasonal broadleaf\ntree communities with an annual cycle of leaf-on and leaf-off periods.\n',
    'Closed forest, mixed.',
    'Closed forest, not matching any of the other definitions.',
    'Open forest, evergreen needle leaf. Top layer- trees 15-70 % and second layer- mixed of shrubs\nand grassland, almost all needle leaf trees remain green all year.\nCanopy is never without green foliage.\n',
    'Open forest, evergreen broad leaf. Top layer- trees 15-70 % and second layer- mixed of shrubs\nand grassland, almost all broadleaf trees remain green year round.\nCanopy is never without green foliage.\n',
    'Open forest, deciduous needle leaf. Top layer- trees 15-70 % and second layer- mixed of shrubs\nand grassland, consists of seasonal needle leaf tree communities with\nan annual cycle of leaf-on and leaf-off periods.\n',
    'Open forest, deciduous broad leaf. Top layer- trees 15-70 % and second layer- mixed of shrubs\nand grassland, consists of seasonal broadleaf tree communities with\nan annual cycle of leaf-on and leaf-off periods.\n',
    'Open forest, mixed.',
    'Open forest, not matching any of the other definitions.',
    # 'Oceans, seas. Can be either fresh or salt-water bodies.'
]

forrest_2021 = [
    'Tree cover',
    'Shrubland',
    'Grassland',
    # 'Cropland',
    # 'Built-up',
    # 'Bare / sparse vegetation',
    # 'Snow and ice',
    # 'Permanent water bodies',
    'Herbaceous wetland',
    'Mangroves',
    'Moss and lichen'
]


globcover_2009_dict = {
    '11': {
        "name": 'Post-flooding or irrigated croplands',
        "forrest_flag": 0},
    '14': {"name": 'Rainfed croplands',
           "forrest_flag": 0},
    '20': {"name": 'Mosaic cropland (50-70%) / vegetation (grassland, shrubland, forest) (20-50%)',
           "forrest_flag": 1},
    '30': {"name": 'Mosaic vegetation (grassland, shrubland, forest) (50-70%) / cropland (20-50%)',
           "forrest_flag": 1},
    '40': {"name": 'Closed to open (>15%) broadleaved evergreen and/or semi-deciduous forest (>5m)',
           "forrest_flag": 1},
    '50': {"name": 'Closed (>40%) broadleaved deciduous forest (>5m)',
           "forrest_flag": 1},
    '60': {"name": 'Open (15-40%) broadleaved deciduous forest (>5m)',
           "forrest_flag": 1},
    '70': {"name": 'Closed (>40%) needleleaved evergreen forest (>5m)',
           "forrest_flag": 1},
    '90': {"name": 'Open (15-40%) needleleaved deciduous or evergreen forest (>5m)',
           "forrest_flag": 1},
    '100': {"name": 'Closed to open (>15%) mixed broadleaved and needleleaved forest (>5m)',
            "forrest_flag": 0},
    '110': {"name": 'Mosaic forest-shrubland (50-70%) / grassland (20-50%)',
            "forrest_flag": 0},
    '120': {"name": 'Mosaic grassland (50-70%) / forest-shrubland (20-50%)',
            "forrest_flag": 0},
    '130': {"name": 'Closed to open (>15%) shrubland (<5m)',
            "forrest_flag": 0},
    '140': {"name": 'Closed to open (>15%) grassland',
            "forrest_flag": 0},
    '150': {"name": 'Sparse (>15%) vegetation (woody vegetation, shrubs, grassland)',
            "forrest_flag": 0},
    '160': {"name": 'Closed (>40%) broadleaved forest regularly flooded - Fresh water',
            "forrest_flag": 0},
    '170': {"name": 'Closed (>40%) broadleaved semi-deciduous and/or evergreen forest regularly flooded - saline water',
            "forrest_flag": 0},
    '180': {"name": 'Closed to open (>15%) vegetation (grassland, shrubland, woody vegetation) on regularly flooded or waterlogged soil - fresh, brackish or saline water',
            "forrest_flag": 0},
    '190': {"name": 'Artificial surfaces and associated areas (urban areas >50%) GLOBCOVER 2009',
            "forrest_flag": 0},
    '200': {"name": 'Bare areas',
            "forrest_flag": 0},
    '210': {"name": 'Water bodies',
            "forrest_flag": 0},
    '220': {"name": 'Permanent snow and ice',
            "forrest_flag": 0},
    '230': {"name": 'Unclassified',
            "forrest_flag": 0}
}


copernicus_2015 = {
    '0': {"name": 'Unknown. No or not enough satellite data available.',
          "forrest_flag": 0},
    '20': {"name": 'Shrubs. Woody perennial plants with persistent and woody stems\nand without any defined main stem being less than 5 m tall. The\nshrub foliage can be either evergreen or deciduous.\n',
           "forrest_flag": 0},
    '30': {"name": 'Herbaceous vegetation. Plants without persistent stem or shoots above ground\nand lacking definite firm structure. Tree and shrub cover is less\nthan 10 %.\n',
           "forrest_flag": 0},
    '40': {"name": 'Cultivated and managed vegetation / agriculture. Lands covered with temporary crops followed by harvest\nand a bare soil period (e.g., single and multiple cropping systems).\nNote that perennial woody crops will be classified as the appropriate\nforest or shrub land cover type.\n',
           "forrest_flag": 0},
    '50': {"name": 'Urban / built up. Land covered by buildings and other man-made structures.',
           "forrest_flag": 0},
    '60': {"name": 'Bare / sparse vegetation. Lands with exposed soil, sand, or rocks and never has\nmore than 10 % vegetated cover during any time of the year.\n',
           "forrest_flag": 0},
    '70': {"name": 'Snow and ice. Lands under snow or ice cover throughout the year.',
           "forrest_flag": 0},
    '80': {"name": 'Permanent water bodies. Lakes, reservoirs, and rivers. Can be either fresh or salt-water bodies.',
           "forrest_flag": 0},
    '90': {"name": 'Herbaceous wetland. Lands with a permanent mixture of water and herbaceous\nor woody vegetation. The vegetation can be present in either salt,\nbrackish, or fresh water.\n',
           "forrest_flag": 1},
    '100': {"name": 'Moss and lichen.',
            "forrest_flag": 1},
    '111': {"name": 'Closed forest, evergreen needle leaf. Tree canopy >70 %, almost all needle leaf trees remain\ngreen all year. Canopy is never without green foliage.\n',
            "forrest_flag": 1},
    '112': {"name": 'Closed forest, evergreen broad leaf. Tree canopy >70 %, almost all broadleaf trees remain\ngreen year round. Canopy is never without green foliage.\n',
            "forrest_flag": 1},
    '113': {"name": 'Closed forest, deciduous needle leaf. Tree canopy >70 %, consists of seasonal needle leaf\ntree communities with an annual cycle of leaf-on and leaf-off\nperiods.\n',
            "forrest_flag": 1},
    '114': {"name": 'Closed forest, deciduous broad leaf. Tree canopy >70 %, consists of seasonal broadleaf\ntree communities with an annual cycle of leaf-on and leaf-off periods.\n',
            "forrest_flag": 1},
    '115': {"name": 'Closed forest, mixed.',
            "forrest_flag": 1},
    '116': {"name": 'Closed forest, not matching any of the other definitions.',
            "forrest_flag": 1},
    '121': {"name": 'Open forest, evergreen needle leaf. Top layer- trees 15-70 % and second layer- mixed of shrubs\nand grassland, almost all needle leaf trees remain green all year.\nCanopy is never without green foliage.\n',
            "forrest_flag": 1},
    '122': {"name": 'Open forest, evergreen broad leaf. Top layer- trees 15-70 % and second layer- mixed of shrubs\nand grassland, almost all broadleaf trees remain green year round.\nCanopy is never without green foliage.\n',
            "forrest_flag": 1},
    '123': {"name": 'Open forest, deciduous needle leaf. Top layer- trees 15-70 % and second layer- mixed of shrubs\nand grassland, consists of seasonal needle leaf tree communities with\nan annual cycle of leaf-on and leaf-off periods.\n',
            "forrest_flag": 1},
    '124': {"name": 'Open forest, deciduous broad leaf. Top layer- trees 15-70 % and second layer- mixed of shrubs\nand grassland, consists of seasonal broadleaf tree communities with\nan annual cycle of leaf-on and leaf-off periods.\n',
            "forrest_flag": 1},
    '125': {"name": 'Open forest, mixed.',
            "forrest_flag": 1},
    '126': {"name": 'Open forest, not matching any of the other definitions.',
            "forrest_flag": 1},
    '200': {"name": 'Oceans, seas. Can be either fresh or salt-water bodies.',
            "forrest_flag": 0},
}

copernicus_2019 = {
    '0': {
        "name": 'Unknown. No or not enough satellite data available.',
        "forrest_flag": 0},
    '20': {
        "name": 'Shrubs. Woody perennial plants with persistent and woody stems\nand without any defined main stem being less than 5 m tall. The\nshrub foliage can be either evergreen or deciduous.\n',
        "forrest_flag": 0},
    '30': {
        "name": 'Herbaceous vegetation. Plants without persistent stem or shoots above ground\nand lacking definite firm structure. Tree and shrub cover is less\nthan 10 %.\n',
        "forrest_flag": 0},
    '40': {
        "name": 'Cultivated and managed vegetation / agriculture. Lands covered with temporary crops followed by harvest\nand a bare soil period (e.g., single and multiple cropping systems).\nNote that perennial woody crops will be classified as the appropriate\nforest or shrub land cover type.\n',
        "forrest_flag": 0},
    '50': {
        "name": 'Urban / built up. Land covered by buildings and other man-made structures.',
        "forrest_flag": 0},
    '60': {
        "name": 'Bare / sparse vegetation. Lands with exposed soil, sand, or rocks and never has\nmore than 10 % vegetated cover during any time of the year.\n',
        "forrest_flag": 0},
    '70': {
        "name": 'Snow and ice. Lands under snow or ice cover throughout the year.',
        "forrest_flag": 0},
    '80': {
        "name": 'Permanent water bodies. Lakes, reservoirs, and rivers. Can be either fresh or salt-water bodies.',
        "forrest_flag": 0},
    '90': {
        "name": 'Herbaceous wetland. Lands with a permanent mixture of water and herbaceous\nor woody vegetation. The vegetation can be present in either salt,\nbrackish, or fresh water.\n',
        "forrest_flag": 1},
    '100': {
        "name": 'Moss and lichen.',
        "forrest_flag": 1},
    '111': {
        "name": 'Closed forest, evergreen needle leaf. Tree canopy >70 %, almost all needle leaf trees remain\ngreen all year. Canopy is never without green foliage.\n',
        "forrest_flag": 1},
    '112': {
        "name": 'Closed forest, evergreen broad leaf. Tree canopy >70 %, almost all broadleaf trees remain\ngreen year round. Canopy is never without green foliage.\n',
        "forrest_flag": 1},
    '113': {
        "name": 'Closed forest, deciduous needle leaf. Tree canopy >70 %, consists of seasonal needle leaf\ntree communities with an annual cycle of leaf-on and leaf-off\nperiods.\n',
        "forrest_flag": 1},
    '114': {
        "name": 'Closed forest, deciduous broad leaf. Tree canopy >70 %, consists of seasonal broadleaf\ntree communities with an annual cycle of leaf-on and leaf-off periods.\n',
        "forrest_flag": 1},
    '115': {
        "name": 'Closed forest, mixed.',
        "forrest_flag": 1},
    '116': {
        "name": 'Closed forest, not matching any of the other definitions.',
        "forrest_flag": 1},
    '121': {
        "name": 'Open forest, evergreen needle leaf. Top layer- trees 15-70 % and second layer- mixed of shrubs\nand grassland, almost all needle leaf trees remain green all year.\nCanopy is never without green foliage.\n',
        "forrest_flag": 1},
    '122': {
        "name": 'Open forest, evergreen broad leaf. Top layer- trees 15-70 % and second layer- mixed of shrubs\nand grassland, almost all broadleaf trees remain green year round.\nCanopy is never without green foliage.\n',
        "forrest_flag": 1},
    '123': {
        "name": 'Open forest, deciduous needle leaf. Top layer- trees 15-70 % and second layer- mixed of shrubs\nand grassland, consists of seasonal needle leaf tree communities with\nan annual cycle of leaf-on and leaf-off periods.\n',
        "forrest_flag": 1},
    '124': {
        "name": 'Open forest, deciduous broad leaf. Top layer- trees 15-70 % and second layer- mixed of shrubs\nand grassland, consists of seasonal broadleaf tree communities with\nan annual cycle of leaf-on and leaf-off periods.\n',
        "forrest_flag": 1},
    '125': {
        "name": 'Open forest, mixed.',
        "forrest_flag": 1},
    '126': {
        "name": 'Open forest, not matching any of the other definitions.',
        "forrest_flag": 1},
    '200': {
        "name": 'Oceans, seas. Can be either fresh or salt-water bodies.',
        "forrest_flag": 0},
}


esaworldcover_2021 = {
    '10': {"name": 'Tree cover', "forrest_flag": 1},
    '20': {"name": 'Shrubland', "forrest_flag": 0},
    '30': {"name": 'Grassland', "forrest_flag": 0},
    '40': {"name": 'Cropland', "forrest_flag": 0},
    '50': {"name": 'Built-up', "forrest_flag": 0},
    '60': {"name": 'Bare / sparse vegetation', "forrest_flag": 0},
    '70': {"name": 'Snow and ice', "forrest_flag": 0},
    '80': {"name": 'Permanent water bodies', "forrest_flag": 0},
    '90': {"name": 'Herbaceous wetland', "forrest_flag": 1},
    '95': {"name": 'Mangroves', "forrest_flag": 1},
    '100': {"name": 'Moss and lichen', "forrest_flag": 1},
}