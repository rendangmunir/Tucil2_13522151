import Bezier
import matplotlib.pyplot as plt
from keyboard import *



def main():
    print("Selamat datang di program Bezier curve!")
    print("1. Kurva Bezier 3 titik")
    print("2. Kurva Bezier n titik")
    control_points = []
    mid_points = []
    curve_points = []

    mode = int(input("Pilihan: "))
    if(mode==1):
        for i in range(3):
            point = input(f"Masukkan titik {i+1}: ")
            point = point.split()
            x = float(point[0])
            y = float(point[1])
            control_points.append((x,y))
    else:
        n = int(input("Masukkan jumlah control points: "))
        for i in range(n):
            x = float(input(f"Masukkan x{i+1}: "))
            y = float((input(f"Masukkan y{i+1}: ")))
            control_points.append((x,y))
    print(control_points)
    iter = int(input("Masukkan jumlah iterasi: "))

    DNC = []
    BF = []
    fig, ax = plt.subplots(1,2)
    for i in range(1,iter+1):
        mid_points=[]
        curve_points=[]
        Bezier.BezierN(control_points, i, mid_points, curve_points)
        DNC.append(curve_points)
        Bezier.show(control_points,i, ax[0], curve_points)
        ax[0].set_title('Divide and Conquer')
        print("----------------------curve point DNC--------------------------")
        print(curve_points)

        mid_points=[]
        curve_points=[]
        Bezier.Bezier(control_points, i, curve_points, mid_points)
        BF.append(curve_points)
        print("----------------------curve point BF----------------------------")
        print(curve_points)
        Bezier.show(control_points,i, ax[1], curve_points)
        ax[1].set_title('Bruteforce')
        plt.pause(1)
    print(DNC)
    print("Press J or K to move between iterations!")
    print("Press q to quit")
    while True:
        # clear()
        key = get_key()
        n = iter-1
        if key == 'j':
            n = max(1, n-1)
        elif key == 'k':
            n = min(iter-1, n+1)
        elif key == 'q':
            break
        else:
            print("Invalid key")

        Bezier.show(control_points, n, ax[0], DNC[n])
        Bezier.show(control_points, n, ax[1], DNC[n])
    plt.show()
    





if __name__ == '__main__':
    main()