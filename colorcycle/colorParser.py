from colorcycle.color_convert import hex_to_rgb, hex_to_hsl

color_names = {
    'red': '#FF0000',
    'green': '#00FF00',
    'blue': '#0000FF',
    'light blue': '#add8e6',
    'dark blue': '#00008B',
    'yellow': '#FFFF00',
    'purple': '#800080',
    'orange': '#FFA500',
    'white': '#FFFFFF',
    'black': '#000000',
    'pink': '#FFB6C1',
    'brown': '#A52A2A',
    'grey': '#A9A9A9',
    'violet': '#EE82EE',
    'indigo': '#4B0082',
    'teal': '#008080',
    'turquoise': '#40E0D0',
    'magenta': '#FF00FF',
    'lime': '#00FF00',
    'cyan': '#00FFFF',
    'gold': '#FFD700',
    'silver': '#C0C0C0',
    'maroon': '#800000',
    'olive': '#808000',
    'navy': '#000080',
    'beige': '#F5F5DC',
    'coral': '#FF7F50',
    'aqua': '#00FFFF',
    'lavender': '#E6E6FA',
    'salmon': '#FA8072',
    'chocolate': '#D2691E',
    'tomato': '#FF6347',
    'orchid': '#DA70D6',
    'khaki': '#F0E68C',
    'plum': '#DDA0DD',
    'crimson': '#DC143C',
    'tan': '#D2B48C',
    'thistle': '#D8BFD8',
    'wheat': '#F5DEB3',
    'seaGreen': '#2E8B57',
    'forestGreen': '#228B22',
    'darkOliveGreen': '#556B2F',
    'midnightBlue': '#191970',
    'royalBlue': '#4169E1',
    'skyBlue': '#87CEEB',
    'deepPink': '#FF1493',
    'hotPink': '#FF69B4',
    'rosyBrown': '#BC8F8F',
    'sienna': '#A0522D',
    'slateGray': '#708090',
    'lightSlateGray': '#778899',
    'steelBlue': '#4682B4',
    'mediumPurple': '#9370DB',
    'mediumOrchid': '#BA55D3',
    'darkGoldenRod': '#B8860B',
    'lightCoral': '#F08080',
    'darkSlateBlue': '#483D8B',
    'dimGray': '#696969',
    'dodgerBlue': '#1E90FF',
    'mediumSeaGreen': '#3CB371',
    'paleVioletRed': '#DB7093',
    'papayaWhip': '#FFEFD5',
    'peachPuff': '#FFDAB9',
    'powderBlue': '#B0E0E6',
    'rosyBrown': '#BC8F8F',
    'sandyBrown': '#F4A460',
    'slateBlue': '#6A5ACD',
    'springGreen': '#00FF7F',
    'yellowGreen': '#9ACD32',
    'lightGreen': '#90EE90',
    'lightPink': '#FFB6C1',
    'mediumVioletRed': '#C71585',
    'paleGoldenRod': '#EEE8AA',
    'chartreuse': '#7FFF00',
    'cadetBlue': '#5F9EA0',
    'oldLace': '#FDF5E6',
    'darkOrange': '#FF8C00',
    'mediumSlateBlue': '#7B68EE',
    'darkTurquoise': '#00CED1',
    'lightSeaGreen': '#20B2AA',
    'darkSeaGreen': '#8FBC8F',
    'darkOrchid': '#9932CC',
    'darkSalmon': '#E9967A',
    'mediumAquamarine': '#66CDAA',
    'mistyRose': '#FFE4E1',
    'honeyDew': '#F0FFF0',
    'azure': '#F0FFFF',
    'mintCream': '#F5FFFA',
    'aliceBlue': '#F0F8FF',
    'floralWhite': '#FFFAF0',
    'ghostWhite': '#F8F8FF',
    'lightYellow': '#FFFFE0',
    'ivory': '#FFFFF0',
    'lemonChiffon': '#FFFACD',
    'lightCyan': '#E0FFFF',
    'lavenderBlush': '#FFF0F5',
    'linen': '#FAF0E6',
    'moccasin': '#FFE4B5',
    'antiqueWhite': '#FAEBD7',
    'bisque': '#FFE4C4',
    'blanchedAlmond': '#FFEBCD',
    'cornsilk': '#FFF8DC',
    'darkKhaki': '#BDB76B',
    'darkRed': '#8B0000',
    'darkMagenta': '#8B008B',
    'darkBlue': '#00008B',
    'lightSkyBlue': '#87CEFA',
    'cornflowerBlue': '#6495ED',
    'darkSlateGray': '#2F4F4F',
    'mediumTurquoise': '#48D1CC',
    'saddleBrown': '#8B4513',
    'paleTurquoise': '#AFEEEE',
    'burlyWood': '#DEB887',
    'navajoWhite': '#FFDEAD',
    'lightSteelBlue': '#B0C4DE',
    'mediumSpringGreen': '#00FA9A',
    'gainsboro': '#DCDCDC',
    'lightGrey': '#D3D3D3',
    'fuchsia': '#FF00FF',
    'slateGray': '#708090',
    'seashell': '#FFF5EE',
    'snow': '#FFFAFA',
    'seagreen': '#2E8B57',
    'goldenrod': '#DAA520',
    'rebeccapurple': '#663399',
    'blueviolet': '#8A2BE2',
    'mediumorchid': '#BA55D3',
    'mediumpurple': '#9370DB',
    'cornsilk': '#FFF8DC',
    'aquamarine': '#7FFFD4',
    'oliveDrab': '#6B8E23',
    'mediumSpringGreen': '#00FA9A',
    'darkViolet': '#9400D3',
    'peru': '#CD853F',
    'peachPuff': '#FFDAB9',
    'paleGreen': '#98FB98',
    'paleTurquoise': '#AFEEEE',
    'tan': '#D2B48C',
    'paleGoldenRod': '#EEE8AA',
    'darkSlateGrey': '#2F4F4F',
    'lightYellow': '#FFFFE0',
    'gainsboro': '#DCDCDC',
    'lightBlue': '#ADD8E6',
    'darkOliveGreen': '#556B2F',
    'rosyBrown': '#BC8F8F',
    'mistyRose': '#FFE4E1',
    'lightSlateGrey': '#778899',
    'burlyWood': '#DEB887',
    'darkSeaGreen': '#8FBC8F',
    'amethyst': '#9966CC',
    'apricot': '#FBCEB1',
    'aquaMarine': '#7FFFD4',
    'asparagus': '#87A96B',
    'atomicTangerine': '#FF9966',
    'babyBlue': '#89CFF0',
    'bananaMania': '#FAE7B5',
    'bittersweet': '#FE6F5E',
    'blizzardBlue': '#ACE5EE',
    'blueBell': '#A2A2D0',
    'brinkPink': '#FB607F',
    'caribbeanGreen': '#00CC99',
    'celeste': '#B2FFFF',
    'cerise': '#DE3163',
    'cerulean': '#007BA7',
    'champagne': '#F7E7CE',
    'cherryBlossomPink': '#FFB7C5',
    'cinnamon': '#D2691E',
    'cobaltBlue': '#0047AB',
    'copper': '#B87333',
    'coralPink': '#F88379',
    'cornflower': '#93CCEA',
    'cosmicLatte': '#FFF8E7',
    'cream': '#FFFDD0',
    'cyanBlueAzure': '#4682BF',
    'darkBrown': '#654321',
    'darkChestnut': '#986960',
    'darkPastelGreen': '#03C03C',
    'deepMossGreen': '#355E3B',
    'desertSand': '#EDC9AF',
    'dodgerBlue': '#1E90FF',
    'electricBlue': '#7DF9FF',
    'electricLime': '#CCFF00',
    'englishLavender': '#B48395',
    'fernGreen': '#4F7942',
    'fuzzyWuzzy': '#CC6666',
    'ghostWhite': '#F8F8FF',
    'gamboge': '#E49B0F',
    'grannySmithApple': '#A8E4A0',
    'heatWave': '#FF7A00',
    'heliotrope': '#DF73FF',
    'honeydew': '#F0FFF0',
    'jungleGreen': '#29AB87',
    'lemonGlacier': '#FDFF00',
    'lilac': '#C8A2C8',
    'limerick': '#9DC209',
    'maize': '#FBEC5D',
    'magicMint': '#AAF0D1',
    'midnight': '#702670',
    'mountbattenPink': '#997A8D',
    'nadeshikoPink': '#F6ADC6',
    'napierGreen': '#2A8000',
    'neonCarrot': '#FFA343',
    'nonPhotoBlue': '#A4DDED',
    'oldGold': '#CFB53B',
    'paleAqua': '#BCD4E6',
    'paleCarmine': '#AF4035',
    'paleCornflowerBlue': '#ABCDEF',
    'palePink': '#FADADD',
    'pastelYellow': '#FDFD96',
    'persianPink': '#F77FBE',
    'persianRose': '#FE28A2',
    'pineGreen': '#01796F',
    'pixiePowder': '#391285',
    'platinum': '#E5E4E2',
    'portlandOrange': '#FF5A36',
    'prussianBlue': '#003153',
    'pueblo': '#7D2C14',
    'radicalRed': '#FF355E',
    'razzmatazz': '#E3256B',
    'roseTaupe': '#905D5D',
    'royalPurple': '#7851A9',
    'saffron': '#F4C430',
    'sapphire': '#0F52BA',
    'scarlet': '#FF2400',
    'seashell': '#FFF5EE',
    'sepia': '#704214',
    'shockingPink': '#FC0FC0',
    'skyMagenta': '#CF71AF',
    'spiroDiscoBall': '#0FC0FC',
    'sunray': '#E3AB57',
    'tangerineYellow': '#FFCC00',
    'teaGreen': '#D0F0C0',
    'thulianPink': '#DE6FA1',
    'ultramarine': '#120A8F',
    'vanilla': '#F3E5AB',
    'viridian': '#40826D',
    'vividViolet': '#9F00FF',
    'wildBlueYonder': '#A2ADD0',
    'wine': '#722F37',
    'yellowOrange': '#FFAE42',
    'zomp': '#39A78E',
    'artichoke': '#8F9779',
    'brickRed': '#CB4154',
    'canary': '#FFFF99',
    'celadon': '#ACE1AF',
    'coralRed': '#FF4040',
    'electricPurple': '#BF00FF',
    'feldgrau': '#4D5D53',
    'fuchsiaPurple': '#CC397B',
    'jazzberryJam': '#A50B5E',
    'moonstoneBlue': '#73A9C2',
    'neonFuchsia': '#FE4164',
    'onyx': '#353839',
    'paleGold': '#E6BE8A',
    'periwinkle': '#CCCCFF',
    'persimmon': '#EC5800',
    'richLavender': '#A76BCF',
    'seaFoamGreen': '#9FE2BF',
    'shinyShamrock': '#5FA778',
    'vermilion': '#E34234',
    'violetRed': '#F75394',
    'wisteria': '#C9A0DC',
    'sandyTan': '#F4A460',
    'flax': '#EEDC82',
    'blueGreen': '#0D98BA',
    'blueViolet': '#8A2BE2',
    'cambridgeBlue': '#A3C1AD',
    'carnationPink': '#FFA6C9',
    'desire': '#EA3C53',
    'fuzzyWuzzyBrown': '#C45655',
    'lemonYellow': '#FFF44F',
    'malachite': '#0BDA51',
    'outerSpace': '#414A4C',
    'paynesGrey': '#536878',
    'prune': '#701C1C',
    'redViolet': '#C71585',
    'rufous': '#A81C07',
    'straw': '#E4D96F',
    'stratos': '#000741',
    'tangoPink': '#E4717A',
    'ultraPink': '#FF6FFF',
    'verdigris': '#43B3AE',
    'zaffre': '#0014A8',
    'zeus': '#292319',
    'midnightBlue': '#191970',
    'mintCream': '#F5FFFA',
    'royalBlue': '#4169E1',
    'rust': '#B7410E',
    'schoolBusYellow': '#FFD800',
    'sunglow': '#FFCC33',
    'tuscan': '#FAD6A5',
    'wasabi': '#78866B',
    'xanadu': '#738678',
    'airForceBlue': '#5D8AA8',
    'aliceBlue': '#F0F8FF',
    'alizarinCrimson': '#E32636',
    'almond': '#EFDECD',
    'antiqueBronze': '#665D1E',
    'antiqueRuby': '#841B2D',
    'antiqueWhite': '#FAEBD7',
    'aqua': '#00FFFF',
    'armyGreen': '#4B5320',
    'arylideYellow': '#E9D66B',
    'ashGray': '#B2BEB5',
    'aztecGold': '#C39953',
    'azure': '#007FFF',
    'babyPink': '#F4C2C2',
    'ballBlue': '#21ABCD',
    'barnRed': '#7C0A02',
    'battleshipGrey': '#848482',
    'beige': '#F5F5DC',
    'bitterLemon': '#CAE00D',
    'blueSapphire': '#126180',
    'bole': '#79443B',
    'brick': '#B22222',
    'brilliantRose': '#FF55A3',
    'burntOrange': '#CC5500',
    'camouflageGreen': '#78866B',
    'celadonGreen': '#2F847C',
    'cherryRed': '#D2042D',
    'chinaPink': '#DE6FA1',
    'chocolate': '#D2691E',
    'classicRose': '#FBCCE7',
    'cocoaBrown': '#D2691E',
    'copperRed': '#CB6D51',
    'cordovan': '#893F45',
    'cornsilk': '#FFF8DC',
    'cottonCandy': '#FFBCD9',
    'darkByzantium': '#5D3954',
    'darkCandyAppleRed': '#A40000',
    'darkChampagne': '#C2B280',
    'darkElectricBlue': '#536878',
    'darkJungleGreen': '#1A2421',
    'darkKhaki': '#BDB76B',
    'darkLavender': '#734F96',
    'darkOliveGreen': '#556B2F',
    'darkPastelBlue': '#779ECB',
    'darkScarlet': '#560319',
    'deepPeach': '#FFCBA4',
    'denimBlue': '#2243B6',
    'dutchWhite': '#EFDFBB',
    'ebony': '#555D50',
    'emeraldGreen': '#50C878',
    'fern': '#71BC78',
    'fieldDrab': '#6C541E',
    'frenchRose': '#F64A8A',
    'fulvous': '#E48400',
    'ginger': '#B06500',
    'glaucous': '#6082B6',
    'greenSheen': '#6EAEA1',
    'harlequin': '#3FFF00',
    'harvestGold': '#DA9100',
    'hollywoodCerise': '#F400A1',
    'hunterGreen': '#355E3B',
    'indiaGreen': '#138808',
    'iris': '#5A4FCF',
    'jasmine': '#F8DE7E',
    'jet': '#343434',
    'laurelGreen': '#A9BA9D',
    'lava': '#CF1020',
    'lemonLime': '#E3FF00',
    'lemonYellowCrayola': '#FFFF9F',
    'licorice': '#1A1110',
    'lightGreen': '#90EE90',
    'lightSlateGray': '#778899',
    'lightTaupe': '#B38B6D',
    'liver': '#534B4F',
    'madderLake': '#CC3336',
    'mangoTango': '#FF8243',
    'mauvelous': '#EF98AA',
    'mediumChampagne': '#F3E5AB',
    'mediumSpringBud': '#C9DC87',
    'mediumTuscanRed': '#79443B',
    'melon': '#FDBCB4',
    'midnightGreen': '#004953',
    'mimiPink': '#FFDAE9',
    'mistyRose': '#FFE4E1',
    'morningBlue': '#8DA399',
    'mossGreen': '#8A9A5B',
    'mossGreenCrayola': '#B9AD61',
    'mughalGreen': '#306030',
    'mustard': '#FFDB58',
    'navajoWhite': '#FFDEAD',
    'neonGreen': '#39FF14',
    'ochre': '#CC7722',
    'oldLavender': '#796878',
    'olivine': '#9AB973',
    'ouCrimsonRed': '#990000',
    'outrageousOrange': '#FF6E4A',
    'parisGreen': '#50C878',
    'pastelGreen': '#77DD77',
    'paynesGrey': '#536878',
    'pearlAqua': '#88D8C0',
    'peridot': '#E6E200',
    'persianBlue': '#1C39BB',
    'persianGreen': '#00A693',
    'pistachio': '#93C572',
    'platinum': '#E5E4E2',
    'plum': '#DDA0DD',
    'polishedPine': '#5DA493',
    'pompAndPower': '#86608E',
    'portlandOrange': '#FF5A36',
    'prussianBlue': '#003153',
    'puce': '#CC8899',
    'quartz': '#51484F',
    'racingGreen': '#0C1910',
    'rajah': '#FBAB60',
    'raspberryGlace': '#915F6D',
    'rawSienna': '#D68A59',
    'redwood': '#A45A52',
    'richBlack': '#004040',
    'romanSilver': '#838996',
    'roseMadder': '#E32636',
    'rosewood': '#65000B',
    'rossoCorsa': '#D40000',
    'rubyRed': '#9B111E',
    'safetyOrange': '#FF6700',
    'salmonPink': '#FF91A4',
    'sapphireBlue': '#0067A5',
    'shadowBlue': '#778BA5',
    'shockingPinkCrayola': '#FF6FFF',
    'skyBlueCrayola': '#76D7EA',
    'skyMagenta': '#CF71AF',
    'slateGray': '#708090',
    'smokeyTopaz': '#933D41',
    'spartanCrimson': '#9E1316',
    'spunPearl': '#AAABB7',
    'steelPink': '#CC33CC',
    'strawberry': '#FC5A8D',
    'sunglowCrayola': '#FFCC33',
    'tangerineYellow': '#FFA812',
    'tartOrange': '#FB4D46',
    'tawnyPort': '#692545',
    'teaGreen': '#D0F0C0',
    'terraCotta': '#E2725B',
    'thistle': '#D8BFD8',
    'tumbleweed': '#DEAA88',
    'umber': '#635147',
    'valencia': '#D64550',
    'vanillaIce': '#F38FA9',
    'viridian': '#40826D',
    'wisteria': '#C9A0DC',
    'yellowGreen': '#9ACD32',
    'zaffreBlue': '#0014A8',
    'zinnwaldite': '#2C1608',
    'abyssalBlue': '#001B44',
    'aero': '#7CB9E8',
    'africanViolet': '#B284BE',
    'alienArmpit': '#84DE02',
    'amaranthPink': '#F19CBB',
    'amber': '#FFBF00',
    'amethyst': '#9966CC',
    'androidGreen': '#A4C639',
    'antiqueBronze': '#665D1E',
    'antiqueFuchsia': '#915C83',
    'appleGreen': '#8DB600',
    'aquaMarine': '#7FFFD4',
    'argent': '#C0C0C0',
    'artichoke': '#8F9779',
    'asparagus': '#87A96B',
    'atomicTangerine': '#FF9966',
    'auburn': '#A52A2A',
    'aureolin': '#FDEE00',
    'avocado': '#568203',
    'azureishWhite': '#DBE9F4',
    'babyBlueEyes': '#A1CAF1',
    'beauBlue': '#BCD4E6',
    'bitterLemon': '#CAE00D',
    'bittersweetShimmer': '#BF4F51',
    'blackBean': '#3D0C02',
    'blackCoral': '#54626F',
    'blackOlive': '#3B3C36',
    'blueGray': '#6699CC',
    'blueYonder': '#5072A7',
    'bondiBlue': '#0095B6',
    'bone': '#E3DAC9',
    'bottleGreen': '#006A4E',
    'brandy': '#87413F',
    'brightCerulean': '#1DACD6',
    'brightGreen': '#66FF00',
    'brilliantAzure': '#3399FF',
    'brilliantLavender': '#F4BBFF',
    'bronzeYellow': '#737000',
    'bubbles': '#E7FEFF',
    'buff': '#F0DC82',
    'cadetGrey': '#91A3B0',
    'calPolyPomonaGreen': '#1E4D2B',
    'camel': '#C19A6B',
    'cambridgeBlue': '#A3C1AD',
    'canaryYellow': '#FFEF00',
    'cardinal': '#C41E3A',
    'carminePink': '#EB4C42',
    'catawba': '#703642',
    'cedarChest': '#C95A49',
    'celestialBlue': '#4997D0',
    'cherryBlossomPink': '#FFB7C5',
    'chestnut': '#954535',
    'chineseRed': '#AA381E',
    'citrine': '#E4D00A',
    'cobaltBlue': '#0047AB',
    'cocoaBrown': '#D2691E',
    'columbiaBlue': '#C4D8E2',
    'copperRose': '#996666',
    'coyoteBrown': '#81613E',
    'cream': '#FFFDD0',
    'crimsonGlory': '#BE0032',
    'crystal': '#A7D8DE',
    'cultured': '#F5F5F5',
    'cypress': '#5C3317',
    'darkCornflowerBlue': '#26428B',
    'darkGreenBlue': '#1F262A',
    'darkGunmetal': '#1F262A',
    'darkLava': '#483C32',
    'deepGreenCyanTurquoise': '#0E7C61',
    'denim': '#1560BD',
    'deepSpaceSparkle': '#4A646C',
    'deepTaupe': '#7E5E60',
    'dollarBill': '#85BB65',
    'dukeBlue': '#00009C',
    'earthYellow': '#E1A95F',
    'eerieBlack': '#1B1B1B',
    'eggplant': '#614051',
    'egyptianBlue': '#1034A6',
    'electricGreen': '#00FF00',
    'electricUltramarine': '#3F00FF',
    'etonBlue': '#96C8A2',
    'fallow': '#C19A6B',
    'fandango': '#B53389',
    'fawn': '#E5AA70',
    'feldgrau': '#4D5D53',
    'flirt': '#A2006D',
    'forestGreenWeb': '#228B22',
    'frenchBeige': '#A67B5B',
    'frenchLime': '#CCFF00',
    'frenchWine': '#AC1E44',
    'frostbite': '#E936A7',
    'gamboge': '#E49B0F',
    'gin': '#E8F2EB',
    'glossyGrape': '#AB92B3',
    'grullo': '#A99A86',
    'guppieGreen': '#00FF7F',
    'heliotrope': '#DF73FF',
    'hollywoodCerise': '#F400A1',
    'honeydew': '#F0FFF0',
    'iceberg': '#71A6D2',
    'illuminatingEmerald': '#319177',
    'imperialRed': '#ED2939',
    'ivoryBlack': '#292421',
    'jasmineYellow': '#F8DE7E',
    'kobi': '#E79FC4',
    'lapisLazuli': '#26619C',
    'lava': '#CF1020',
    'laurel': '#A9BA9D',
    'lemonGlacier': '#FDFF00',
    'licorice': '#1A1110',
    'lincolnGreen': '#195905',
    'liverChestnut': '#987456',
    'majorelleBlue': '#6050DC',
    'marsRed': '#AD5140',
    'maximumBluePurple': '#ACACE6',
    'meatBrown': '#E5B73B',
    'mediumCarmine': '#AF4035',
    'mediumTurquoise': '#48D1CC',
    'mellowApricot': '#F8B878',
    'midnight': '#702670',
    'mindaro': '#E3F988',
    'moonstone': '#3AA8C1',
    'mulberry': '#C54B8C',
    'napierGreen': '#2A8000',
    'naplesYellow': '#FADA5E',
    'navyPurple': '#9457EB',
    'oceanGreen': '#48BF91',
    'oldRose': '#C08081',
    'paleLavender': '#BBA0CB',
    'palePink': '#FAD0C9',
    'paleTurquoise': '#AFEEEE',
    'paradisePink': '#E63B8C',
    'parisGreen': '#50C878',
    'pastelBlue': '#AEC6CF',
    'pastelGray': '#CFCFC4',
    'pastelGreen': '#77DD77',
    'pastelOrange': '#FFB347',
    'pastelPink': '#DEA5A4',
    'pastelPurple': '#B39EB5',
    'pastelRed': '#FF6961',
    'pastelYellow': '#FDFD96',
    'peach': '#FFDAB9',
    'peachPuff': '#FFDAB9',
    'pear': '#D1E231',
    'periwinkle': '#CCCCFF',
    'persianBlue': '#1C39BB',
    'persianGreen': '#00A693',
    'persianIndigo': '#32127A',
    'persianOrange': '#D84B16',
    'persianPink': '#F77FBE',
    'persianRed': '#D32F2F',
    'phlox': '#DF4ED5',
    'pink': '#FFC0CB',
    'pinkPearl': '#E7A1B0',
    'pistachio': '#93C572',
    'plum': '#8E4585',
    'plumWeb': '#DDA0DD',
    'portlandOrange': '#FF5A36',
    'powderBlue': '#B0E0E6',
    'princetonOrange': '#F58025',
    'purpleHeart': '#6A4C93',
    'purpleMountainMajesty': '#9B4F96',
    'purpleWeb': '#800080',
    'radicalRed': '#FF355E',
    'raspberry': '#E30B5C',
    'raspberryRose': '#B3446C',
    'red': '#FF0000',
    'redDevil': '#9B111E',
    'redOrange': '#FF5349',
    'redPink': '#F08A5D',
    'redPurple': '#9B1B30',
    'redSalsa': '#FD3A4A',
    'richBlack': '#004040',
    'rose': '#FF007F',
    'roseDust': '#9E5B40',
    'roseGold': '#B76E79',
    'roseMadder': '#E80054',
    'royalBlue': '#4169E1',
    'royalFuchsia': '#CA2C92',
    'ruby': '#E0115F',
    'ruddy': '#FF6347',
    'ruddyBrown': '#BB6528',
    'ruddyPink': '#F8A3A8',
    'russet': '#80461B',
    'rust': '#B7410E',
    'saffron': '#F4C430',
    'salmon': '#FA8072',
    'sapphire': '#0F52BA',
    'satinSheenGold': '#CBA135',
    'scarlet': '#FF2400',
    'scooter': '#1E98D2',
    'seaGreen': '#2E8B57',
    'seaShell': '#FFF5EE',
    'sepia': '#704214',
    'shadow': '#8A795D',
    'shamrockGreen': '#009E60',
    'shockingPink': '#FC0FC0',
    'silver': '#C0C0C0',
    'silverChalice': '#ACACAC',
    'silverLake': '#6B7C7E',
    'sinopia': '#CB4A3A',
    'skobeloff': '#007A5E',
    'slateBlue': '#6A5ACD',
    'slateGray': '#708090',
    'smitten': '#D99A6C',
    'snow': '#FFFAFA',
    'spice': '#7F3F3E',
    'springGreen': '#00FF7F',
    'sunflower': '#FFDA03',
    'tan': '#D2B48C',
    'tangerine': '#FF6347',
    'tartOrange': '#FB4D46',
    'teaRose': '#F4C2C2',
    'thistle': '#D8BFD8',
    'tomato': '#FF6347',
    'tropicalRainForest': '#00755E',
    'turquoise': '#40E0D0',
    'turquoiseBlue': '#00FFEF',
    'violet': '#8A2BE2',
    'violetRed': '#D02090',
    'violetWeb': '#EE82EE',
    'viridian': '#40826D',
    'wenge': '#645452',
    'wisteria': '#C9A0DC',
    'yellow': '#FFFF00',
    'yellowGreen': '#9ACD32',
    'yellowOrange': '#FFAE42'
}




# Color parser function
def color_parser(color_name):
    # Normalize the color name (case-insensitive)
    color_name = color_name.lower().strip()

    # Check if the color name exists in the color_names dictionary
    if color_name in color_names:
        # Get the hex code from the dictionary
        hex_code = color_names[color_name]  # This should be a string, not a dictionary

        # Get the RGB and HSL values
        rgb_value = hex_to_rgb(hex_code)
        hsl_value = hex_to_hsl(hex_code)

        # Return the results
        return {
            'color_name': color_name,
            'hex': hex_code,
            'rgb': rgb_value,
            'hsl': hsl_value
        }
    else:
        return f"Color name '{color_name}' not found."
