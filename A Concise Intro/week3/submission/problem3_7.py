def problem3_7(csv_pricefile, flower):

    import csv

    f = open(csv_pricefile)

    for row in csv.reader(f):

        if flower == row[0]:

            print(row[1])

    f.close()

