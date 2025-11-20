#### Fonction secondaire
""" 
Module contenant une fonction qui teste si la chaîne de caractères à tester 
est un palindrome.
"""

def ispalindrome(p):
    """
    Retourne la vérité de la proposition : "p est un palindrome".

    Args:
        p: la chaîne de caractères à tester pour savoir si elle est un palindrome.
    
    Returns:
        True: si p est un palindrome.
        False: si p n'est pas un palindrome.
    """
    tab = {
    ord("é"): "e", ord("è"): "e", ord("ê"): "e", ord("ë"): "e",
    ord("à"): "a", ord("ä"): "a",
    ord("ç"): "c",
    ord("ö"): "o", ord("ô"): "o",
    ord(" "): "", ord("?"): "", ord("!"): "", ord(","): "", ord("-"): "", ord(":"): "", ord("'"): ""
    }
    p = p.lower()
    p = p.translate(tab)
    print(p)
    mid = len(p)//2
    length = len(p) - 1
    for i in range(mid):
        if p[i] != p[length - i]:
            return False
    return True

#### Fonction principale


def main():
    """ appel de la fonction ispalindrome(p) sur divers exemples """
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
