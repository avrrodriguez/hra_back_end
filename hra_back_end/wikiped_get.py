import requests
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def wiki_rec(PARAMS):
    '''
    Makes get request to wikipedia based on the parameters given
    '''
    BASE = "https://en.wikipedia.org/w/api.php"

    S = requests.Session()

    wikiInfo = S.get(url=BASE, params=PARAMS)

    Info_json = wikiInfo.json()

    return Info_json


def remove_nonwords(info):
    '''
    Turns list from multiple lists to one list
    '''
    new_list = ""

    for element in info:
        for i in element:
            if i.lower() in 'abcdefghijklmnopqrstuvwxyz' or i == " ":
                new_list += i

    new_list = new_list.split(" ")

    return new_list


def get_dict(cat_list):
    '''
    Turns list of hobbies cats into dictionary
    '''
    hob_dict = {}
    for i in range(len(cat_list)):
        if cat_list[i] in ["hobbies", "Indoors", "Outdoors"]:
            if cat_list[i] == "hobbies" and (cat_list[i-1] not in "to, of"):
                hob_dict[f"{cat_list[i-1]} "+ f"{cat_list[i]}"] = None

    hob_dict["General hobbies"] = {"General": None, "Outdoors and Sports": None}
    hob_dict["Collection hobbies"] = {"Indoors": None, "Outdoors": None}
    hob_dict["Competitive hobbies"] = {"Indoors": None, "Outdoors": None}
    hob_dict["Observation hobbies"] = {"Indoors": None, "Outdoors": None}
    

    return hob_dict


def clean_up_categories(wiki_info):
    '''
    It gets only the categories of the hobbies from the get request
    dictionary, and removes the ===\n\n\n=== present in the data
    '''
    find_info = wiki_info["query"]["pages"]["31257416"]["extract"]
    find_info = find_info.split("===\n\n\n===")

    cleaned_info = remove_nonwords(find_info)
    hobby_dict = get_dict(cleaned_info)

    return hobby_dict


def hobbies():
    '''
    All hobbies taken from wikipedia, put into appropriate categories in a dictionary
    '''
    general_hobbies_list = ["3D printing", "Acroyoga", "Acting", "Acting", "Animation", "Anime", "Aquascaping", "Art", "Astrology", "Baking", "Barbershop Music", "Baton twirling", "Beatboxing", "Beer tasting", "Bell ringing", "Binge watching", "Blogging", "Board/tabletop games", "Book discussion clubs", "Book restoration", "Bowling", "Brazilian jiu-jitsu", "Breadmaking", "Bullet jornaling", "Calligraphy", "Candle making", "Candy making", "Car spotting", "Car fixing & building", "Card games", "Cardistry", "Ceramics", "Chatting", "Cheesemaking", "Chess", "Cleaning", "Clothesmaking", "Coffee roasting", "Collecting", "Coloring", "Communication", "Community activism", "Computer programming", "Confectionery", "Conlanging", "Construction", "Cooking", "Cosplaying", "Couch surfing", "Couponing", "Craft", "Creative writing", "Crocheting", "Cross-stitch", "Crossword puzzles", "Cryptography", "Cue sports", "Dance", "Decorating", "Digital arts", "Dining", "Diorama", "Distro Hopping", "Diving", "Diorama", "Distro Hopping", "Diving", "Djembe", "Djing", "Do it yourself", "Drama", "Drawing", "Drink Mixing", "Electronic games", "Electronics", "Embroidery", "Engraving", "Entertaining", "Experimenting", "Fantasy sports", "Fashion", "Fashion design", "Feng shui decorating", "Filmmaking", "Fingerpainting", "Fishfarming", "Fishkeeping", "Flower arranging", "Fly tying", "Foreign language learning", "Furniture building", "Gaming (tabletop games, role-playing games, Electronic games)", "Geneology", "Gingerbread house making", "Giving advice", "glassblowing", "Gardening", "Gunsmithing", "Hacking", "Hardware", "Herp keeping", "Home improvement", "Homebrewing", "Houseplant care", "Hula hooping", "Humor", "Hydrodipping", "Hydroponics", "Ice skating", "Inventing", "Jewelry making", "Jigsaw puzzles", "Journaling", "Juggling", "Karaoke", "Karate", "Kendama", "Knife making", "Knitting", "Knot tying", "Kombucha brewing", "Kung fu", "Lace making", "Lapidary", "Leather crafting", "Lego building", "Livestreaming", "Listening to music", "Listening to podcasts", "Lock picking", "Machining", "Macrame", "Magic", "Makeup", "Manga", "Massaging", "Mazes (indoor/outdoor)", "Mechanics", "Meditation", "Memory training", "Metalworking", "Miniature art", "Minimalism", "Model building", "Modeling", "Model engineering", "Music", "Nail art", "Needlepoint", "Origami", "Painting", "Pen Spinning", "Performance", "Pet", "Pet adoption & fostering", "Pet sitting", "Philately", "Photography", "Pilates", "Planning", "Plastic art", "Playing musical instruments", "Poetry", "Poi", "Pole dancing", "Postcrossing", "Pottery", "Power Nap", "Practical jokes", "Pressed flower craft", "Proofreading and editing", "Proverbs", "Public speaking", "Puppetry", "Puzzles", "Pyrography", "Quilling", "Quilting", "Quizzes", "Radio-controlled model playing", "Rail transport modeling", "Rapping", "Reading", "Recipe creation", "Redefining", "Reiki", "Reviewing Gadgets", "Robot combat", "Rubik's Cube", "Scrapbooking", "Scuba Diving", "Sculpting", "Sewing", "Shoemaking", "Singing", "Sketching", "Skipping rope", "Slot car", "Soapmaking", "Social media", "Spreadsheets", "Stamp collecting", "Stand-up comedy", "Storytelling", "Stretching", "Stripping", "Sudoku", "Talking", "Tapestry", "Tarot", "diorama", "Tattooing", "Taxidermy", "Telling jokes", "Thrifting", "Upcycling", "Video editing", "Video game developing", "Video gaming", "Video making", "VR Gaming", "Wargaming", "Watch making", "Watching documentaries", "Watching movies", "Watching television", "Wax sealing", "Waxing", "Weaving", "Webtoooning", "Weight training", "Welding", "Whisky", "Whittling", "Wikipedia editing", "Wine tasting", "Winemaking", "Witchcraft", "Wood carving", "Woodworking", "Word searches", "Worldbuilding", "Writing", "Writing music", "Yo-yoing", "Yoga", "Zumba"]

    general_hobbies_outdoors = ["Air sports", "Airsoft", "amateur geology", "Amusement park visiting", "Archery", "Auto detailing", "Automobolism", "Astronomy", "Backpacking", "Badminton", "BASE jumping", "Baseball", "Basketball", "Beachcombing", "Beekeeping", "Birdwatching", "Blacksmithing", "BMX", "Board sports", "Bodybuilding", "Bonsai", "Bus riding", "Camping", "Canoeing", "Canyoning", "Car riding", "Car tuning", "Caving", "City trip", "Climbing", "Composting", "Croquet", "Cycling", "Dandyism", "Darts", "Dog training", "Dowsing", "Driving", "Farming", "Fishing", "Flag football", "Flower growing", "Flying", "Flying disc", "Flying model planes", "Foraging", "Fossicking", "Freestyle football", "Fruit picking", "Gardening", "Geocaching", "Ghost hunting", "Gold prospecting", "Graffiti", "Groundhopping", "Guerrilla gardening", "Gymnastics", "Handball", "Herbalism", "Herping", "High-power rochetry", "Hiking", "Hobby horsing", "Hobby tunneling", "Hooping", "Horseback riding", "Hunting", "Inline skating", "Jogging", "Jumping rope", "Karting", "Kayaking", "Kite flying", "Kitesurfing", "Lacrosse", "LARPing", "Letterboxing", "Lomography", "Longboarding", "Martial arts", "Metal detecting", "Motorcycling", "Meteorology","Model trains", "Motor sports", "Mounting biking", "Mountaineering", "Museum visiting", "Mushroom hunting/mycology", "Netball", "Nooding", "Nordic skating", "Orienteering", "Paintball", "Paragliding", "Parkour", "Photography", "Pickleball", "Picnicking", "Podcast hosting", "Polo", "Powerlifting", "Public transport riding", "Qigong", "Radio-controlled model playing", "Rafting", "Railway journeys", "Rappelling", "Renaissance fair", "Renovating", "Road biking", "Rock climbing", "Rock painting", "Roller skating", "Rugby", "Running", "Safari", "Sailing", "Sand art", "Scouting", "Scuba diving", "Rowing", "Shooting", "Shopping", "Shuffleboard", "Skateboarding", "Skiing", "Skimboarding", "Skydiving", "Slacklining", "Sledding", "Snorkeling", "Snowboarding", "Snowmobiling", "Snowshoeing", "Soccer", "Stone skipping", "Storm chasing", "Sun bathing", "Surfing", "Survivalism", "Swimming", "Table tennis playing", "Taekwondo", "Tai chi", "Tennis", "Thru-hiking", "Topiary", "Tourism", "Trade fair visiting", "Travel", "Unicycling", "Urban exploration", "Vacation", "Vegetable farming", "Vehicle restoration", "Videography", "Volleyball", "Volunteering", "Walking", "Water sports", "Zoo visiting"]

    educational_hobbies_list = ["Archaeology", "Astronomy", "Animation", "Aerospace", "Biology", "Botany", "Business", "Chemistry", "English", "Entrepreneurship", "Geography", "History", "Literature", "Mathematics", "Medical science", "Microbiology", "Mycology", "Neuroscience", "philosophy", "Physics", "Psychology", "Railway studies", "Research", "Science and technology studies", "Social studies", "Sociology", "Sports science", "Story Writing", "Life Science", "Teaching", "Web design"]

    collection_hobbies_indoors = ["Action figure", "Antiquing", "Ant-keeping", "Art collecting", "Book collecting", "Button collecting", "Cartophily", "Coin collecting", "Comic book collecting", "Compact discs", "Crystals", "Deltiology", "Die-cast toy", "Digital hoarding", "Dolls", "Element collecting", "Ephemera collecting", "Fusilately", "Knife collecting", "Lotology", "Movie memorabilia collecting", "Perfume", "Philately", "Phillumeny", "Radio-controlled model collecting", "Rail transport modelling", "Rock tumbling", "Scutelliphily", "Shoes", "Slot car", "Sports memorabilia", "Stamp collecting", "Stuffed toy collecting", "Tea bag collecting", "Ticket collecting", "Transit map collecting", "Video game collecting", "Vintage cars", "Vintage clothing", "Vinyl Records", "Wikipedia editing"]

    collection_hobbies_outdoors = ["Antiquities", "Auto audiophilia", "Flower collecting and pressing", "Fossil hunting", "Insect collecting", "Leaves", "Magnet fishing", "Metal detecting", "Mineral collecting", "Rock balancing", "Sea glass collecting", "Seashell collecting", "Stone collecting"]

    competitive_hobbies_indoors = ["Air hockey", "Animal fancy", "Axe throwing", "Backgammon", "Badminton", "Baking", "Ballet dancing", "Ballroom dancing", "Baton twirling", "Beauty pageants", "Billiards", "Bowling", "Cooking", "Bridge", "Checkers", "Cheerleading", "Chess", "Color guard", "Cribbage", "Curling", "Dancing", "Darts", "Debate", "Dominoes", "Eating", "Esports", "Fencing", "Figure Skating", "Go", "Gymnastics", "Ice hockey", "Ice skating", "Judo", "Jujitsu", "Kabaddi", "Knowledge/word games", "Laser tag", "Magic","Mahjong", "Marbles", "Martial arts", "Model racing", "Model United Nations", "Poker", "Pole dancing", "Pool", "Radio-controlled model playing", "Role-playing games", "Rughooking", "Shogi", "Slot car racing", "Speedcubing", "Sport stacking", "Table football", "Table tennis", "Volleyball", "Video gaming", "VR Gaming", "Weightlifting", "Wrestling"]

    competitive_hobbies_outdoors = ["Airsoft", "Archery", "Association football", "Australian rules football", "Auto racing", "Baseball", "Beach volleyball", "Breakdancing", "Climbing", "Cornhole", "Cricket", "Croquet", "Cycling", "Disc gold", "Dog sport", "Equestrianism", "Exhibition drill", "Field hockey", "Figure skating", "Fishing", "Fitness", "Football", "Frisbee", "Golfing", "Handball", "Horseback riding", "Horsemanship", "Horseshoes", "Iceboat racing", "Jukskei", "Kart racing", "Knife throwing", "Lacrosse", "Longboarding", "Long-distance running", "Marching band", "Mini Gold", "Model aircraft", "Orienteering", "Pickleball", "Powerboat racing", "Quidditch", "Race walking", "Racquetball", "Radio-controlled car racing", "Radio-controlled model playing", "Roller derby", "Rugby league football", "Rowing", "Shooting sports", "Skateboarding", "Skiing", "Sled dog racing", "Softball", "Speed skating", "Squash", "Surfing", "Swimming", "Table tennis", "Tennis", "Tennis polo", "Tether car", "Tour skating", "Tourism", "Trapshooting", "Triathlon", "Ultimate frisbee", "Volleyball", "Water polo"]

    observation_hobbies_indoors = ["Audiophile", "Fishkeeping", "Learning", "Meditation", "Microscopy", "Reading", "Research", "Shortwave listening"]

    observation_hobbies_outdoors = ["Aircraft spotting", "Amateur astronomy", "benchmarking", "Birdwatching", "Bus spotting", "Butterfly watching", "Geocaching", "Gongoozling", "Herping", "Hiking/backpacking", "Meteorology", "People-watching", "Photography", "Satellite watching", "Trainspotting", "Whale watching"]

    return general_hobbies_list, general_hobbies_outdoors, educational_hobbies_list,collection_hobbies_indoors, collection_hobbies_outdoors, competitive_hobbies_indoors, competitive_hobbies_outdoors, observation_hobbies_indoors,observation_hobbies_outdoors



def hobbies_dict(cat_dict):

    hobbies_list = hobbies()

    cat_dict["General hobbies"]["General"] = hobbies_list[0]
    cat_dict["General hobbies"]["Outdoors and Sports"] = hobbies_list[1]
    cat_dict["Educational hobbies"] = hobbies_list[2]
    cat_dict["Collection hobbies"]["Indoors"] = hobbies_list[3]
    cat_dict["Collection hobbies"]["Outdoors"] = hobbies_list[4]
    cat_dict["Competitive hobbies"]["Indoors"] = hobbies_list[5]
    cat_dict["Competitive hobbies"]["Outdoors"] = hobbies_list[6]
    cat_dict["Observation hobbies"]["Indoors"] = hobbies_list[7]
    cat_dict["Observation hobbies"]["Outdoors"] = hobbies_list[8]

    return cat_dict



def main():
    '''
    Get categories and content from a wikipedia page and turning it
    into a nested dictionary with hobbies inside their categories
    '''

    PARAMS_cats = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "explaintext": 1,
        "titles": "List of hobbies"
    }

    Hobby_cats = wiki_rec(PARAMS_cats)

    hobby_cat_dict = clean_up_categories(Hobby_cats)
    completed_hobby_dict = hobbies_dict(hobby_cat_dict)
    

    return completed_hobby_dict

@app.route('/')
@cross_origin()
def route():
    dict_hobbies = main()
    return dict_hobbies

if __name__ == "__main__":
    app.run(debug=True)