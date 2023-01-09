from collections import defaultdict
visited =defaultdict(lambda:False)

j1,j2,l=0,0,0

def water(x,y):
    global j1,j2,l
    if(x==l and y==0) or (y==l and x==0):
        print("(",x,',',y,')')
        return True
        
    if visited[(x,y)]==False:
              print('(',x,',',y,')')       


              visited[(x,y)]=True

              return(water(0,y)or
                    water(x,0) or 
                    water(j1,y) or 
                    water(x,j2) or 
                    water(x+min(y,(j1-x)),y-min(y,(j1-x))) or
                    water(x-min(x,(j2-y)),y+min(x,(j2-y))))

    else :
        return False



j1 =5
j2 =3
l =4
print("path is as follow:")
water(0,0)