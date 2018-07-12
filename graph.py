from graphviz import Digraph, render
import mini_mundo
#---------------------------------------------DIVERSION-------------------------------------------------------------------------
global diversion
diversion = ['leisure','historic','touriusm','man_made','sport']
global leisure
global historic
global touriusm
global man_made
global sport
#---------------------------------------------HEALTH-------------------------------------------------------------------------
global health
health = ['emergency']

global emergency
emergency = ['medical_rescue', 'firefighters', 'lifeguards', 'other_Structure', 'other_Station']
global medical_rescue
global firefighters
global lifeguards
global other_Structure
global other_Station

#---------------------------------------------PACKAGED SERVICES--------------------------------------------------------------------------
global service
service = ['shop', 'amenity', 'craft']

global amenity
amenity = ['sustenance','education', 'transportation', 'financial', 'healthCare', 'entertainment', 'other_Amenity']
global sustenance
sustenance = ['bar','bbq','biergarten','cafe','drinking_water','fast_food','ice_cream','pub','restaurant']
global education
education = ['college', 'kindergarten', 'library', 'archive', 'public_bookcase', 'school', 'music_school',
             'driving_school', 'language_school', 'university', 'research_institute']
global transportation
transportation = ['bicycle_parking','bicycle_repair_station','bicycle_rental','boat_rental','bus_station', 'fuel',
                  'boat_sharing','bus_station','car_rental','car_sharing','car_wash','charging_station',
                  'ferry_terminal','grit_bin','motorcycle_parking','parking','parking_entrance','	parking_space',
                  'taxi','ticket_validator']
global financial
financial = ['atn','bank','bureau_de_change']
global healthCare
healthCare = ['baby_hatch','clinic','dentist','doctors','hospital','nursing_home','pharmacy','social_facility',
              'veterinary','blood_donation']
global entertainment
entertainment = ['arts_centre','brothel','casino','cinema','community_centre','fountain','gambling','nightclub',
                 'planetarium','social_centre','stripclub','studio','swingerclub','theatre']
global other_Amenity
other_Amenity = ['animal_boarding','animal_shelter','baking_oven','bench','clock','courthhouse','coworking_spece','creamtorium',
          'crypt','dive_centre','dojo','embassy','fire_station','game_feeding','grave_feeding','grave_yard','hunting_stand',
          'internet_cafe','kitchen','kneipp_water_cure','marketplace','photo_booth','place_of_worship','police','post_box',
          'post_office','prison','public_bath','ranger_station','recycling','rescue_station','sanitary_dump_station',
          'shelter','shower','table','telephone','toilets','townhall','vendingg_machine','wasted_disposal',
          'waste_transfer_station','watering_place','water_point']


global shop
shop = ['food_beverages','general_store','clothing_shoes_acessories','discount Store','health and beauty',
        'do_it_yourself','furniture_interior','eletronics','outdoors_sport','art_music_hobbies','stationery_gifts_books',
        'other_Shop']
global food_beverages
food_beverages = ['alcohol','bakery','beverages','brewing_supplies','butcher','cheese', 'chocolate','chocolate','coffee',
                  'confectionery','convenience','deli','dairy','farm','frozen_food','greengrocer','health_food','ice_cream',
                  'pasta','pastry','seafood','spices','tea','water']
global general_store
general_store = ['department_sote','general','kiosk','mail','supermarket','wholesale']
global clothing_shoes_acessories
clothing_shoes_acessories = ['baby_goods','bag','boutique','clothes','fabric','fashion','jewelry','leather','sewing',
                             'shoes','tailor','watches']
global discountStore
discountStore = ['charity','second_hand','variety_store']
global health_beaty
health_beaty = ['beauty','chemist','cosmetics','erotic','hairdresser','hairdresser_supply','hearing_aids','herbalist',
                'massage','medical_supply','nutrition_supplements','optician','perfumery','tattoo']
global do_it_yourself
do_it_yourself= ['agraria','appliance','bathoroom_furnishing','doityourself','electrical','energy','fireplace',
                         'florist','garden_centre','garden_furniture','gas','glaziery','hardware','houseware','locksmith',
                         'paint','security','trade']
global furniture_interior
furniture_interior = ['antique','bed','candles','carpet','curtain','doors','flooring','furniture','interior_decoration',
                      'kitchen','lamps','tiles','window_blind']
global eletronics
eletronics = ['computer','robot','electronics','hifi','mobile_phone','radiotechnics','vacuum_cleaner']
global outdoors_sport
outdoors_sport = ['atv','bicycle','boat','car','car_repair','car_parts','fuel','fishing','free_flying','hunting','jetski',
                  'motorcycle','outdoor','scuba_diving','ski','snowmobile','sports','swimming_pool','tyres']
global art_music_hobbies
art_music_hobbies = ['atr','collector','craft','frame','games','model','music','musical_instrument','photo','camera',
                     'trophy','video','video_games']
global stationery_gifts_books
stationery_gifts_books = ['anime','books','gift','lottery','newsagent','stationery','ticket']
global other_Shop
other_Shop = ['bookmaker','copyshop','dry_cleaning','e-cigarette','funeral_directors','laundry','money_lender','party',
              'pawnbroker','pet','pyrotechnics','religion','storage_rental','tobacco','toys','travel_agency','vacant',
              'weapons','user_defined']

global craft
craft = ['agricultura_engines', 'bakery', 'carpenter']

#-----------------------------------------------PACKAGE ROAD MESH----------------------------------------------------------------------
global road_mesh
road_mesh = ['highway', 'aerialway', 'aeroway', 'railway', 'public_transportation', 'route']

global aerialway
aerialway = ['cable_car','gondola','chair_lift','mixed_lift','drag_lift','t-bar','j-bar','rope_tow','magic_carpet','zip_line']
global aeroway
aeroway = ['aerodrome','apron','gate','hangar','helipad','heliport','navigationaid','runway','spaceport','taxilane',
           'taxiway','terminal','windsock']

global highway
highway = ['roads', 'linkRoads','special_road', 'path', 'lifecycle', 'other highway features']
global roads
roads = ['motorway','trunk','primary','secondary','tertiary','unclassified','residential','service']
global linkRoads
linkRoads = ['motorway_link','trunk_link','primary_link','secondary_link','tertiary_link']
global special_road
specialRoads = ['living_street','pedestrian','track','bus_guideway','escape','raceway','road']
global path
path = ['footway','bridleway','steps','path','cycleway','busway']
global lifecycle
lifecycle = ['proposed','construction']
global other_Highway
other_Highway = ['bus_stop','crossing','elevator','emergency_access_point','give_way','phone','mini_roundabout','motorway_junstion',
                'passing_place','rest_area','speed_camera','street_lamp','services','stop','traffic_signals','turning_circle',
                'User Defined']

global railway
railway = ['tracks', 'station_and_shop', 'other_Railway']
global tracks
tracks = ['abandoned','construction','disused','funicular','light_rail','miniature','monorail','narrow_gauge','preserved',
          'rail','subway','tram']
global station_and_shop
station_and_shop = ['halt','stop_position','platform','station','subway_entrance','tram_stop']
global other_Railway
other_Railway = ['buffer_stop','derail','crossing','level_crossing','signal','switch','railway_crossing','turntable',
                 'roundhouse','traverser','wash','user defined']

global public_transportation
public_transportation = ['stop_position','platform','station','stop_area']
global route
route = ['bicycle','bus','canoe','detour','ferry','fitness_trail','hiking','horse','inline_skates','light_rail','mtb',
         'nordic_walking','pipeline','piste','power','railway','road','running','ski','train','tram','User defined']


#-----------------------------------------------PACKAGE EDIFICATION--------------------------------------------------------------------
global edification
edification = ['place','office','building']

global place
global administratively_declared_places
global populated_settlements_urban
global pupulated_settlements_urban_and_rural
global other_places

global office

global building
building = ['accommodation','commercial','religious','civic_amenity','other_building']
global accommodation
global commercial
global religious
global civic_amenity
civic_amenity = ['university']
global other_building


#-----------------------------------------------STERIOTYPE-------------------------------------------------------------------


#-----------------------------------------------VARIAVEIS CONTROLE-----------------------------------------------------------
global contNode
global mother
contNode = 0
mother = {}
#-----------------------------------------------------------------------------------------------------------------------------

def driveGraph(listDic):
    listWay = listDic.copy()
    listService = []
    listRoadMesh = []
    listHealth = []
    listDiversion = []
    listEdification = []

    if not listWay:
        return "Graph failed!"
    else:
        for i in range(len(listWay)):  # separate the entities according to packages
            for j in listWay[i].keys():
                if j in service:
                    if 'amenity' in listWay[i].keys():
                        if listWay[i]['amenity'] in healthCare:
                            print("health " + listWay[i]['name'])
                            listHealth.append(listWay[i].copy())
                        elif listWay[i]['amenity'] in entertainment:
                            print("diversion " + listWay[i]['name'])
                            listDiversion.append(listWay[i].copy())
                        else:
                            print("service " + listWay[i]['name'])
                            listService.append(listWay[i].copy())
                if j in road_mesh:
                    listRoadMesh.append(listWay[i].copy())
                if j in edification:
                    listEdification.append(listWay[i].copy())

        arq = open("schema.gv", 'w+')
        arq.write("digraph structs { \n\tnode [shape=box]")

        diversionGraph(arq, listDiversion)
        serviceGraph(arq, listService)
        emergencyGraph(arq, listHealth)
        roadMeshGraph(arq, listRoadMesh)
        edificationGraph(arq, listEdification)
        findRelation(arq)

        arq.write("\n\trankdir=BT\n\tsplines=ortho\n}")
        arq.close()

        render('dot', 'png', 'schema.gv')
    return "Graph checked!\n"


######################################################################################### DIVERSION
def findClassDiversion(tag):
    if tag in entertainment:
        return "entertainment"
    return


def diversionGraph(arq, listDiversion):
    arq.write(initPackage("DIVERSION"))
    packageRelation(arq, listDiversion, "amenity", "diversion")  ##AMENITY
    subGraph(arq, "Diversion", diversion, listDiversion)

    return "DIVERSION checked!"


######################################################################################### HEALTH
def findClassHealth(tag):
    if tag in healthCare:
        return "healthCare"
    return


def emergencyGraph(arq, listHealth):
    arq.write(initPackage("HEALTH"))
    packageRelation(arq, listHealth, "amenity", "health")  ##AMENITY
    subGraph(arq, "health", health, listHealth)

    return "HEALTH checked!"


######################################################################################### ROAD MESH
def findClassroad_mesh(tag):
    if tag in roads:
        return "roads"
    elif tag in path:
        return "path"
    elif tag in linkRoads:
        return "link Roads"
    elif tag in lifecycle:
        return "life cycle"
    elif tag in specialRoads:
        return "special roads"
    elif tag in other_Highway:
        return "other highway features"

    elif tag in tracks:
        return "tracks"
    elif tag in station_and_shop:
        return "statoin and shop"
    elif tag in other_Railway:
        return "other railway"

def roadMeshGraph(arq, listRoadMesh):
    arq.write(initPackage("ROAD_MESH"))
    subGraph(arq, "road_mesh", road_mesh, listRoadMesh)

    return "road_mesh checked!"


######################################################################################### EDIFICATION
def findClassEdification(tag):
    if tag in civic_amenity:
        return "civic_amenity"
    return


def edificationGraph(arq, listEdification):
    arq.write(initPackage("EDIFICATION"))
    subGraph(arq, "edification", edification, listEdification)

    return "EDIFICATION checked!"


######################################################################################### SERVICES
def findClassService(tag):
    if tag in education:
        return "education"
    elif tag in transportation:
        return "transportation"
    elif tag in sustenance:
        return "sustenance"
    elif tag in financial:
        return "financial"
    elif tag in other_Amenity:
        return "other_Amenity"

    elif tag in general_store:
        return "general_store"
    elif tag in do_it_yourself:
        return "do_it_yourself"
    elif tag in eletronics:
        return "eletronics"
    elif tag in health_beaty:
        return "health and beauty"
    elif tag in food_beverages:
        return "food_beverages"
    elif tag in furniture_interior:
        return "furniture_interior"
    elif tag in outdoors_sport:
        return "outdoors_sport"
    elif tag in discountStore:
        return "discount_Store"
    elif tag in clothing_shoes_acessories:
        return "clothing_shoes_acessories"
    elif tag in art_music_hobbies:
        return "art_music_hobbies"
    elif tag in stationery_gifts_books:
        return "stationary_gifts_books"


def serviceGraph(arq, listService):
    arq.write(initPackage("SERVICES"))
    subGraph(arq, "service", service, listService)

    return "Services checked!"


######################################################################################### CLASS_xml
def initPackage(name):
    return ("\n\tsubgraph cluster_" + name + " {" +
            "\n\t\tnode [color=black style=filled]" +
            "\n\t\tcolor=lightgrey style=filled" +
            "\n\t\tlabel=" + name)


def subGraph(arq, namePackage, package, list):
    flg = []
    global contNode  # HOW MANY NODES HAS IN THE SCHEMA
    global mother  # SAVE ALL CLASSES WITH YOUR KEYS, WILL USE FOR FIND RELATION
    listControlMain = []  # SECURITY FLAG, USED FOR TO KNOW IF MAINCLASS(AMENITY, SHOP, HIGHWAY) WAS GENERATED
    listControlSub = []
    listControlthird = []

    for k in package:
        for i in range(len(list)):  ##  TABLE NAME = university, third level
            if k in list[i] and list[i][k] not in listControlthird:
                arq.write(entityName(contNode, list[i][k], entityStereotype(list[i]["stereotype"])))
                mother[list[i][k]] = contNode
                flg.append(findClass(namePackage, list[i][k]))
                contNode = contNode + 1
                arq.write("\n\t\t\t<hr/>")
                for j in list[i].keys():  ##  TABLE ATT
                    if "stereotype" not in j and "lat" not in j and "lon" not in j and k not in j:
                        arq.write(entityAtt(j))
                arq.write(entityAtt("coordinates") + "\n\t\t\t</TABLE>>]")
                listControlthird.append(list[i][k])
                if k not in listControlMain:
                    arq.write(entityName(contNode, k, entityStereotype(
                        None)) + "\n\t\t\t</TABLE>>]")  ## MainClass = highway FIRST LEVEL
                    mother[k] = contNode
                    contNode = contNode + 1
                    listControlMain.append(k)

    for i in range(len(flg)):  ## SubClasses = roads, path SECOND LEVEL
        if flg[i] not in listControlSub:
            arq.write(entityName(contNode, flg[i], entityStereotype(None)) + "\n\t\t\t</TABLE>>]")
            mother[flg[i]] = contNode
            contNode = contNode + 1
            listControlSub.append(flg[i])
    arq.write("\n\t}")


def entityName(contNode, list, stereotype):
    return ("\n\t\t" + str(contNode) + "[style = \"filled, bold\" penwidth = \"1\" fillcolor=\"white\" label=<" +
            "\n\t\t\t<TABLE color=\"black\" border=\"0\">" +
            "\n\t\t\t <TR>" +
            "\n\t\t\t\t<TD align=\"center\"><font color=\"black\">" + str(list) + "</font>" +
            stereotype + "\n\t\t\t</TR>")


def entityStereotype(name):
    stereotype = "  "
    if name == "line":
        stereotype += "\n\t\t\t\t<font FACE=\"sigmoda\" POINT-SIZE=\"20.0\"> w</font>"
    if name == "point":
        stereotype += "\n\t\t\t\t<font FACE=\"sigmoda\" POINT-SIZE=\"20.0\"> b</font>"
    if name == "polygon":
        stereotype += "\n\t\t\t\t<font FACE=\"sigmoda\" POINT-SIZE=\"20.0\"> e</font>"

    stereotype += "</TD>"
    return stereotype


def entityAtt(valor):
    return ("\n\t\t\t<TR>" +
            "\n\t\t\t\t<TD align=\"left\">" + valor + "</TD>" +
            "\n\t\t\t </TR>")


def findClass(name, tag):
    if name == 'road_mesh':
        return findClassroad_mesh(tag)
    elif name == 'service':
        return findClassService(tag)
    elif name == 'health':
        return findClassHealth(tag)
    elif name == 'diversion':
        return findClassDiversion(tag)
    elif name == 'edification':
        return findClassEdification(tag)


######################################################################################### REALATION
def entityRelation(slave, master):
    return ("\n\t\t" + str(slave) + " -> " + str(master) + "[arrowhead=onormal]")


def findRelation(arq):
    global mother
    print(mother)
    for i in mother:
        if i in education:
            arq.write(entityRelation(mother[i], mother['education']))
        if i in transportation:
            arq.write(entityRelation(mother[i], mother['transportation']))
        elif i in entertainment:
            arq.write(entityRelation(mother[i], mother['entertainment']))
        elif i in healthCare:
            arq.write(entityRelation(mother[i], mother['healthCare']))
        elif i in amenity:
            arq.write(entityRelation(mother[i], mother['amenity']))
        elif i in art_music_hobbies:
            arq.write(entityRelation(mother[i], mother['art_music_hobbies']))
        elif i in shop:
            arq.write(entityRelation(mother[i], mother['shop']))
        elif i in other_Highway:
            arq.write(entityRelation(mother[i], mother['other highway features']))
        elif i in roads:
            arq.write(entityRelation(mother[i], mother['roads']))
        elif i in highway:
            arq.write(entityRelation(mother[i], mother['highway']))
        elif i in civic_amenity:
            arq.write(entityRelation(mother[i], mother['civic_amenity']))
        elif i in building:
            arq.write(entityRelation(mother[i], mother['building']))
    return print("\nRelation checked!")


def packageRelation(arq, list, name, packageName):
    flg = []
    global contNode
    global mother

    for i in range(len(list)):  ##  NOME TABELA
        if name in list[i]:
            arq.write(entityName(contNode, list[i][name], entityStereotype(list[i]["stereotype"])))
            mother[list[i]['amenity']] = contNode

            if packageName == 'health':
                flg.append(findClassHealth(list[i]['amenity']))
            elif packageName == 'diversion':
                flg.append(findClassDiversion(list[i]['amenity']))

            contNode = contNode + 1
            arq.write("\n\t\t\t<hr/>")
            for j in list[i].keys():  ##  ATRIBUTOS TABELA
                if "stereotype" not in j and "lat" not in j and "lon" not in j and name not in j:
                    arq.write(entityAtt(j))
            arq.write(entityAtt("coordenadas") + "\n\t\t\t</TABLE>>]")

    for i in range(len(flg)):  ## SubClasses = HEALTHCARE .....
        arq.write(entityName(contNode, flg[i], entityStereotype(None)) + "\n\t\t\t</TABLE>>]")
        mother[flg[i]] = contNode
        contNode = contNode + 1



# def serviceGraph(arq, listService):
#     flg=[]
#     global contNode
#     global mother
#
#     arq.write(initPackage("SERVICES"))
#     ##AMENITY
#     for i in range(len(listService)):##  NOME TABELA
#         arq.write(entityName(contNode,listService[i]['amenity']))
#         mother[listService[i]['amenity']] =  contNode
#         flg.append(findClassService(listService[i]['amenity']))
#         contNode = contNode+1
#         for j in listService[i].keys():##  ATRIBUTOS TABELA
#             if "lat" not in j and "lon" not in j and "amenity" not in j:
#                 arq.write(entityAtt(j))
#         arq.write(entityAtt("coordenadas")+"\n\t\t\t</TABLE>>]")
#
#     for i in range(len(flg)):## SubClasses = transportation, education .....
#         arq.write(entityName(contNode,flg[i])+"\n\t\t\t</TABLE>>]")
#         mother[flg[i]] = contNode
#         contNode = contNode +1
#     arq.write(entityName(contNode,"amenity")+"\n\t\t\t</TABLE>>]"+"\n\t}") ## MainClass = amenity
#     mother['amenity'] = contNode
#     contNode = contNode+1
#
#     print(flg)
#     print(mother)
#     return "Services checked!"
