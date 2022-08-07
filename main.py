import pandas

data = pandas.read_csv('Gas_stations_Zagreb.csv')
all_data = data.NAZIV.to_list()

click_is_on = True
while click_is_on:
    test = input('Choose preferred gas station company: [INA/TIFON/PETROL/CRODUX/LUKOIL/ADRIA OIL] ').upper()
    if test in all_data:
        test_data = data[data.NAZIV == test]
        print(f'{test} gas station addresses in Zagreb: \n', test_data.ADRESA)
        click_checker = input("Do you want to search for other gas stations? [y/n] ").lower()
        if click_checker == 'n':
            click_is_on = False





