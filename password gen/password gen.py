import random # voor random keuzes van de tekens die er in komen 
import string # voor meer opties dan die er standaard zijn

def generate_password(length: int ): # functie om een wachtwoord te genereren
    alphabet =string.ascii_letters + string.digits + string.punctuation # alle mogelijke tekens die er in kunnen komen
    password = ''.join( random.choice(alphabet) for i in range(length)) # maakt een wachtwoord met de lengte die de gebruiker opgeeft
    return password # geeft het wachtwoord terug

length = int(input("hoe lang wil je het wachtwoord hebben? : ")) # vraag de gebruiker om de lengte van het wachtwoord

if length <= 8: # controleer of de lengte minder dan of gelijk is aan 8
    print("waarschuwing: een wachtwoord van minder dan 8 tekens in minder veilig .")

else: 
    print("je wachtwoord is veilig genoeg .")



print(generate_password(length)) # print wachtwoord in de terminal 