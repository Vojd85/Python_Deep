# Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа. 
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


from Sem_Task5_6 import Fish, Birds

class Fabrique:
    def __init__(self, animal_class, *args, **kwargs):
        self.animal = animal_class(*args, **kwargs)
        
    
    def new_animal(self):
        return self.animal
    

if __name__ == '__main__':
    new_fish = Fabrique(Fish, 'yes', 4, 'Окунь', 'Плавник').new_animal()
    print(type(new_fish))
    print(f'{new_fish.name} Пресноводная: {new_fish.specific()}, Глубоководность: {new_fish.check_deep()}')
    new_bird = Fabrique(Birds, 4, 'Аист', 'Перьевой').new_animal()
    print(type(new_bird))
    print(f'{new_bird.name} Длина крыла: {new_bird.specific()}')
    
    