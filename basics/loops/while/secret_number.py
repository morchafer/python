numeroSecreto = 777

print(
    """
        ++       +++++   +++++++ +       + +++++++ ++      +       ++
       ++++      +    +     +    +       +    +    + +     +      +  +
      +    +     +     +    +    +       +    +    +  +    +     +    +
     +      +    +     +    +     +     +     +    +   +   +    +      +
    ++++++++++   +     +    +      +   +      +    +    +  +   ++++++++++
   +          +  +    +     +       + +       +    +     + +  +          +
  +            + +++++   +++++++     +     +++++++ +      ++ +            +

  # # # # # # # # #   E L   N Ú M E R O   S E C R E T O   # # # # # # # # #
  
""")

numeroIngresado = int(input("\n\tIngresa un número: "))

while numeroIngresado != numeroSecreto:
    print("\n¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    numeroIngresado = int(input("\n\tIngresa un número nuevamente: "))
print("\n¡Maldita sea! Has encontrado el número secreto: ", numeroSecreto)
print("¡Bien hecho, muggle! Eres libre ahora")
