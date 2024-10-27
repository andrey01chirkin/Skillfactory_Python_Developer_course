
class SoundEquipment:
    def switch_on(self):
        self.state = True

    def switch_off(self):
        self.state = False

class Microphone(SoundEquipment):
    def __init__(self, volume, state):
        self.volume = volume
        self.state = state

    def adjust_volume(self, amount):
        self.volume = amount
        print(f"Volume is now {self.volume}")

class Speaker(SoundEquipment):
    def __init__(self, bass, state):
        self.bass = bass
        self.state = state

    def adjust_bass(self, amount):
        self.bass = amount
        print(f"Bass level is now {self.bass}")


# Создаём объект микрофон с громкостью 5 состоянием "включен"
mic = Microphone(volume=5, state=True)
# Отключаем микрофон
mic.switch_off()
# Устаналиваем новый уровень громкости
mic.adjust_volume(7)

# Volume is now 7


# Создаём объект динамик с уровнем бассов 7 и состоянием "выключен"
sp = Speaker(7, False)
# Включили динамик
sp.switch_on()
# Устаналиваем новый уровень бассов
sp.adjust_bass(8)

# Bass level is now 8








