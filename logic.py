from random import randint
import requests
from datetime import datetime,timedelta
class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer   
        #-----------------------------------
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        #-----------------------------------
        self.hp = randint(200,500)
        self.damage = randint(20,80)
        self.last_feed_time = datetime.now()
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}/'
        res = requests.get(url)
        
        if res.status_code == 200:
            data = res.json()    
            return data['sprites']['other']['official-artwork']['front_default']
        else:
            return 'https://avatars.mds.yandex.net/get-entity_search/2057673/954086035/SUx182_2x'
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}\nЗдоровья твоего покимона:{self.hp}\nУрон твоего покимона{self.damage}"
        
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

    def attack(self,enemy):
        if enemy.hp <= 0:
            return f'у покина @{enemy.pokemon_trainer}'
        if isinstance(enemy,Wizard):
            x = randint(1,2)
            if x == 1:
                enemy.hp -= self.damage //2
                if enemy.hp <= 0:
                    enemy.hp = 0
                return f'покемон @{self.pokemon_trainer} нанес урон @{enemy.pokemon_trainer} , но волшебник поставил щит{enemy.hp}'
        enemy.hp -= self.damage
        if enemy.hp <= 0:
            enemy.hp = 0
        return f'покемон @{self.pokemon_trainer} нанес урон @{enemy.pokemon_trainer}, у покимона {enemy.hp}Хп'
    
    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {self.last_feed_time+delta_time}"  


class Wizard(Pokemon):
    def feed(self, feed_interval=20, hp_increase=23):
        return super().feed(feed_interval, hp_increase)
    

class Fighter(Pokemon):
    def attack(self, enemy):
        x = randint(1,2)
        if x == 1:
            self.damage *= 2
        res = super().attack(enemy)
        if x == 1:
            self.damage = self.damage //2
        return res + 'боец умножил свой уорн на два раза больше'
    
    def feed(self, feed_interval=12, hp_increase=11):
        return super().feed(feed_interval, hp_increase)