import Bezier
import matplotlib.pyplot as plt
import time

control_points = []
mid_points = []
curve_points = []
iter=0

def main():
    global control_points,mid_points,curve_points,iter
    print("Selamat datang di program Bezier curve!")
    print("1. Kurva Bezier 3 titik")
    print("2. Kurva Bezier n titik")
    mode = int(input("Pilihan: "))
    if(mode==1):
        for i in range(3):
            point = tuple(map(float, input(f"Masukkan titik {i+1}: ").split(" ")))
            control_points.append(point)
    else:
        n = int(input("Masukkan jumlah control points: "))
        for i in range(n):
            point = tuple(map(float, input(f"Masukkan titik {i+1}: ").split(" ")))
            control_points.append(point)
    iter = int(input("Masukkan jumlah iterasi: "))

    if(mode==1):
        fig, ax = plt.subplots(1,2)
        start1 = time.time()
        Bezier.BezierN(control_points, iter, mid_points, curve_points)
        end1 = time.time()
        duration1 = end1-start1
        print(f'Divide and Conquer: {duration1}')
        mid_points=[]
        curve_points=[]
        start2 = time.time()
        Bezier.BF(control_points, iter, curve_points, mid_points)
        end2 = time.time()
        duration2 = end2-start2
        print(f'Bruteforce: {duration2}')
        if(duration2>duration1):
            print("Algoritma Divide and Conquer Lebih cepat!")
        elif(duration1>duration2):
            print("Algoritma Bruteforce Lebih cepat!")
        else:
            print("Waktu eksekusi sama!")
        print(f'Selisih waktu eksekusi: {abs(duration2-duration1)}')



        for i in range(1,iter+1):
            mid_points=[]
            curve_points=[]
            Bezier.Bezier(control_points, i, curve_points, mid_points)
            Bezier.show(control_points,i, ax[0], curve_points)
            ax[0].set_title('Divide and Conquer')

            mid_points=[]
            curve_points=[]
            Bezier.BF(control_points, i, curve_points, mid_points)
            Bezier.show(control_points,i, ax[1], curve_points)
            ax[1].set_title('Bruteforce')
            plt.pause(1)
    else:
        fig, ax = plt.subplots(1)
        for i in range(1,iter+1):
            mid_points=[]
            curve_points=[]
            Bezier.BezierN(control_points, i, mid_points, curve_points)
            Bezier.show(control_points,i, ax, curve_points)
            ax.set_title('Divide and Conquer')
            plt.pause(1)
    plt.show()
    

if __name__ == '__main__':
    main()