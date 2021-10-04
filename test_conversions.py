import unittest
import conversions

class KnownValues(unittest.TestCase):
#here we are setting up test value cases for each conversion:
    known_values_C_K = ( 
        
        (500.00, 773.15),
        (490.00, 763.15),
        (270.00, 543.15),
        (20.00, 293.15),
        (-140.00, 133.15),
        (-273.15, 0.0)
                     
        )
    
    known_values_C_F = (
        
        (500.00, 932.00),
        (450.00, 842.00),
        (170.00, 338.00),
        (0.00, 32.00),
        (-40.00, -40.00),
        (-273.15, -459.67)
        
        )
    
    known_values_F_C = (
        
        (932.00, 500.00),
        (806.00, 430.00),
        (536.00, 280.00),
        (32.00, 0.00),
        (-76.00, -60.00),
        (-459.67, -273.15)
        
        )
    
    known_values_F_K = (
        
        (932.00, 773.15),
        (788.00, 693.15),
        (518.00, 543.15),
        (32.00, 273.15),
        (-166.00, 163.15),
        (-459.67, 0.00)
        
        )
    
    known_values_K_F = (
        
        (773.15, 932.00),
        (653.15, 716.00),
        (393.15, 248.00),
        (273.15, 32.00),
        (33.15, -400.00),
        (0.00, -459.67)
        
        )
    
    known_values_K_C = (
        
        (773.15, 500.00),
        (623.15, 350.00),
        (403.15, 130.00),
        (273.15, 0.00),
        (63.15, -210.00),
        (0.00, -273.15)
        
        )
 
    
    def test_to_all(self):
        #coverting to temparatues 
        for C,K in self.known_values_C_K:
            result = conversions.convertCelsiusToKelvin(C)
            self.assertAlmostEqual(K,result)
            print('The temperature {0} in Celius is {1} in Kelvin'.format(C,result))
    
        for C,F in self.known_values_C_F:
            result = conversions.convertCelsiusToFahrenheit(C)
            self.assertAlmostEqual(F,result)
            print('The temperature {0} in Celius is {1} in Fahrenheit'.format(C,result))
        
        for F,C in self.known_values_F_C:
            result = conversions.convertFahrenheitToCelsius(F)
            self.assertAlmostEqual(C,result)
            print('The temperature {0} in Fahrenheit is {1} in Celsius'.format(F,result))
            
        for F,K in self.known_values_F_K:
            result = conversions.convertFahrenheitToKelvin(F)
            self.assertAlmostEqual(K,result)
            print('The temperature {0} in Fahrenheit is {1} in Kelvin '.format(F,result))
            
        for K,F in self.known_values_K_F:
            result = conversions.convertKelvinToFahrenheit(K)
            self.assertAlmostEqual(F,result)
            print('The temperature {0} in Kelvin is {1} in Fahrenheit '.format(K,result))
        
        for K,C in self.known_values_K_C:
            result = conversions.convertKelvinToCelsius(K)
            self.assertAlmostEqual(C,result)
            print('The temperature {0} in Kelvin is {1} in Celsius '.format(K,result))
        
if __name__ == '__main__':
    unittest.main()
