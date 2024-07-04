def main():
    def TVA(tva_pourcentage):
        tva = (tva_pourcentage / 100) + 1
        def HT_to_TVA(prix):
            return prix * tva
        return HT_to_TVA

    HT_to_TVA_20 = TVA(20)
    HT_to_TVA_40 = TVA(40)
    print(HT_to_TVA_20(5))
    print(HT_to_TVA_20(10))
    print(HT_to_TVA_20(100))
    print(HT_to_TVA_40(5))
    print(HT_to_TVA_40(10))
    print(HT_to_TVA_40(100))

if __name__ == "__main__":
    main()