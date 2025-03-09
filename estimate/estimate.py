import numpy as np
import csv
class Estimate:
    def __init__(self):
        self.__param_y = 10
        self.__param_x = 0
        self.__lidar2robot_rotation = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.__lidar2robot_vector = np.array([0, 0, 0])
        self.__motor_rotation= np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.load_lidar2robot_rotation()
    
    @property
    def param_y(self):
        return self.__param_y
    
    @property
    def param_x(self):
        return self.__param_x
    
    @property
    def lidar2robot_rotation(self):
        return self.__lidar2robot_rotation
    
    @property
    def lidar2robot_vector(self):
        return self.__lidar2robot_vector
    
    @property
    def motor_rotation(self):
        return self.__motor_rotation
    
    
    def load_lidar2robot_rotation(self):
        with open('./estimate/vector/rVec.csv', 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        self.__lidar2robot_rotation = np.array(data, dtype=float)

    def solve_motor_rotation(self):

        pass
        
        
    
if __name__ == '__main__':
    est = Estimate()
    print("aa")
    print(est.lidar2robot_rotation)
    
    


  
    
