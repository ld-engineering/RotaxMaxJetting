from time import sleep
import math
import sys

#Variables   
alpha = -0.0065
beta = 5.255877432
Rs = 287.053
Tref= 288.15
densityAirRef1 = 1.224999463
heightRef1 = 9685.0
heightRef2 = 2038.5
href = 0.0
pd = 611.213
pdRef1 = 17.5043
pdRef2 = 241.2
pref = 101325
rotax_costant = 0.3773253796095445

print("Dell'Orto VHSB34 Configuration for Rotax MAX engines")
print("Based on Rotax Jetting app v2.0.0")

temperature = float(input("Temeperature (°C): "))
temperature_kelvin = temperature + 273.15
altitude = float(input("Altitude (m): "))
var_d = float(input("Pressure (mbar): "))
vard_d2 = float(input("Umidity (%): "))
if vard_d2 > 100:
    print("Max value for umidity is 100")
    sleep(5)
    sys.exit()
elif vard_d2 < 0:
    print("Min. value for umidity is 0")
    sleep(5)
    sys.exit()
elif var_d < 0:
    print("Min. value for pressure is 0")
    sleep(5)
    sys.exit()
else:
    print("write info for having more information")
    engine_type = input("Engine type: ").lower()

    if engine_type == 'info':
        print("Available engine configurations:")
        print("micro, mini, junior, senior, dd2, custom")
        print("Needle is K57 with clip position in the third slot(from the top), air screw is 1.5/2 turns out from closed")
        sleep(60)
    elif engine_type == 'micro':
        engine_spec = 110
        engine_spec_new = 111
    elif engine_type == 'mini':
        engine_spec = 115
        engine_spec_new = 117
    elif engine_type == 'junior':
        engine_spec = 129
        engine_spec_new = 129
    elif engine_type == 'senior':
        engine_spec = 128
        engine_spec_new = 128
    elif engine_type == 'dd2':
        engine_spec = 136
        engine_spec_new = 132
    elif engine_type == 'custom':
        engine_spec = int(input("Main jet: "))
    else:
        print("This type of engine doesn't exists, use one the following engine specs")
        print("micro, mini, junior, senior, dd2, custom")
        sleep(5)
        sys.exit()

    pow = var_d * 100.0 * math.pow((((altitude - href) * alpha) + Tref) / Tref, beta)
    exp = pow / ((Rs / (1.0 - (((((math.exp((pdRef1 * temperature) / (temperature + pdRef2)) * pd) * vard_d2) / pow) / 100.0) * rotax_costant))) * temperature_kelvin)        
    exp_log = math.log(exp)

    if engine_type != 'custom' and engine_type != 'junior' and engine_type != 'senior':
        final_old = (engine_spec *(((-((1.0 - math.sqrt(exp / densityAirRef1)) * 100.0)) / 2.0) + 100.0)) / 100.0
        final_new = (engine_spec_new *(((-((1.0 - math.sqrt(exp / densityAirRef1)) * 100.0)) / 2.0) + 100.0)) / 100.0
        print("Main jet size using old configuration: " + str(math.trunc(final_old)))
        print("Main jet size using new configuration: " + str(math.trunc(final_new)))
        sleep(30)
    else:
        final = (engine_spec *(((-((1.0 - math.sqrt(exp / densityAirRef1)) * 100.0)) / 2.0) + 100.0)) / 100.0
        print("Main jet size: " + str(math.trunc(final)))
        sleep(30)

sys.exit()