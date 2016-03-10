from .features import Dictionary, RegexMatches, Stopwords

name = "polish"

try:
    import enchant
    dictionary = enchant.Dict("pl")
except enchant.errors.DictNotFoundError:
    raise ImportError("No enchant-compatible dictionary found for 'pl'.  " +
                      "Consider installing 'aspell-pl'.")

dictionary = Dictionary(name + ".dictionary", dictionary.check)
"""
:class:`~revscoring.languages.features.Dictionary` features via
:class:`enchant.Dict` "pl".  Provided by `aspell-pl`
"""

stopwords = [
    r"aby",
    r"ale",
    r"and",
    r"artykuł",
    r"autor",
    r"bardzo",
    r"bez",
    r"bibliografia",
    r"border",
    r"by",
    r"być",
    r"był",
    r"była",
    r"było",
    r"były",
    r"category",
    r"center",
    r"com",
    r"commons",
    r"cytuj",
    r"czasie",
    r"czerwca",
    r"czy",
    r"czyli",
    r"często",
    r"części",
    r"część",
    r"data",
    r"defaultsort",
    r"di",
    r"dla",
    r"do",
    r"dopracować",
    r"dostępu",
    r"dwa",
    r"dwóch",
    r"dzięki",
    r"em",
    r"fakt",
    r"flaga",
    r"gdy",
    r"gdzie",
    r"go",
    r"grafika",
    r"grafiki",
    r"grudnia",
    r"głównie",
    r"historia",
    r"ich",
    r"ii",
    r"iii",
    r"im",
    r"image",
    r"imię",
    r"in",
    r"inde",
    r"infobo",
    r"inne",
    r"innych",
    r"isbn",
    r"jak",
    r"jako",
    r"jan",
    r"je",
    r"jeden",
    r"jednak",
    r"jednym",
    r"jego",
    r"jej",
    r"jest",
    r"jeszcze",
    r"jpg",
    r"już",
    r"język",
    r"kategoria",
    r"kiedy",
    r"kilka",
    r"koniec",
    r"książkę",
    r"która",
    r"które",
    r"którego",
    r"której",
    r"który",
    r"których",
    r"którym",
    r"kwietnia",
    r"lata",
    r"latach",
    r"left",
    r"liczba",
    r"link",
    r"linki",
    r"lipca",
    r"listopada",
    r"lub",
    r"ma",
    r"maja",
    r"mają",
    r"marca",
    r"miasta",
    r"miasto",
    r"miał",
    r"miejsce",
    r"między",
    r"może",
    r"można",
    r"mu",
    r"nad",
    r"należy",
    r"name",
    r"następnie",
    r"natomiast",
    r"nawet",
    r"nazwa",
    r"nazwisko",
    r"nazwy",
    r"nbsp",
    r"nich",
    r"nie",
    r"nim",
    r"niż",
    r"nowy",
    r"np",
    r"nr",
    r"obecnie",
    r"od",
    r"of",
    r"ok",
    r"około",
    r"okresie",
    r"old",
    r"on",
    r"ona",
    r"opis",
    r"opublikowany",
    r"oraz",
    r"org",
    r"państwo",
    r"października",
    r"php",
    r"pierwsze",
    r"pierwszy",
    r"plik",
    r"png",
    r"po",
    r"pod",
    r"podczas",
    r"pol",
    r"polsce",
    r"polska",
    r"polski",
    r"polskie",
    r"polskiego",
    r"polskiej",
    r"ponad",
    r"przed",
    r"przez",
    r"przy",
    r"przypisy",
    r"później",
    r"right",
    r"rodzaj",
    r"rok",
    r"roku",
    r"również",
    r"sierpnia",
    r"się",
    r"sposób",
    r"strona",
    r"strony",
    r"stronę",
    r"stub",
    r"stycznia",
    r"style",
    r"są",
    r"tak",
    r"także",
    r"tam",
    r"tego",
    r"tej",
    r"ten",
    r"też",
    r"the",
    r"thumb",
    r"trzy",
    r"tych",
    r"tylko",
    r"tym",
    r"typ",
    r"tytuł",
    r"tzw",
    r"url",
    r"urodzeni",
    r"usa",
    r"warszawa",
    r"we",
    r"według",
    r"wg",
    r"width",
    r"wiek",
    r"wieku",
    r"wiele",
    r"wielu",
    r"wikipedia",
    r"wojna",
    r"wojny",
    r"wraz",
    r"września",
    r"wszystkich",
    r"wszystkie",
    r"www",
    r"wydawca",
    r"wydawnictwo",
    r"zdjęcia",
    r"zdjęcie",
    r"ze",
    r"zewnętrzne",
    r"zm",
    r"znaczenia",
    r"znajduje",
    r"zobacz",
    r"został",
    r"została",
    r"zostały",
    r"ów",
    r"śmierci",
    r"źródła",
    r"że",
    r"życia"
]

stopwords = Stopwords(name + ".stopwords", stopwords)
"""
:class:`~revscoring.languages.features.Stopwords` features copied from
"common words" in https://meta.wikimedia.org/w/index.php?diff=13836514
"""

badword_regexes = [
    r"burdel",
    r"burdelu",
    r"chuj",
    r"chuja",
    r"chuje",
    r"chujowy",
    r"chuju",
    r"chój",
    r"ciota",
    r"cioty",
    r"cipa",
    r"cipe",
    r"cipie",
    r"cipka",
    r"cipki",
    r"cipy",
    r"cwel",
    r"cwele",
    r"cycki",
    r"debil",
    r"debile",
    r"debili",
    r"downa",
    r"dupa",
    r"dupe",
    r"dupeczki",
    r"dupek",
    r"dupie",
    r"dupsko",
    r"dupy",
    r"dupę",
    r"dziwek",
    r"dziwka",
    r"dziwki",
    r"elo",
    r"fiut",
    r"fiuta",
    r"fuck",
    r"gej",
    r"gejem",
    r"glupi",
    r"glupia",
    r"glupie",
    r"gowno",
    r"gunwo",
    r"gupia",
    r"guwno",
    r"gówna",
    r"gównem",
    r"gówno",
    r"huj",
    r"huja",
    r"huje",
    r"hujem",
    r"hujowa",
    r"hujowy",
    r"huju",
    r"hwdp",
    r"idiota",
    r"idioto",
    r"japierdole",
    r"jebac",
    r"jebana",
    r"jebane",
    r"jebany",
    r"jebać",
    r"jebał",
    r"jebcie",
    r"jebie",
    r"joł",
    r"kiblu",
    r"koles",
    r"kupa",
    r"kupe",
    r"kupy",
    r"kupą",
    r"kupę",
    r"kurwa",
    r"kurwy",
    r"kutafon",
    r"kutas",
    r"kutasa",
    r"kutasem",
    r"kutasiarz",
    r"kutasy",
    r"lalala",
    r"loda",
    r"lol",
    r"mać",
    r"noob",
    r"nooby",
    r"pała",
    r"pałe",
    r"pały",
    r"pałę",
    r"pedal",
    r"pedaly",
    r"pedał",
    r"pedałem",
    r"pedały",
    r"penis",
    r"penisa",
    r"penisy",
    r"piedol",
    r"pierdole",
    r"pierdolone",
    r"pierdolony",
    r"pisior",
    r"pizda",
    r"pizdy",
    r"piździe",
    r"pojebane",
    r"przygłup",
    r"przygłupa",
    r"przygłupów",
    r"pupa",
    r"redtube",
    r"rucha",
    r"ruchania",
    r"ruchanie",
    r"ruchaniu",
    r"ryj",
    r"skurwiel",
    r"skurwysyn",
    r"smierdzi",
    r"spierdalaj",
    r"sraczka",
    r"sraka",
    r"sraką",
    r"sranie",
    r"sraniu",
    r"ssie",
    r"ssij",
    r"ssijcie",
    r"syf",
    r"szmata",
    r"technotłuki",
    r"wiocha",
    r"wogule",
    r"wpierdol",
    r"wpierdoli",
    r"wyruchany",
    r"zadupie",
    r"zajebista",
    r"zajebisty",
    r"zajebiście",
    r"zapierdala",
    r"ziom",
    r"ziomki",
    r"ziomy",
    r"zjeb",
    r"zjebany",
    r"śmierdzi",
    r"śmierdziele",
    r"żul"
]

badwords = RegexMatches(name + ".badwords", badword_regexes)
"""
:class:`~revscoring.languages.features.RegexMatches` features via a list of
badword detecting regexes.
"""

informal_regexes = [
    r"elo",
    r"fajna",
    r"fajne",
    r"fajnie",
    r"fajny",
    r"glupi",
    r"glupia",
    r"glupie",
    r"haha",
    r"hahah",
    r"hahaha",
    r"hahahaha",
    r"hahahahaha",
    r"heh",
    r"hehe",
    r"hehehe",
    r"hej",
    r"hihi",
    r"pozdro",
    r"siema",
    r"siemka",
    r"spoko"
]

informals = RegexMatches(name + ".informals", informal_regexes)
"""
:class:`~revscoring.languages.features.RegexMatches` features via a list of
informal word detecting regexes.
"""