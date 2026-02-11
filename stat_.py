class ChaiUtils:

      @staticmethod
      def clean_ingredients(text):
            return [item.strip() for item in text.split(",")]

raw = " water , milk , ginger , honey "   #SPACING IS IMP IN STATIC MTHD

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)