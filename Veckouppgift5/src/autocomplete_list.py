# Söka efter användare

# Tänk dig en funktion som kan användas för att visa sökresultat medan användaren skriver i ett sökfält. Funktionen ska ta två parametrar: input är det användaren skriver, master_list är en lista med alternativ som kan hittas.
# def autocomplete_list(input, master_list):
#
# Börja med att formulera de krav och acceptanskriterier (AK) som ska gälla för funktionen.
# Välj sedan ut ett AK och skriv ett testfall. (red)
# Skriv sedan kod som uppfyller testfallet. (green)
# Städa i koden, så du känner dig nöjd med din kod hittills. Fortsätt sedan med nästa AK.

def autocomplete_list(input, master_list):
    # Sanity check
    if not isinstance(input, str):
        return TypeError
    if len(input) == 0 or input == "" or len(master_list) == 0:
        return []

    # si == sanitised_input
    si = str(input).lower()
    # sml == sanitised_master_list
    sml = []
    for mli in master_list:
        sml.append(str(mli).lower())

    returnlist = []
    for i in sml:
        if i.startswith(si):
            returnlist.append(i.capitalize())

    return returnlist