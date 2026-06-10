# ==========================================
# 1. WUJEK (Niezależny ekspert od sprzętu)
# ==========================================
class SkanerBezpieczenstwa:
    def __init__(self, nazwa_strefy):
        self.strefa = nazwa_strefy
        self.czy_zablokowano = False  # Na początku zakładamy, że nikogo nie ma w strefie

    # To jest odpowiednik funkcji "publish()" z ROS 2
    def skanuj_obszar(self):
        if self.czy_zablokowano:
            print(f"[SKANER: {self.strefa}] ALARM! Wykryto obiekt! Zatrzymanie awaryjne.")
            return False  # Zwraca fałsz - nie można jechać
        else:
            print(f"[SKANER: {self.strefa}] Czysto. Obszar bezpieczny.")
            return True   # Zwraca prawdę - można jechać


# ==========================================
# 2. RODZIC (Fundament systemu z wbudowaną "fabryką")
# ==========================================
class GlownyKontroler:
    def __init__(self, nazwa_stanowiska):
        self.stanowisko = nazwa_stanowiska
        print(f"[{self.stanowisko}] Kontroler główny uruchomiony.")

    # To jest odpowiednik "create_publisher()" z ROS 2
    # Rodzic nie skanuje sam, tylko dzwoni do Wujka i produkuje narzędzie.
    def zainstaluj_skaner(self, strefa):
        print(f"[{self.stanowisko}] Zlecam budowę skanera dla strefy: {strefa}...")
        nowe_narzedzie = SkanerBezpieczenstwa(strefa) # Wzywamy Wujka!
        return nowe_narzedzie


# ==========================================
# 3. DZIECKO (Konkretny program robota)
# ==========================================
class RobotPaletyzujacy(GlownyKontroler):
    def __init__(self, nazwa_stanowiska):
        # A. Budzimy Rodzica (włączamy główny kontroler)
        super().__init__(nazwa_stanowiska)
        
        # B. Dziecko dzwoni do Rodzica i prosi o załatwienie sprzętu od Wujka.
        # Gotowy skaner chowamy do "kieszeni" (self.moj_skaner). 
        # To jest odpowiednik "self.pub = self.create_publisher(...)"
        self.moj_skaner = self.zainstaluj_skaner("Strefa Załadunku Palet")
        
        # C. Własne zmienne Dziecka
        self.licznik_palet = 0

    # To jest odpowiednik funkcji "tick()" z ROS 2
    def cykl_pracy(self):
        print("\n--- Start cyklu paletyzacji ---")
        
        # Dziecko używa sprzętu Wujka bezpośrednio z własnej kieszeni!
        # To jest odpowiednik "self.pub.publish()"
        czy_bezpiecznie = self.moj_skaner.skanuj_obszar()
        
        if czy_bezpiecznie:
            self.licznik_palet += 1
            print(f"[ROBOT] Paleta nr {self.licznik_palet} odstawiona poprawnie.")
        else:
            print("[ROBOT] Czekam na zresetowanie kurtyn bezpieczeństwa...")


# ==========================================
# TESTOWANIE W PRAKTYCE
# ==========================================
if __name__ == '__main__':
    # 1. Powołujemy nasze Dziecko do życia
    kuka_paletyzer = RobotPaletyzujacy("Cela_Paletyzacji_A")

    # 2. Wykonujemy pierwszy, prawidłowy cykl pracy
    kuka_paletyzer.cykl_pracy()

    # 3. Symulujemy, że ktoś nagle wszedł w pole skanera!
    # Wchodzimy do "kieszeni" robota i zmieniamy stan na narzędziu Wujka
    kuka_paletyzer.moj_skaner.czy_zablokowano = True

    # 4. Próbujemy wykonać kolejny cykl roboczy
    kuka_paletyzer.cykl_pracy()