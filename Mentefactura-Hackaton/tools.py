import re 
from googletrans import Translator, LANGUAGES

def extra_clean(reviews: str) -> str:
    reviews = str(reviews).lower()
    reviews.replace(",", " ")
    reviews.replace("'", "")
    reviews = re.sub(r"[á']", r"a", reviews)
    reviews = re.sub(r"[é']", r"e", reviews)
    reviews = re.sub(r"[í']", r"i", reviews)
    reviews = re.sub(r"[ó']", r"o", reviews)
    reviews = re.sub(r"[ú']", r"u", reviews)
    # remove special characters and digits from the string
    pattern = r"[^a-zA-Zñ\s]"
    cleaned = " ".join(re.sub(pattern, " ", str(reviews)).split())
    return cleaned


def traducir(texto, lang_dest='en'):
    translator = Translator()
    try:
        # Intenta traducir el texto al idioma deseado
        traduccion = translator.translate(texto, dest=lang_dest)
        return traduccion.text
    except Exception as e:
        # Maneja cualquier error que pueda ocurrir
        return f"Error al traducir: {str(e)}"

def translateTxtArray(txtArr, lang_dest = 'en'):
  newArr = []
  for t in txtArr:
    new_t = traducir(t, lang_dest)
    newArr.append(new_t)

  return newArr










