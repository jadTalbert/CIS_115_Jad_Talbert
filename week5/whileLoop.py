#this program demonstrates a while look for sales commissions

keep_going = "y"

#calculate a series of commissions
while keep_going == "y":
    sales = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter the commission rate: "))

    #calculate the commission
    commission = sales * comm_rate

    print(f"The commission is ${commission:,.2f}")

    keep_going = input("Do you want to calculate another commission(Enter y for yes): ")

