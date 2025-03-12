import numpy as np
import csv
import cv2 as cv
from scipy.optimize import fsolve
class Estimate:
    def __init__(self):
        self.__param_y = 10
        self.__param_z = 0
        self.__tVec, self.__rVec = self.load_vector()
        self.__lidar2robot_rotation = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        cv.Rodrigues(self.__rVec, self.__lidar2robot_rotation)

        self.__lidar2robot_vector = np.array([0, 0, 0])
        self.__motor_rotation= np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.load_lidar2robot_rotation()
    
    @property
    def param_y(self):
        return self.__param_y
    
    @property
    def param_z(self):
        return self.__param_z
    
    @property
    def lidar2robot_rotation(self):
        return self.__lidar2robot_rotation
    
    @property
    def lidar2robot_vector(self):
        return self.__lidar2robot_vector
    
    @property
    def motor_rotation(self):
        return self.__motor_rotation
    
    def load_vector(self):
        with open('./estimate/vector/rVec.csv', 'r') as file:
            reader = csv.reader(file)
            rVecData = list(reader)
        rVec = np.array(rVecData, dtype=float)

        with open('./estimate/vector/tVec.csv', 'r') as file:
            reader = csv.reader(file)
            tVecData = list(reader)
        tVec = np.array(tVecData, dtype=float)  
        return tVec, rVec   
        
    def rotation_matrix(self, theta):
        return np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])
    
    def equation(self,theta,a,b,c):
        return -a * np.sin(theta) + b * np.cos(theta) - c

    def solve_motor_rotation(self, coordWorld):
        #world ->robot frame
        coordRobot = self.__lidar2robot_rotation*coordWorld+self.__tVec
        initial_theta=0
        solution=fsolve(self.equation,initial_theta,args=(coordRobot[0],coordRobot[1],self.__param_y))
        return solution
 
    
if __name__ == '__main__':
    est = Estimate()
    print("aa")
    print(est.lidar2robot_rotation)
    
    


  
    
