import numpy as np

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

def BF(control_points,iter,curve_points, mid_points):
    control_points = np.array(control_points)
    total = 2**iter + 1
    t = np.linspace(0,1,total)
    for i in range(total):
        p = (1 - t[i])**2 * control_points[0] + 2 * \
            (1 - t[i]) * t[i] * control_points[1] + t[i]**2 * control_points[2]
        curve_points.append(p)


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
    ax.plot(x_curve, y_curve, label="Bezier Curve", color="blue")
    ax.scatter(x_curve, y_curve, color="blue")
    ax.plot(x_control, y_control, label="control Points", color="red")
    ax.scatter(x_control, y_control, color="red", label="Control Points")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    ax.legend()