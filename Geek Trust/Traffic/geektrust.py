class Weather:
    def __init__(self,weather):
        self.weather = weather
    
        if self.weather == 'SUNNY':
            self.craters_rate = -10
            self.available_vehicles = ['CAR','BIKE','TUKTUK']
        
        elif self.weather == 'RAINY':
            self.craters_rate = 20
            self.available_vehicles = ['CAR','TUKTUK']
        
        elif self.weather == 'WINDY':
            self.craters_rate = 0
            self.available_vehicles = ['CAR','BIKE']
        else:
            print("Please check your weather input")
        

class Orbit(Weather):
    
    def __init__(self,orbit,traffic_speed,weather):
        
        self.traffic_speed = traffic_speed
        self.orbit = orbit
        if self.orbit == 'ORBIT1':
            
            self.distance = 18
            self.no_of_craters = 20
        
        elif self.orbit == 'ORBIT2':
            
            self.distance = 20
            self.no_of_craters = 10
            
        super().__init__(weather)
        
    def get_time(self):
        result_dic = {}
        
        for i in self.available_vehicles:
            vehicle_object = Vehicle(i)
            orbit=self.orbit
            if vehicle_object.speed >= self.traffic_speed:
                result_dic[i] = self.distance/self.traffic_speed + (self.no_of_craters*(100+self.craters_rate)*vehicle_object.crater_time)/100
            else:
                result_dic[i] = self.distance/vehicle_object.speed + (self.no_of_craters*(100+self.craters_rate)*vehicle_object.crater_time)/100
            
        return(result_dic)
        
class Vehicle(Orbit):
     def __init__(self, vehicle):
        
        if vehicle == 'CAR':
            self.speed = 20
            self.crater_time = 3/60
            
            
        elif vehicle == 'BIKE':
            self.speed = 10
            self.crater_time = 2/60
            
        
        elif vehicle == 'TUKTUK':
            self.speed = 12
            self.crater_time = 1/60
            


class traffic_speed_error(Exception):
    pass

class weather_input_error(Exception):
    pass

import sys   
def main(Exception):

    with open(" ".join(sys.argv[1:]), 'r') as f:
        lines=f.readlines()
        
    try:
        if len(lines)>1:
            raise TypeError
        else:
            lines= "".join(lines)
            input_list = lines.split()

            weather_input = input_list[0]
            traffic_speed_orbit1 = int(input_list[1])
            traffic_speed_orbit2 = int(input_list[2])
            
            if traffic_speed_orbit1 < 0 or traffic_speed_orbit2 < 0 :
                raise traffic_speed_error
            
            if weather_input.upper() not in ['SUNNY','RAINY','WINDY']:
                raise weather_input_error
            
            orbit_trafficspeed_dic = {'ORBIT1':traffic_speed_orbit1,'ORBIT2':traffic_speed_orbit2}
            
            
            min_time={}
            for i in orbit_trafficspeed_dic.keys():
                orb1=Orbit(i,orbit_trafficspeed_dic[i],'RAINY').get_time()
                min_time[i]=min(orb1.items(), key=lambda x: x[1])    
            
            shortest_path = min(min_time.items(), key=lambda x: x[1][1])
            print(shortest_path[1][0],shortest_path[0])
    
    except weather_input_error:
        print("Error!!. Please check the weather input.")
    except traffic_speed_error:
        print("Error!!. Please check the traffic speed. It should not be negative.")
    except TypeError:
        print("Error!!. Please check the input carefully.")
        
            
if __name__ == "__main__":
    main(Exception)