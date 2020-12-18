from __future__ import division, print_function, absolute_import
from ACHP.Compressor import CompressorClass
import CoolProp as CP
from CoolProp.CoolProp import PropsSI

Ref = 'R448A.mix'
Backend = 'REFPROP' #choose between: 'HEOS','TTSE&HEOS','BICUBIC&HEOS','REFPROP','SRK','PR'
AS = CP.AbstractState(Backend, Ref)
fluid = f"{Backend}::{Ref}"   

kwds={
      # 'M':[217.3163128,5.094492028,-0.593170311,4.38E-02,-2.14E-02,1.04E-02,7.90E-05,-5.73E-05,1.79E-04,-8.08E-05],
      # 'P':[-561.3615705,-15.62601841,46.92506685,-0.217949552,0.435062616,-0.442400826,2.25E-04,2.37E-03,-3.32E-03,2.50E-03],
      'P' : [516.7314315,	-8.027291392,	12.18085185,	-0.239504654,	0.27550642,	-0.039809193,	-0.002564457,	0.001894206,	-0.001023899,	0.000426288],
      'M' : [182.9271859,	4.770930891,	-0.083612619,	0.063604522,	-0.002474897,	-0.000641904,	0.000466731,	-6.89E-05,	-2.56E-05,	0],
      'Ref':Ref,
      'Tin_r':280,
      'pin_r':PropsSI('P','T',279,'Q',1,fluid),
      'pout_r':PropsSI('P','T',315,'Q',1,fluid),
      'fp':0.15, #Fraction of electrical power lost as heat to ambient
      'Vdot_ratio': 1.0, #Displacement Scale factor
      'shell_pressure': 'low-pressure',
      'Oil': 'POE32',
      'V_oil_sump': 0.0,
      'AS':AS
      }
Comp=CompressorClass(**kwds)
Comp.Calculate()

print ('Electrical power is: ' + str(Comp.W) + ' W')
print ('Actual mass flow rate is: ' + str(Comp.mdot_r) + ' kg/s')
print ('Isentropic Efficiency is: ' + str(Comp.eta_oi))
print ('Discharge Refrigerant Temperature is: ' + str(Comp.Tout_r) + ' K')
print (' ')

'''to print all the output, uncomment the next 2 lines'''
# for id, unit, value in Comp.OutputList():                
#     print (str(id) + ' = ' + str(value) + ' ' + str(unit))





# =============================================================================
# RR	Rev.Date	Model	Data Status	Perf Sheet	Appl	Voltage Codes	Test Voltage	Hertz	Phase	Refr	Total Subcooling (F)	Constant Superheat (°F)	Constant Return Gas Temp. (°F)	Min. Cond. (°F)	Max. Cond. (°F)	Min. Evap. (°F)	Max. Evap. (°F)	RT_C0	RT_C1	RT_C2	RT_C3	RT_C4	RT_C5	RT_C6	RT_C7	RT_C8	RT_C9	RT_W0	RT_W1	RT_W2	RT_W3	RT_W4	RT_W5	RT_W6	RT_W7	RT_W8	RT_W9	RT_A0	RT_A1	RT_A2	RT_A3	RT_A4	RT_A5	RT_A6	RT_A7	RT_A8	RT_A9	RT_M0	RT_M1	RT_M2	RT_M3	RT_M4	RT_M5	RT_M6	RT_M7	RT_M8	RT_M9
#  17-1443	 8/31/2017	 ZF07KAE-TF5	 Y	1.4XLL60-17-1443	LL	TF5,TFD	230	60	3	448A	0	N	40	40	140	-40	10	19339.50413	486.198366	-74.18803854	5.554632125	-1.824627609	0	0.030094493	-0.018874372	-0.001689688	-0.000248838	516.7314315	-8.027291392	12.18085185	-0.239504654	0.27550642	-0.039809193	-0.002564457	0.001894206	-0.001023899	0.000426288	3.644701239	0	0.006157051	-0.000388095	-0.000309701	0	0	4.80E-06	4.60E-06	1.34E-06	182.9271859	4.770930891	-0.083612619	0.063604522	-0.002474897	-0.000641904	0.000466731	-6.89E-05	-2.56E-05	0
# 
# =============================================================================

C = [19339.50413,	486.198366,	-74.18803854,	5.554632125,	-1.824627609,	0,	0.030094493,	-0.018874372,	-0.001689688,	-0.000248838]
P = [516.7314315,	-8.027291392,	12.18085185,	-0.239504654,	0.27550642,	-0.039809193,	-0.002564457,	0.001894206,	-0.001023899,	0.000426288]
A = [3.644701239,	0,	0.006157051,	-0.000388095,	-0.000309701,	0,	0,	4.80E-06,	4.60E-06,	1.34E-06]
M = [182.9271859,	4.770930891,	-0.083612619,	0.063604522,	-0.002474897,	-0.000641904,	0.000466731,	-6.89E-05,	-2.56E-05,	0]

