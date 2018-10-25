import sys
gaga=sys.argv[1]
gaga=float(gaga)

if gaga>=220.0:
    print("Super Typhoon")
elif gaga>=118.0:
    print("Typhoon")
elif gaga>=89.0:
    print("Severe Tropical Storm")
elif gaga>=62.0:
    print("Tropical Storm")
elif gaga<=61.0:
    print("Tropical Depression")