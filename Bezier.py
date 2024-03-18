import matplotlib.pyplot as plt
import time



def Bezier(control_points,iter,curve_points, mid_points):
    if (iter==0):
        if (curve_points==[]):
            curve_points=control_points.copy()
        else:
            curve_points.append(control_points[-1])
    else:
        if (curve_points==[]):
            curve_points.append(control_points[0])
        r0 = (0.5*(control_points[0][0]+control_points[1][0]), 0.5*(control_points[0][1]+control_points[1][1]))
        r1 = (0.5*(control_points[1][0]+control_points[2][0]), 0.5*(control_points[1][1]+control_points[2][1]))
        r2 = (0.5*(r0[0]+r1[0]), 0.5*(r0[1]+r1[1]))
        mid_points.append(r0)
        mid_points.append(r1)
        mid_points.append(r2)
        Bezier([control_points[0],r0,r2], iter-1,curve_points, mid_points)
        Bezier([r2,r1,control_points[-1]], iter-1,curve_points, mid_points)





def Bezier2(control_points,iter,curve_points, mid_points):
    if(iter==0):
        print(control_points)
        curve_points=control_points
        print("okasoka")
        print(curve_points)
    else:
        for i in range(len(control_points)-1):
            r = (0.5*(control_points[i][0]+control_points[i+1][0]), 0.5*(control_points[i][1]+control_points[i+1][1]))
            mid_points.append(r)
        Bezier2(mid_points, iter-1, curve_points, [])

def BezierN(control_points, iter,mid_points, curve_points):
    if(iter>0):
        n = len(control_points)-1
        left = control_points.copy()
        left = left[::-1]
        right = control_points.copy()
        curve_points.append(control_points[0])
        while(n>0):
            for i in range(n):
                right[i] = (0.5*(right[i][0]+right[i+1][0]), 0.5*(right[i][1]+right[i+1][1]))
                left[i] = (0.5*(left[i][0]+left[i+1][0]), 0.5*(left[i][1]+left[i+1][1]))
                mid_points.append(right[i])
            if(n==1):
                BezierLeft(left, iter-1, mid_points,curve_points)
                curve_points.append(right[0])
                BezierRight(right, iter-1, mid_points,curve_points)
                curve_points.append(control_points[-1])
            n-=1

def BezierLeft(control_points, iter,mid_points, curve_points):
    if(iter>0):
        n = len(control_points)-1
        left = control_points.copy()
        right = control_points.copy()
        right = right[::-1]
        while(n>0):
            for i in range(n):
                right[i] = (0.5*(right[i][0]+right[i+1][0]), 0.5*(right[i][1]+right[i+1][1]))
                left[i] = (0.5*(left[i][0]+left[i+1][0]), 0.5*(left[i][1]+left[i+1][1]))
                mid_points.append(right[i])
            if(n==1):
                BezierLeft(left, iter-1, mid_points,curve_points)
                curve_points.append(left[0])
                BezierRight(right, iter-1, mid_points,curve_points)
            n-=1
    
def BezierRight(control_points, iter,mid_points, curve_points):
    if(iter>0):
        n = len(control_points)-1
        left = control_points.copy()
        left = left[::-1]
        right = control_points.copy()
        while(n>0):
            for i in range(n):
                right[i] = (0.5*(right[i][0]+right[i+1][0]), 0.5*(right[i][1]+right[i+1][1]))
                left[i] = (0.5*(left[i][0]+left[i+1][0]), 0.5*(left[i][1]+left[i+1][1]))
                mid_points.append(right[i])
            if(n==1):
                BezierLeft(left, iter-1, mid_points,curve_points)
                curve_points.append(right[0])
                BezierRight(right, iter-1, mid_points,curve_points)
            n-=1

    
def show(control_points,iter, ax, curve_points):
    ax.clear()
    x_control, y_control = zip(*control_points)
    x_curve, y_curve = zip(*curve_points)
    # x_mid, y_mid = zip(*mid_points)
    # ax.f(figsize=(6, 4))
    ax.plot(x_curve, y_curve, label="Bezier Curve", color="blue")
    ax.scatter(x_curve, y_curve, color="blue")
    ax.plot(x_control, y_control, label="control Points", color="red")
    ax.scatter(x_control, y_control, color="red", label="Control Points")
    # ax.scatter(x_mid, y_mid, color="green", label="mid points")
    # ax.set_title(f'iterasi - {iter}')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    # ax.legend()
# control_points = [(0,0), (4,4), (8,0), (12,4)]
# curve_points = []
# mid_points = []
# start_time = time.time()
# BezierN(control_points,10, mid_points, curve_points)
# # curve_points.append(control_points[-1])
# # Bezier(control_points, 10, curve_points, mid_points)
# # Bezier2(control_points, 2, curve_points, mid_points)
# # mid_points = sorted(mid_points, key=lambda x: x[0])
# end_time = time.time()
# duration = end_time-start_time


# print(f"control points: {control_points}")
# print(f'curve : {curve_points}')
# print(mid_points)
# print(duration)

# # Add labels and title
# x_control, y_control = zip(*control_points)
# x_curve, y_curve = zip(*curve_points)
# x_mid, y_mid = zip(*mid_points)

# plt.figure(figsize=(6, 4))
# plt.plot(x_curve, y_curve, label="Bezier Curve", color="blue")
# plt.plot(x_control, y_control, label="control Points", color="red")
# plt.scatter(x_control, y_control, color="red", label="Control Points")
# # plt.scatter(x_mid, y_mid, color="green", label="mid points")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.legend()
# plt.grid(True)
# plt.show()

# Show the plot


