class Element_properties:
    def __init__(self,name,symbol,at_weight,elect_config,metalic_prop):
        self.name = name
        self.symbol = symbol
        self.at_weight = at_weight
        self.elect_config = elect_config
        self.meatlic_prop = metalic_prop
    def show_details(self):
        print("Name = ",self.name)
        print("Symbol = ",self.symbol)
        print("Atomic weight = ",self.at_weight)
        print("electronic configuration = ",self.elect_config)
        print("Metalic properties = ",self.meatlic_prop)
ep1 = Element_properties('hydrogen','H',1.00784,'1s1','Gas_Non-metal')
ep2 = Element_properties('helium','He',4.002602,'1s2','inert, monatomic gas')
ep3 = Element_properties('lithium','Li',6.941,' [He] 2s1','soft, silvery-white alkali metal')
ep4 = Element_properties('Beryllium','Be',9.0121831,'[He] 2s²','It is a steel-gray, strong, lightweight and brittle alkaline earth metal')
ep5 = Element_properties('Boron','B',10.811,'[He] 2s22p1','it is a brittle, dark, lustrous metalloid')
ep6 = Element_properties('Carbon','C',12.0107,'[He] 2s22p2','nonmetallic and tetravalent')
ep7 = Element_properties('Nitrogen','N',14.0067,' [He] 2s22p3','it is a gas')
ep8 = Element_properties('Oxygen','O',15.999,'[He] 2s²2p⁴',' a highly reactive nonmetal')
ep9 = Element_properties('Fluorine','F',18.998403,' [He] 2s22p5','most electronegative element')
ep10 = Element_properties('Neon','Ne',20.1797,'[He] 2s²2p⁶','a noble gas')
while(True):
    print("\n**************{{ Welcome To The Modern Periodic Table }}****************")
    n = int(input("Enter the automic number "))
    if n==1:
        ep1.show_details()
        print("\n")
    elif n==2:
        ep2.show_details()
        print("\n")
    elif n==3:
        ep3.show_details()
        print("\n")
    elif n==4:
        ep4.show_details()
        print("\n")
    elif n==5:
        ep5.show_details()
        print('\n')
    elif n==6:
        ep6.show_details()
        print('\n')
    elif n==7:
        ep7.show_details()
        print('\n')
    elif n==8:
        ep8.show_details()
        print('\n')
    elif n==9:
        ep9.show_details()
        print('\n')
    elif n==10:
        ep10.show_details()
        print('\n')


    else:
        print("Enter the Aoutomic number upto 10 only because this application contain only 10 elements details.")

exit()