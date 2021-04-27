


class Dea:
    def __init__(self, x, y, dea_id):
        self.x = float(x)
        self.y = float(y)
        self.dea_id = dea_id
    
    def get_distance(self, user_x, user_y):
        c_1 = (user_x - self.x)**2
        c_2 = (user_y - self.y)**2
        return (c_1+c_2)**0.5

class User:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_nearest_dea(self, given_list):
        H = 100000000000
        # print(H)
        result = None
        for dea in given_list:
            dea_object = Dea(dea["direccion_coordenada_x"], dea["direccion_coordenada_y"], dea["codigo_dea"])
            if dea_object.get_distance(self.x, self.y) <= H:
                result = dea
                H = dea_object.get_distance(self.x, self.y)
        return result