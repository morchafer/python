class PizzaError(Exception):
    def __init__(self, pizza='desconocida.', mensaje='Estado de la pizza:'):
        Exception.__init__(self, mensaje)
        self.pizza = pizza


class DemasiadoQuesoError(PizzaError):
    def __init__(self, pizza='desconocida', queso='>100.', mensaje='Cantidad de queso excedida:'):
        PizzaError.__init__(self, pizza, mensaje)
        self.queso = queso


def hacerPizza(pizza, queso):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError
    if queso > 100:
        raise DemasiadoQuesoError
    print("¡Pizza lista!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        hacerPizza(pz, ch)
    except DemasiadoQuesoError as tmce:
        print(tmce, tmce.queso)
    except PizzaError as pe:
        print(pe, pe.pizza)
