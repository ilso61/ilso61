# git clone -b main --single-branch https://github.com/ilso61/ilso61.git
import math

class deBilError(Exception):
    "Нельзя такое считать!!!"
    pass

def volume(R):
    V = 4/3*math.pi*(R**3)
    if V <= 0:
        raise deBilError('Не бывает такого!')
    return V

def radius(S):
    R = math.sqrt(S/(4*math.pi))
    if R <= 0:
        raise deBilError('Не бывает такого!')
    return R

def mass_(V): # 0.9 г/см куб
    m = V*0.9
    if m <= 0:
        raise deBilError('Не бывает такого!')
    return m
    
peel_thickness = float(input('Введите толщину кожуры (в см)\n'))
if peel_thickness <= 0:
    raise deBilError('Не бывает такого!')
    
peel_square = float(input('Введите площадь кожуры (в кв. см)\n'))
if peel_square <= 0:
    raise deBilError('Не бывает такого!')
full_R = radius(peel_square)

pulp_R = full_R - peel_thickness

pulp_V = volume(pulp_R)

peel_V = volume(full_R) - volume(pulp_R)

#плотность
m_pulp = mass_(pulp_V)

print('Радиус неочищенного апельсина =', str(full_R), 'см')
print('Радиус очищенного апельсина =', str(pulp_R), 'см')
print('Объем очищенного апельсина =', str(pulp_V), 'куб. см')
print('Масса очищенного апельсина =', str(m_pulp), 'г')
print('Объем кожуры =', str(peel_V), 'куб. см')


