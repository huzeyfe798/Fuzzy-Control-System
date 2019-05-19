import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


MARKET_VALUE = float(input("Enter Market Value: "))
MARKET_VALUE = MARKET_VALUE / 1000
LOCATION = float(input("Enter House Location: "))
PERSONAL_ASSET = float(input("Enter Asset Value: "))
PERSONAL_ASSET = PERSONAL_ASSET / 1000
PERSONAL_INCOME = float(input("Enter Income Value: "))
PERSONAL_INCOME = PERSONAL_INCOME / 1000
INTEREST = float(input("Enter Interest Value: "))






#house compute
market_value = ctrl.Antecedent(np.arange(0, 1001, 1), 'market_value')
location = ctrl.Antecedent(np.arange(0, 11, 0.5), 'location')
house = ctrl.Consequent(np.arange(0,11,1),'house')
house_an = ctrl.Antecedent(np.arange(0,11,1),'house_an')


market_value['low'] = fuzz.trapmf(market_value.universe, [0, 0, 75, 100])
market_value['medium'] = fuzz.trapmf(market_value.universe, [50, 100, 200, 250])
market_value['high'] = fuzz.trapmf(market_value.universe, [200, 300, 650, 850])
market_value['veryhigh'] = fuzz.trapmf(market_value.universe, [650, 850, 1000, 1000])

location['bad'] = fuzz.trapmf(location.universe, [0,0,1.5,4])
location['fair'] = fuzz.trapmf(location.universe, [2.5,5,6,8.5])
location['excellent'] = fuzz.trapmf(location.universe, [6,8.5,10,10])

house['very low'] = fuzz.trimf(house.universe,[0,0,3])
house['low'] = fuzz.trimf(house.universe,[0,3,6])
house['medium'] = fuzz.trimf(house.universe,[2,5,8])
house['high'] = fuzz.trimf(house.universe,[4,7,10])
house['very high'] = fuzz.trimf(house.universe,[7,10,10])

house_an['very low'] = fuzz.trimf(house_an.universe,[0,0,3])
house_an['low'] = fuzz.trimf(house_an.universe,[0,3,6])
house_an['medium'] = fuzz.trimf(house_an.universe,[2,5,8])
house_an['high'] = fuzz.trimf(house_an.universe,[4,7,10])
house_an['very high'] = fuzz.trimf(house_an.universe,[7,10,10])



house_rule1 = ctrl.Rule(market_value['low'], house['low'])
house_rule2 = ctrl.Rule(location['bad'], house['low'])
house_rule3 = ctrl.Rule(location['bad'] & market_value['low'], house['very low'])
house_rule4 = ctrl.Rule(location['bad'] & market_value['medium'], house['low'])
house_rule5 = ctrl.Rule(location['bad'] & market_value['high'], house['medium'])
house_rule6 = ctrl.Rule(location['bad'] & market_value['veryhigh'], house['high'])
house_rule7 = ctrl.Rule(location['fair'] & market_value['low'], house['low'])
house_rule8 = ctrl.Rule(location['fair'] & market_value['medium'], house['medium'])
house_rule9 = ctrl.Rule(location['fair'] & market_value['high'], house['high'])
house_rule10 = ctrl.Rule(location['fair'] & market_value['veryhigh'], house['very high'])
house_rule11 = ctrl.Rule(location['excellent'] & market_value['low'], house['medium'])
house_rule12 = ctrl.Rule(location['excellent'] & market_value['medium'], house['very high'])
house_rule13 = ctrl.Rule(location['excellent'] & market_value['high'], house['very high'])
house_rule14 = ctrl.Rule(location['excellent'] & market_value['veryhigh'], house['very high'])

house_ctrl = ctrl.ControlSystem([house_rule1, house_rule2, house_rule3, house_rule4, house_rule5, house_rule6,
                                 house_rule7, house_rule8, house_rule9, house_rule10, house_rule11, house_rule12, house_rule13, house_rule14])

house_value = ctrl.ControlSystemSimulation(house_ctrl)

house_value.input['market_value'] = MARKET_VALUE
house_value.input['location'] = LOCATION

house_value.compute()
#input
house_out = house_value.output['house']

print(house_value.output['house'])
house.view(sim=house_value)

#applicant compute

personal_asset = ctrl.Antecedent(np.arange(0, 1001, 1), 'personal_asset')
personal_income = ctrl.Antecedent(np.arange(0, 101, 1), 'personal_income')
applicant = ctrl.Consequent(np.arange(0,11,1),'applicant')

applicant_an = ctrl.Antecedent(np.arange(0,11,1),'applicant_an')

personal_asset['low'] = fuzz.trimf(personal_asset.universe, [0, 0, 150])
personal_asset['medium'] = fuzz.trapmf(personal_asset.universe, [50, 250, 450, 650])
personal_asset['high'] = fuzz.trapmf(personal_asset.universe, [500, 700, 1000, 1000])



personal_income['low'] = fuzz.trapmf(personal_income.universe, [0, 0, 10, 25])
personal_income['medium'] = fuzz.trimf(personal_income.universe, [15, 35, 55])
personal_income['high'] = fuzz.trimf(personal_income.universe, [40, 60, 80])
personal_income['very high'] = fuzz.trapmf(personal_income.universe, [60, 80, 100, 100])

applicant['low'] = fuzz.trapmf(applicant.universe, [0, 0, 2, 4])
applicant['medium'] = fuzz.trimf(applicant.universe, [2, 5, 8])
applicant['high'] = fuzz.trapmf(applicant.universe, [6, 8, 10, 10])

applicant_an['low'] = fuzz.trapmf(applicant.universe, [0, 0, 2, 4])
applicant_an['medium'] = fuzz.trimf(applicant.universe, [2, 5, 8])
applicant_an['high'] = fuzz.trapmf(applicant.universe, [6, 8, 10, 10])

applicant_rule1 = ctrl.Rule(personal_income['low'] & personal_asset['low'], applicant['low'])
applicant_rule2 = ctrl.Rule(personal_income['medium'] & personal_asset['low'], applicant['low'])
applicant_rule3 = ctrl.Rule(personal_income['high'] & personal_asset['low'], applicant['medium'])
applicant_rule4 = ctrl.Rule(personal_income['very high'] & personal_asset['low'], applicant['high'])
applicant_rule5 = ctrl.Rule(personal_income['low'] & personal_asset['medium'], applicant['low'])
applicant_rule6 = ctrl.Rule(personal_income['medium'] & personal_asset['medium'], applicant['medium'])
applicant_rule7 = ctrl.Rule(personal_income['high'] & personal_asset['medium'], applicant['high'])
applicant_rule8 = ctrl.Rule(personal_income['very high'] & personal_asset['medium'], applicant['high'])
applicant_rule9 = ctrl.Rule(personal_income['low'] & personal_asset['high'], applicant['medium'])
applicant_rule10 = ctrl.Rule(personal_income['medium'] & personal_asset['high'], applicant['medium'])
applicant_rule11 = ctrl.Rule(personal_income['high'] & personal_asset['high'], applicant['high'])
applicant_rule12 = ctrl.Rule(personal_income['very high'] & personal_asset['high'], applicant['high'])

applicant_ctrl = ctrl.ControlSystem([applicant_rule1, applicant_rule2, applicant_rule3, applicant_rule4, applicant_rule5, applicant_rule6,
                                 applicant_rule7, applicant_rule8, applicant_rule9, applicant_rule10, applicant_rule11, applicant_rule12])

applicant_value = ctrl.ControlSystemSimulation(applicant_ctrl)

applicant_value.input['personal_asset'] = PERSONAL_ASSET
applicant_value.input['personal_income'] = PERSONAL_INCOME

applicant_value.compute()

applicant_out = applicant_value.output['applicant']

print(applicant_value.output['applicant'])
applicant.view(sim=applicant_value)


#interest define

interest = ctrl.Antecedent(np.arange(0, 11, 0.5), 'interest')

interest['low'] = fuzz.trapmf(interest.universe, [0,0,2,5])
interest['medium'] = fuzz.trapmf(interest.universe, [2,4,6,8])
interest['high'] = fuzz.trapmf(interest.universe, [6,8.5,10,10])

credit = ctrl.Consequent(np.arange(0,501,1),'credit')

credit['very low'] = fuzz.trimf(credit.universe, [0, 0, 125])
credit['low'] = fuzz.trimf(credit.universe, [0, 125, 250])
credit['medium'] = fuzz.trimf(credit.universe, [125, 250, 375])
credit['high'] = fuzz.trimf(credit.universe, [250, 375, 500])
credit['very high'] = fuzz.trimf(credit.universe, [375, 500, 500])


#final compute


credit_rule1 = ctrl.Rule(personal_income['low'] & interest['medium'], credit['very low'])
credit_rule2 = ctrl.Rule(personal_income['low'] & interest['high'], credit['very low'])
credit_rule3 = ctrl.Rule(personal_income['medium'] & interest['high'], credit['low'])
credit_rule4 = ctrl.Rule(applicant_an['low'], credit['very low'])
credit_rule5 = ctrl.Rule(house_an['very low'] , credit['very low'])
credit_rule6 = ctrl.Rule(applicant_an['medium'] & house_an['very low'], credit['low'])
credit_rule7 = ctrl.Rule(applicant_an['medium'] & house_an['low'], credit['low'])
credit_rule8 = ctrl.Rule(applicant_an['medium'] & house_an['medium'], credit['medium'])
credit_rule9 = ctrl.Rule(applicant_an['medium'] & house_an['high'], credit['high'])
credit_rule10 = ctrl.Rule(applicant_an['medium'] & house_an['very high'], credit['high'])
credit_rule11 = ctrl.Rule(applicant_an['high'] & house_an['very low'], credit['low'])
credit_rule12 = ctrl.Rule(applicant_an['high'] & house_an['low'], credit['medium'])
credit_rule13 = ctrl.Rule(applicant_an['high'] & house_an['medium'], credit['high'])
credit_rule14 = ctrl.Rule(applicant_an['high'] & house_an['high'], credit['high'])
credit_rule15 = ctrl.Rule(applicant_an['high'] & house_an['very high'], credit['very high'])

credit_ctrl = ctrl.ControlSystem([credit_rule1, credit_rule2, credit_rule3, credit_rule4, credit_rule5, credit_rule6, credit_rule7, credit_rule8, credit_rule9, credit_rule10, credit_rule11, credit_rule12, credit_rule13, credit_rule14, credit_rule15])

credit_value = ctrl.ControlSystemSimulation(credit_ctrl)

credit_value.input['house_an'] = house_out
credit_value.input['personal_income'] = PERSONAL_INCOME
credit_value.input['applicant_an'] = applicant_out
credit_value.input['interest'] = INTEREST


credit_value.compute()

print(credit_value.output['credit']*1000)
credit.view(sim=credit_value)
