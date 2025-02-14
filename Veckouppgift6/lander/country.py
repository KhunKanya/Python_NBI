
class Country:
    def __init__(self, name, population, area):
        self._name = name
        self._population = population
        self._area = area
        self._languages = []

    def print_info(self):
        area_info = f"Area: {self._area} km²" if self._area else "Area: Not specified"
        print(f"I {self._name} bor det {self._population} miljoner invånare.")
        if self._area is not None:
            print(area_info)
        if self._languages:
            print("Officiella språk:")
            for language in self._languages:
                print(f"- {language}")

    def add_language(self, language):
        if language not in self._languages:
            self._languages.append(language)


# Skapa objekt för länderna
se = Country("Sverige", 10.5, None)
no = Country("Norge", 5.5, None)

# Skapa objekt för Island och Danmark med befolkningsdata från januari 2024
island = Country("Island", 0.383726, None)
island.add_language("Icelandic")
island.print_info()

print()

denmark = Country("Danmark", 5.961249, 43094)
denmark.add_language("Danish")
denmark.print_info()

print()

# Skapa ett land med flera officiella språk
switzerland = Country("Schweiz", 8.632703, 41285)
switzerland.add_language("German")
switzerland.add_language("French")
switzerland.add_language("Italian")
switzerland.add_language("Romansh")
switzerland.print_info()