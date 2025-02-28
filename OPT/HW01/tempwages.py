import numpy as np

def fit_wages(t, M):
    A = np.vstack([np.ones(len(t)), t]).T
    x = np.linalg.lstsq(A, M, rcond = None)[0]
    return x

def quarter2_2009(x):
    return x[0] + x[1] * (2009.25)
 

def fit_temps(t, T, omega):
    matrix = np.column_stack((np.ones_like(t), t, np.sin(omega*t), np.cos(omega*t)))
    x = np.linalg.lstsq(matrix, T, rcond=None)[0]
    return x

if __name__ == "__main__":
    wages_data = {
    2000.00: 11941,
    2000.25: 13227,
    2000.50: 12963,
    2000.75: 14717,
    2001.00: 13052,
    2001.25: 14391,
    2001.50: 14117,
    2001.75: 15908,
    2002.00: 14083,
    2002.25: 15599,
    2002.50: 15268,
    2002.75: 17133,
    2003.00: 14986,
    2003.25: 16529,
    2003.50: 16088,
    2003.75: 18096,
    2004.00: 16231,
    2004.25: 17223,
    2004.50: 17190,
    2004.75: 19183,
    2005.00: 17067,
    2005.25: 18112,
    2005.50: 18203,
    2005.75: 19963,
    2006.00: 18270,
    2006.25: 19300,
    2006.50: 19305,
    2006.75: 21269,
    2007.00: 19687,
    2007.25: 20740,
    2007.50: 20721,
    2007.75: 22641,
    2008.00: 21647,
    2008.25: 22370,
    2008.50: 22282,
    2008.75: 24484
}

    t1 = np.array(list(wages_data.keys()))
    M = np.array(list(wages_data.values()))
    
    x = fit_wages(t1, M)
    print("Mzda:", "x:", x)
    
    es = quarter2_2009(x)
    print("Mzda:", "M:", es)
    
    temperature_data = {
    14: -1.00, 
    46: -4.75, 
    74: 0.25, 
    105: 12.25, 
    135: 12.75, 
    166: 18.50, 
    196: 21.00, 
    227: 15.00, 
    258: 15.75,
    288: 7.00, 
    319: 1.25, 
    349: 0.75, 
    369: -6.40, 
    401: -3.10, 
    429: -1.65, 
    460: 7.65, 
    490: 13.08, 
    521: 19.35,
    551: 17.93, 
    582: 14.38, 
    613: 17.73, 
    643: 8.18, 
    674: 6.98, 
    704: -0.63, 
    724: -1.40,
    756: 2.48, 
    784: 3.58,
    815: 13.80,
    845: 12.55, 
    876: 23.23, 
    906: 22.38, 
    937: 20.35, 
    968: 10.33, 
    998: 4.63, 
    1029: -1.63, 
    1059: -1.88
}
    t2 = np.array(list(temperature_data.keys()))
    T = np.array(list(temperature_data.values()))
    omega = 2 * np.pi / 365
    
    params = fit_temps(t2, T, omega)
    print("Teplota:", "x:", params)
