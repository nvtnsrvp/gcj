import numpy as np

sqrt2 = math.sqrt(2)

def estimate_coo(A):
    mat = np.zeros((3,3))
    if A == 1:
        mat[0, 0] = 0.5
        mat[1, 1] = 0.5
        mat[2, 2] = 0.5
    elif A <= 2*sqrt2:
        theta_xy = np.arcsin(A/sqrt2) - np.pi/4
        mat[0, 0] = 0.5*sin(theta_xy)
        mat[1, 0] = 0.5*cos(theta_xy)
        mat[1, 0] = -0.5*sin(theta_xy)
        mat[1, 1] = 0.5*cos(theta_xy)
    else:
        theta_xy = np.arcsin(A/sqrt2) - np.pi/4
        theta_xyz = np.arcsin(A/3) - np.arctan(1/(2*sqrt2))
        mat[0, 0] = 0.5*sin(theta_xy)*cos(theta_xyz)
        mat[1, 0] = 0.5*cos(theta_xy)*cos(theta_xyz)
        mat[1, 0] = -0.5*sin(theta_xy)*cos(theta_xyz)
        mat[1, 1] = 0.5*cos(theta_xy)*cos(theta_xyz)
    return mat

t = int(raw_input().strip())
for case in range(1, t+1):
    A = float(raw_input().strip())
    print "Case #" + str(case)
    print estimate_coo(A)
