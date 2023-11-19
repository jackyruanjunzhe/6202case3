import random
import pandas as pd
# generate random integer values
from random import seed
from random import randint


# Generate a random value between 0 to 1 to determine the annual demand forecast number
myrandom = random.random()

if myrandom < 0.3:
    demand_year1 = 80000
    demand_year2 = 90000
    demand_year3 = 100000
    demand_year4 = 105000
    demand_year5 = 110000
elif myrandom < 0.55:
    demand_year1 = 60000
    demand_year2 = 65000
    demand_year3 = 70000
    demand_year4 = 80000
    demand_year5 = 90000
elif myrandom < 0.75:
    demand_year1 = 80000
    demand_year2 = 100000
    demand_year3 = 110000
    demand_year4 = 120000
    demand_year5 = 150000
elif myrandom < 0.9:
    demand_year1 = 50000
    demand_year2 = 70000
    demand_year3 = 75000
    demand_year4 = 75000
    demand_year5 = 65000
else:
    demand_year1 = 50000
    demand_year2 = 60000
    demand_year3 = 60000
    demand_year4 = 60000
    demand_year5 = 60000

list_fiveyear_day_demand = []
list_year_demand = [demand_year1,demand_year2,demand_year3,demand_year4,demand_year5]
for demand_year in list_year_demand:

    ## calculate 4 week period demand based on form
    list_4week_demand = []
    list_4week_ratio = [0.06,0.05,0.06,0.07,0.09,0.06,0.04,0.10,0.10,0.06,0.08,0.10,0.13]
    for ratio in list_4week_ratio:
        demand = demand_year * ratio
        list_4week_demand.append(demand)

    list_week_demand = []
    for fourweekdemand in list_4week_demand:
        oneweekdemand = fourweekdemand/4
        for n in range(1,5):
            list_week_demand.append(oneweekdemand)

    list_weekday_ratio =[0.05,0.1,0.15,0.15,0.18,0.22,0.15]
    list_day_demand = []
    for weekdemand in list_week_demand:
        for ratio in list_weekday_ratio:
            list_day_demand.append(round(weekdemand * ratio))
    list_fiveyear_day_demand.append(list_day_demand)
demandframe = pd.DataFrame()
demandframe['year1'] = list_fiveyear_day_demand[0]
demandframe['year2'] = list_fiveyear_day_demand[1]
demandframe['year3'] = list_fiveyear_day_demand[2]
demandframe['year4'] = list_fiveyear_day_demand[3]
demandframe['year5'] = list_fiveyear_day_demand[4]

##Generate the expected demand for each day for five years and show it in excel
demandframe.to_csv('dailydemand.csv')

##figure out the pickup time and deliver time for each demand

##use a random generator between 0 to 10000 to determine the deliver time and pick up time for each demand
##list of pickup and delivertime
list_p = []
list_d = []
list_space = []
space = 0
totaldemand = demand_year1 +demand_year2 + demand_year3 + demand_year4 + demand_year5
for i in range(totaldemand):
    random_10000 = random.randint(0,10000)
    itrandom = random.random()
    if itrandom < 0.08:
        space = 1
    elif itrandom < 0.2:
        space = 2
    elif itrandom < 0.35:
        space = 3
    elif itrandom < 0.47:
        space = 4
    elif itrandom < 0.55:
        space = 5
    elif itrandom < 0.61:
        space = 6
    elif itrandom < 0.66:
        space = 7
    elif itrandom < 0.71:
        space = 8
    elif itrandom < 0.76:
        space = 9
    elif itrandom < 0.8:
        space = 10
    elif itrandom < 0.84:
        space = 11
    elif itrandom < 0.87:
        space = 12
    elif itrandom < 0.90:
        space = 13
    elif itrandom < 0.93:
        space = 14
    elif itrandom < 0.95:
        space = 15
    elif itrandom < 0.97:
        space = 16
    elif itrandom < 0.99:
        space = 17
    else:
        space = 18

    if random_10000 < 30:
        p = 0
        d = 0
    elif random_10000 < 50:
        p = 1
        d = 0
    elif random_10000 < 54:
        p = 2
        d = 0
    elif random_10000 < 58:
        p = 3
        d= 0
    elif random_10000 < 62:
        p = 4
        d= 0
    elif random_10000 < 72:
        p = 5
        d= 0
    elif random_10000 < 92:
        p = 6
        d= 0
    elif random_10000 < 116:
        p = 7
        d= 0
    elif random_10000 < 148:
        p = 8
        d= 0
    elif random_10000 < 168:
        p = 9
        d= 0
    elif random_10000 < 180:
        p = 10
        d= 0
    elif random_10000 < 192:
        p = 11
        d= 0
    elif random_10000 < 200:
        p = 12
        d= 0
    elif random_10000 < 224:
        p = 1
        d= 1
    elif random_10000 < 236:
        p = 2
        d= 1
    elif random_10000 < 242:
        p = 3
        d= 1
    elif random_10000 < 246:
        p = 4
        d= 1
    elif random_10000 < 256:
        p = 5
        d= 1
    elif random_10000 < 276:
        p = 6
        d= 1
    elif random_10000 < 300:
        p = 7
        d= 1
    elif random_10000 < 332:
        p = 8
        d= 1
    elif random_10000 < 352:
        p = 9
        d= 1
    elif random_10000 < 368:
        p = 10
        d= 1
    elif random_10000 < 380:
        p = 11
        d= 1
    elif random_10000 < 392:
        p = 12
        d= 1
    elif random_10000 < 400:
        p = 13
        d= 1
    elif random_10000 < 412:
        p = 2
        d= 2
    elif random_10000 < 418:
        p = 3
        d= 2
    elif random_10000 < 421:
        p = 4
        d= 2
    elif random_10000 < 426:
        p = 5
        d= 2
    elif random_10000 < 436:
        p = 6
        d= 2
    elif random_10000 < 448:
        p = 7
        d= 2
    elif random_10000 < 464:
        p = 8
        d= 2
    elif random_10000 < 474:
        p = 9
        d= 2
    elif random_10000 < 482:
        p = 10
        d= 2
    elif random_10000 < 488:
        p = 11
        d= 2
    elif random_10000 < 494:
        p = 12
        d= 2
    elif random_10000 < 498:
        p = 13
        d= 2
    elif random_10000 < 500:
        p = 14
        d= 2
    elif random_10000 < 512:
        p = 3
        d= 3
    elif random_10000 < 518:
        p = 4
        d= 3
    elif random_10000 < 521:
        p = 5
        d= 3
    elif random_10000 < 531:
        p = 6
        d= 3
    elif random_10000 < 543:
        p =7
        d= 3
    elif random_10000 < 559:
        p = 8
        d= 3
    elif random_10000 < 569:
        p = 9
        d= 3
    elif random_10000 < 577:
        p = 10
        d= 3
    elif random_10000 < 583:
        p = 11
        d= 3
    elif random_10000 < 589:
        p = 12
        d= 3
    elif random_10000 < 593:
        p = 13
        d= 3
    elif random_10000 < 597:
        p = 14
        d= 3
    elif random_10000 < 600:
        p = 15
        d= 3
    elif random_10000 < 636:
        p = 4
        d= 4
    elif random_10000 < 660:
        p = 5
        d= 4
    elif random_10000 < 690:
        p = 6
        d= 4
    elif random_10000 < 726:
        p = 7
        d= 4
    elif random_10000 < 774:
        p = 8
        d= 4
    elif random_10000 < 804:
        p = 9
        d= 4
    elif random_10000 < 828:
        p = 10
        d= 4
    elif random_10000 < 846:
        p = 11
        d= 4
    elif random_10000 < 864:
        p = 12
        d= 4
    elif random_10000 < 879:
        p = 13
        d= 4
    elif random_10000 < 891:
        p = 14
        d= 4
    elif random_10000 < 900:
        p = 15
        d= 4
    elif random_10000 < 936:
        p = 5
        d= 5
    elif random_10000 < 981:
        p = 6
        d= 5
    elif random_10000 < 1026:
        p = 7
        d= 5
    elif random_10000 < 1074:
        p = 8
        d= 5
    elif random_10000 < 1104:
        p = 9
        d= 5
    elif random_10000 < 1128:
        p = 10
        d= 5
    elif random_10000 < 1146:
        p = 11
        d= 5
    elif random_10000 < 1164:
        p = 12
        d= 5
    elif random_10000 < 1179:
        p = 13
        d= 5
    elif random_10000 < 1191:
        p = 14
        d= 5
    elif random_10000 < 1200:
        p = 15
        d= 5
    elif random_10000 < 1260:
        p = 6
        d= 6
    elif random_10000 < 1320:
        p = 7
        d= 6
    elif random_10000 < 1392:
        p = 8
        d= 6
    elif random_10000 < 1436:
        p = 9
        d= 6
    elif random_10000 < 1468:
        p = 10
        d= 6
    elif random_10000 < 1492:
        p = 11
        d= 6
    elif random_10000 < 1516:
        p = 12
        d= 6
    elif random_10000 < 1536:
        p = 13
        d= 6
    elif random_10000 < 1552:
        p =14
        d= 6
    elif random_10000 < 1568:
        p = 15
        d= 6
    elif random_10000 < 1588:
        p = 16
        d= 6
    elif random_10000 < 1600:
        p = 17
        d= 6
    elif random_10000 < 1672:
        p = 7
        d= 7
    elif random_10000 < 1772:
        p = 8
        d= 7
    elif random_10000 < 1820:
        p = 9
        d= 7
    elif random_10000 < 1852:
        p = 10
        d= 7
    elif random_10000 < 1876:
        p = 11
        d= 7
    elif random_10000 < 1900:
        p = 12
        d= 7
    elif random_10000 < 1920:
        p = 13
        d= 7
    elif random_10000 < 1936:
        p = 14
        d= 7
    elif random_10000 < 1952:
        p = 15
        d= 7
    elif random_10000 < 1972:
        p = 16
        d= 7
    elif random_10000 < 1988:
        p = 17
        d= 7
    elif random_10000 < 2000:
        p = 18
        d= 7
    elif random_10000 < 2150:
        p = 8
        d= 8
    elif random_10000 < 2270:
        p = 9
        d= 8
    elif random_10000 < 2330:
        p = 10
        d= 8
    elif random_10000 < 2378:
        p = 11
        d= 8
    elif random_10000 < 2426:
        p = 12
        d= 8
    elif random_10000 < 2462:
        p = 13
        d= 8
    elif random_10000 < 2486:
        p = 14
        d= 8
    elif random_10000 < 2510:
        p = 15
        d= 8
    elif random_10000 < 2540:
        p = 16
        d= 8
    elif random_10000 < 2564:
        p = 17
        d= 8
    elif random_10000 < 2582:
        p = 18
        d= 8
    elif random_10000 < 2600:
        p = 19
        d= 8
    elif random_10000 < 2720:
        p = 9
        d= 9
    elif random_10000 < 2816:
        p = 10
        d= 9
    elif random_10000 < 2906:
        p = 11
        d= 9
    elif random_10000 < 2966:
        p = 12
        d= 9
    elif random_10000 < 3002:
        p = 13
        d= 9
    elif random_10000 < 3026:
        p = 14
        d= 9
    elif random_10000 < 3086:
        p = 15
        d= 9
    elif random_10000 < 3128:
        p = 16
        d= 9
    elif random_10000 < 3158:
        p = 17
        d= 9
    elif random_10000 < 3176:
        p = 18
        d= 9
    elif random_10000 < 3188:
        p = 19
        d= 9
    elif random_10000 < 3200:
        p = 20
        d= 9
    elif random_10000 < 3290:
        p = 10
        d= 10
    elif random_10000 < 3398:
        p = 11
        d= 10
    elif random_10000 < 3506:
        p = 12
        d=  10
    elif random_10000 < 3596:
        p = 13
        d= 10
    elif random_10000 < 3626:
        p = 14
        d= 10
    elif random_10000 < 3650:
        p = 15
        d= 10
    elif random_10000 < 3686:
        p = 16
        d= 10
    elif random_10000 < 3728:
        p = 17
        d= 10
    elif random_10000 < 3758:
        p = 18
        d= 10
    elif random_10000 < 3776:
        p = 19
        d= 10
    elif random_10000 < 3788:
        p = 20
        d= 10
    elif random_10000 < 3800:
        p = 21
        d= 10
    elif random_10000 < 3920:
        p = 11
        d= 11
    elif random_10000 < 4058:
        p = 12
        d= 11
    elif random_10000 < 4148:
        p = 13
        d= 11
    elif random_10000 < 4196:
        p = 14
        d= 11
    elif random_10000 < 4232:
        p = 15
        d= 11
    elif random_10000 < 4268:
        p = 16
        d= 11
    elif random_10000 < 4316:
        p = 17
        d= 11
    elif random_10000 < 4346:
        p = 18
        d= 11
    elif random_10000 < 4364:
        p = 19
        d=11
    elif random_10000 < 4376:
        p = 20
        d= 11
    elif random_10000 < 4388:
        p = 21
        d= 11
    elif random_10000 < 4400:
        p = 22
        d= 11
    elif random_10000 < 4480:
        p = 12
        d= 12
    elif random_10000 < 4580:
        p = 13
        d= 12
    elif random_10000 < 4620:
        p = 14
        d= 12
    elif random_10000 < 4652:
        p = 15
        d= 12
    elif random_10000 < 4684:
        p = 16
        d= 12
    elif random_10000 < 4724:
        p = 17
        d= 12
    elif random_10000 < 4764:
        p = 18
        d= 12
    elif random_10000 < 4776:
        p = 19
        d= 12
    elif random_10000 < 4784:
        p = 20
        d= 12
    elif random_10000 < 4792:
        p = 21
        d= 12
    elif random_10000 < 4796:
        p = 22
        d= 12
    elif random_10000 < 4800:
        p = 23
        d= 12
    elif random_10000 < 4920:
        p = 13
        d= 13
    elif random_10000 < 5028:
        p = 14
        d= 13
    elif random_10000 < 5088:
        p = 15
        d= 13
    elif random_10000 < 5136:
        p = 16
        d= 13
    elif random_10000 < 5196:
        p = 17
        d= 13
    elif random_10000 < 5256:
        p = 18
        d= 13
    elif random_10000 < 5316:
        p = 19
        d= 13
    elif random_10000 < 5352:
        p = 20
        d= 13
    elif random_10000 < 5376:
        p = 21
        d= 13
    elif random_10000 < 5394:
        p = 22
        d= 13
    elif random_10000 < 5400:
        p = 23
        d= 13
    elif random_10000 < 5560:
        p = 14
        d= 14
    elif random_10000 < 5704:
        p = 15
        d= 14
    elif random_10000 < 5816:
        p = 16
        d= 14
    elif random_10000 < 5928:
        p = 17
        d= 14
    elif random_10000 < 6008:
        p = 18
        d= 14
    elif random_10000 < 6088:
        p = 19
        d= 14
    elif random_10000 < 6136:
        p = 20
        d= 14
    elif random_10000 < 6168:
        p = 21
        d= 14
    elif random_10000 < 6192:
        p = 22
        d= 14
    elif random_10000 < 6200:
        p = 23
        d= 14
    elif random_10000 < 6320:
        p = 15
        d= 15
    elif random_10000 < 6440:
        p = 16
        d= 15
    elif random_10000 < 6560:
        p = 17
        d= 15
    elif random_10000 < 6650:
        p = 18
        d= 15
    elif random_10000 < 6716:
        p = 19
        d= 15
    elif random_10000 < 6752:
        p = 20
        d= 15
    elif random_10000 < 6776:
        p = 21
        d= 15
    elif random_10000 < 6794:
        p = 22
        d= 15
    elif random_10000 < 6800:
        p = 23
        d= 15
    elif random_10000 < 6920:
        p = 16
        d= 16
    elif random_10000 < 7070:
        p = 17
        d= 16
    elif random_10000 < 7190:
        p = 18
        d= 16
    elif random_10000 < 7328:
        p = 20
        d= 16
    elif random_10000 < 7364:
        p = 21
        d= 16
    elif random_10000 < 7388:
        p = 22
        d= 16
    elif random_10000 < 7400:
        p = 23
        d= 16
    elif random_10000 < 7520:
        p = 17
        d= 17
    elif random_10000 < 7700:
        p = 18
        d= 17
    elif random_10000 < 7820:
        p = 19
        d= 17
    elif random_10000 < 7964:
        p = 20
        d= 17
    elif random_10000 < 7988:
        p = 21
        d= 17
    elif random_10000 < 8000:
        p = 22
        d= 17
    elif random_10000 < 8010:
        p = 6
        d= 18
    elif random_10000 < 8050:
        p = 7
        d= 18
    elif random_10000 < 8070:
        p = 8
        d= 18
    elif random_10000 < 8080:
        p = 9
        d= 18
    elif random_10000 < 8180:
        p = 18
        d= 18
    elif random_10000 < 8300:
        p = 19
        d= 18
    elif random_10000 < 8400:
        p = 20
        d= 18
    elif random_10000 < 8470:
        p = 21
        d= 18
    elif random_10000 < 8490:
        p = 22
        d= 18
    elif random_10000 < 8500:
        p = 23
        d= 18
    elif random_10000 < 8505:
        p = 0
        d= 19
    elif random_10000 < 8520:
        p = 6
        d= 19
    elif random_10000 < 8570:
        p = 7
        d= 19
    elif random_10000 < 8610:
        p = 8
        d= 19
    elif random_10000 < 8625:
        p = 9
        d= 19
    elif random_10000 < 8725:
        p = 19
        d= 19
    elif random_10000 < 8875:
        p = 20
        d= 19
    elif random_10000 < 8950:
        p = 21
        d= 19
    elif random_10000 < 8985:
        p = 22
        d= 19
    elif random_10000 < 9000:
        p = 23
        d= 19
    elif random_10000 < 9108:
        p = 0
        d= 20
    elif random_10000 < 9028:
        p = 6
        d= 20
    elif random_10000 < 9088:
        p = 7
        d= 20
    elif random_10000 < 9128:
        p = 8
        d= 20
    elif random_10000 < 9140:
        p = 9
        d= 20
    elif random_10000 < 9148:
        p = 10
        d= 20
    elif random_10000 < 9156:
        p = 11
        d= 20
    elif random_10000 < 9160:
        p = 12
        d= 20
    elif random_10000 < 9240:
        p = 20
        d= 20
    elif random_10000 < 9340:
        p = 21
        d= 20
    elif random_10000 < 9380:
        p = 22
        d= 20
    elif random_10000 < 9400:
        p = 23
        d= 20
    elif random_10000 < 9410:
        p = 0
        d= 21
    elif random_10000 < 9414:
        p = 1
        d= 21
    elif random_10000 < 9426:
        p = 6
        d= 21
    elif random_10000 < 9462:
        p = 7
        d= 21
    elif random_10000 < 9492:
        p = 8
        d= 21
    elif random_10000 < 9500:
        p = 9
        d= 21
    elif random_10000 < 9504:
        p = 10
        d= 21
    elif random_10000 < 9508:
        p = 11
        d= 21
    elif random_10000 < 9510:
        p = 12
        d= 21
    elif random_10000 < 9540:
        p = 21
        d= 21
    elif random_10000 < 9580:
        p = 22
        d= 21
    elif random_10000 < 9600:
        p = 23
        d= 21
    elif random_10000 < 9620:
        p = 0
        d= 22
    elif random_10000 < 9630:
        p = 1
        d= 22
    elif random_10000 < 9634:
        p = 3
        d= 22
    elif random_10000 < 9646:
        p = 6
        d= 22
    elif random_10000 < 9682:
        p = 7
        d= 22
    elif random_10000 < 9712:
        p = 8
        d= 22
    elif random_10000 < 9720:
        p = 9
        d= 22
    elif random_10000 < 9724:
        p = 10
        d= 22
    elif random_10000 < 9728:
        p = 11
        d= 22
    elif random_10000 < 9730:
        p = 12
        d= 22
    elif random_10000 < 9760:
        p = 22
        d= 22
    elif random_10000 < 9800:
        p = 23
        d= 22
    elif random_10000 < 9830:
        p = 0
        d= 23
    elif random_10000 < 9844:
        p = 1
        d= 23
    elif random_10000 < 9850:
        p = 2
        d= 23
    elif random_10000 < 9866:
        p = 6
        d= 23
    elif random_10000 < 9906:
        p = 7
        d= 23
    elif random_10000 < 9942:
        p = 8
        d= 23
    elif random_10000 < 9958:
        p = 9
        d= 23
    elif random_10000 < 9964:
        p = 10
        d= 23
    elif random_10000 < 9968:
        p = 11
        d= 23
    elif random_10000 < 9970:
        p = 12
        d= 23
    else :
        p = 23
        d= 23
    list_space.append(space)
    list_p.append(p)
    list_d.append(d)
pdframe = pd.DataFrame()
pdframe['delivertime'] = list_d
pdframe['pickuptime'] = list_p
pdframe['space'] = list_space
pdframe.to_csv('deliverpickuptime.csv')


#####Task2
##Assume if parcel size <= 3 ft^3 it's small parcel
##Assume if parcel size >3 <=8 it's mid parcels
##Assume if parcel size >8 it's large parcel
####Large locker can save large parcel
####mid locker can save mid parcel
####small locker can save small parcel

import random
from collections import defaultdict

def initialize_lockers(num_small, num_medium, num_large):
## Initialize lockers with given numbers for each size. """
#list [status,till time when]
    return {
        'small': [['free',0] for _ in range(num_small)],
        'medium': [['free',0] for _ in range(num_medium)],
        'large': [['free',0] for _ in range(num_large)]
    }
def lockers_afteroneday(lockers):
## Initialize lockers with given numbers for each size. """
#list [status,till time when]
    for i in range(len(lockers['small'])):
        lockers['small'][i][1] = lockers['small'][i][1] - 24
    for n in range(len(lockers['medium'])):
        lockers['medium'][n][1] = lockers['medium'][n][1] - 24
    for p in range(len(lockers['large'])):
        lockers['large'][p][1] = lockers['large'][p][1] - 24
    return lockers

def generate_parcel(deliverytime, pickuptime,size):
##      Generate random parcel sizes based on the given distribution.
    if deliverytime > pickuptime:
        pickuptime = pickuptime + 24
    if size <= 3:
        list_parcel = [deliverytime,pickuptime, 'small']
        return list_parcel
    elif size <= 8:
        list_parcel = [deliverytime,pickuptime, 'medium']
        return  list_parcel
    else:
        list_parcel = [deliverytime,pickuptime, 'large']
        return list_parcel

def assign_parcels_to_lockers(parcel, lockers):
###    Assign parcels to lockers based on size and availability. """
### assignmentstatus means if assignment is successfull, if not, the value is 0
    assignmentstatus = 'unsuccessful assignment'
    lockfreetime = 0
    for i in range(len(lockers[parcel[2]])):

        lockerstate = lockers[parcel[2]][i][0]
        occupiedtime = lockers[parcel[2]][i][1]
        if lockerstate == 'free':
            lockers[parcel[2]][i] = ['occupied',parcel[1]]
            assignmentstatus = 'successful assignment'
            break

        elif lockerstate == 'occupied' and occupiedtime < parcel[0]:
            lockers[parcel[2]][i] = ['occupied',parcel[1]]
            assignmentstatus = 'successful assignment'
            lockfreetime = parcel[0] - occupiedtime
            break


    return lockers,assignmentstatus,lockfreetime

# Simulation parameters
num_small_lockers = 20
num_medium_lockers = 20
num_large_lockers = 20

num_lockers = num_small_lockers+num_medium_lockers+num_large_lockers

# Initialize lockers
lockers = initialize_lockers(num_small_lockers, num_medium_lockers, num_large_lockers)

# Generate parcel sizes
parcels = generate_parcel(1,7,8)
parcelss = generate_parcel(8,12,8)

# Assign parcels to lockers

#####Task3
#####put data in task 1 into task2's simulator
#####use num_successful_assignment_all to count for successful assignment
list_yearly_performance = []
list_yearly_utilization = []
list_daily_performance = []
list_daily_utilization = []
for each_year_demand in list_fiveyear_day_demand:

    num_successful_assignment_all = 0
    locker_all_freetime = 0
    newdemand = 0
    for demand in each_year_demand:
        num_successful_assignment_day = 0
        locker_daily_freetime = 0
        for i in range(newdemand,newdemand + demand):
            parcels = generate_parcel(list_d[i],list_p[i],list_space[i])
            updated_lockers,assignmentstatus,lockfreetime = assign_parcels_to_lockers(parcels, lockers)

            locker_daily_freetime += lockfreetime
            if assignmentstatus == "successful assignment":
                num_successful_assignment_day += 1

            # print("\nnew pacel:")
            # print(parcels)
            # print("\nUpdated locker status:")
            # for size, locker_status in updated_lockers.items():
            #     print(f"{size.capitalize()} lockers:", locker_status)

        lockers = lockers_afteroneday(lockers)
        list_daily_performance.append(num_successful_assignment_day/demand)
        list_daily_utilization.append(locker_daily_freetime/(num_lockers*24))
        num_successful_assignment_all += num_successful_assignment_day
        locker_all_freetime += locker_daily_freetime
        newdemand += demand

    # print("\none new day!!")
    ##each year's demand accept rate
    demand_accept_rate = num_successful_assignment_all/newdemand
    demand_reject_rate = 1 - demand_accept_rate
    yearly_utilization = locker_all_freetime/(24*num_lockers*365)
    list_yearly_performance.append(demand_accept_rate)
    list_yearly_utilization.append(yearly_utilization)
general_performance = sum(list_yearly_performance)/5
general_utilization = sum(list_yearly_utilization)/5

performanceframe = pd.DataFrame()
performanceframe['dailyperformance'] = list_daily_performance
performanceframe['dailyutilization'] = list_daily_utilization

performanceframe.to_csv('systemperformancedaily.csv')

performanceyearlyframe = pd.DataFrame()
performanceyearlyframe['yearlyperformance'] = list_yearly_performance
performanceyearlyframe['yearlyutilization'] = list_yearly_utilization

performanceyearlyframe.to_csv('systemperformanceyearly.csv')

print("general performance is:")
print(general_performance)
print("general_utilization is:")
print(general_utilization)

##Task4 design the locker_

num_grid = 60
num_grip_usedas_interactive = 7
rate_3type = [0.35,0.36,0.29]
real_rate_3type = [rate_3type[0]*3, rate_3type[1]*8, rate_3type[2]*18]
total = sum(real_rate_3type)
num_small = (num_grid- num_grip_usedas_interactive)*(real_rate_3type[0]/total)
num_medium = (num_grid- num_grip_usedas_interactive)*(real_rate_3type[1]/total)
num_large = (num_grid- num_grip_usedas_interactive)*(real_rate_3type[2]/total)

print(num_small)
print(num_medium)
print(num_large)




    ##11
