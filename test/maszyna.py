class Alarms:
    def __init__(self, name_of_alarms, time_of_alarms):
        self.name_of_alarms = name_of_alarms
        self.time_of_alarms = time_of_alarms

    def Alarm_ON(self):
        print(f"Alarm wlaczony = , {self.name_of_alarms}, ,{self.time_of_alarms}")

    def Alarm_OFF(self):
        print(f"Alarm OFF, {self.name_of_alarms}, {self.time_of_alarms}")


class Industry_devices:
    def __init__(self, nazwa, uniq_id, type_dev):
        self.nazwa = nazwa
        self.uniq_id = uniq_id
        self.zasilanie_wlaczone = False
        self.register = [0, 0, 0, 0, 0]

        # 1. Sposób bezpośredni: Tworzymy obiekt Alarms od razu na miejscu
        self.system_alarmowy_wrong = Alarms(nazwa, 10)

        # 2. Sposób ROS 2 (Metoda-Fabryka): Zlecamy stworzenie alarmu wewnętrznej funkcji
        self.system_alarmowy = self.stworz_alarm(f"Alarm_{nazwa}", "12:00")

        # Sekcja walidacji typu urządzenia
        baza_typow = {'1': "KUKA", '2': "FANUC", '3': "ABB"}
        if type_dev in baza_typow:
            self.type_dev = baza_typow[type_dev]
        else:
            raise ValueError("Niepoprawny typ!")

    # To jest nasza metoda-fabryka (odpowiednik create_publisher() z ROS 2)
    def stworz_alarm(self, nazwa_alarmu, czas):
        print(f"[{self.nazwa}] Uruchamiam wewnętrzną fabrykę i tworzę alarm...")
        nowy_obiekt_alarmu = Alarms(nazwa_alarmu, czas)
        return nowy_obiekt_alarmu

    def primery_data(self):
        print(self.nazwa, self.uniq_id, self.register, self.type_dev)


class Drons(Industry_devices):
    def __init__(self, nazwa, uniq_id, type_dev, range, load):
        # Teleport danych do klasy nadrzędnej (Rodzica)
        super().__init__(nazwa, uniq_id, type_dev)
        # Własne zmienne Dziecka
        self.range = range
        self.load = load


# ==========================================
# TEST URUCHOMIENIA PROGRAMU
# ==========================================
if __name__ == '__main__':
    # Tworzymy obiekt Drona. Pamiętaj, że typ '1' podajemy w cudzysłowie jako tekst (string)!
    fly_bee = Drons("Hornet", 155, '1', 10, 12)
    
    print("\n==========================================")
    print("      URUCHAMIAMY ALARMY DRONA")
    print("==========================================\n")

    # Wywołanie alarmu stworzonego bezpośrednio (linia 17 u rodzica)
    print("--- Wywołanie system_alarmowy_wrong ---")
    fly_bee.system_alarmowy_wrong.Alarm_ON()

    print()  # Odstęp dla czytelności w konsoli

    # Wywołanie alarmu stworzonego przez fabrykę (linia 20 u rodzica)
    print("--- Wywołanie system_alarmowy (Fabryka ROS 2 style) ---")
    fly_bee.system_alarmowy.Alarm_ON()