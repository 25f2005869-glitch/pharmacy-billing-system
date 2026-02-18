shopvisit= int(input("No. of visits"))
point=0
for i in range(1,shopvisit+1):
    print("\n\nshopvisit",i)
    total = 0
    medt=int(input("Enter how many types of medicines customer wants to purchase "))
    medqbill = medt
    if medt > 0:
        for j in range(1,medt+1):
            print("medicine type",j)
            medq=int(input(f"Enter medicine type{j} quantity "))
            if medq > 0:
                medc=float(input(f"Enter medicine type{j} cost "))
                perMediTotal = medq*medc
                total += perMediTotal
            else:
                print(f"Wrong Input: Quantity entered for type{j} medicine is zero")
                medqbill -= 1
        curpoint=total//100
        if medqbill > 0:
            print("Bill is in",i,"visit",total)
            print("points earned in",i,"visit",curpoint)
            if i==1:
                point=curpoint
            elif(i>1):
                if(point>=10):
                    pointvalue=point*25
                    print("If customer want to redeem his points")
                    ans=input("Enter y/n: ")
                    if(ans=="Y") or (ans=="y"):
                        print("Stored points are ", point, "and their value is",pointvalue)
                        print(f"According to your current bill maximum redeemable points are {total//25} and their value is {25*(total//25)}")
                        if(total//25) > 0:
                            redpoint=int(input("How many points you want to redeem "))
                            if(redpoint<=point):
                                dis=redpoint*25
                                if(dis <= total):
                                    FB=total-dis
                                    point-=redpoint
                                    point+=curpoint
                                    print("Total Bill with redeeming",redpoint,"points",FB)
                                else:
                                    print("Discount is more than total, redeeming not possible")
                                    point+=curpoint
                            else:
                                print("Wrong Input: Redeem points given are greater than points")
                                point+=curpoint
                        else:
                            print("No points to redeem")
                            point+=curpoint
                    else:
                        print("Total Bill without redeeming is",total)
                        point=curpoint+point
                else:
                    FB=total
                    point=point+curpoint
                    print("Total Bill when redeeming not possible ",FB)
            else:
                print("Stored point are not sufficient to redeem")
                point=point+curpoint
            print("Total points from last visit purchase",point)
        else:
            print("No bill generated since user didn't purchase anything")
    else:
        print("Wrong Input: Number of medicine to be purchase are given zero")
