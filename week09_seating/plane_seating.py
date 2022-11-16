import random
def create_plane(rows,cols):
   
    plane = []
    for r in range(rows):
        s = ["win"]+["avail"]*(cols-2)+["win"]
        plane.append(s)
    return plane

def get_number_economy_sold(economy_sold):
    
    sold = 0
    for v in economy_sold.values():
        sold = sold + v
    return sold
  
def get_avail_seats(plane,economy_sold):
    
    avail = 0;
    for r in plane:
        for c in r:
            if c == "avail" or c == "win":
                avail = avail + 1
    avail = avail - get_number_economy_sold(economy_sold)
    return avail

def get_total_seats(plane):
    
    return len(plane)*len(plane[0])

def get_plane_string(plane):
    
    s = ""
    for r in plane:
        r = ["%14s"%x for x in r] 
        s = s + " ".join(r)
        s = s + "\n"
    return s
  
def purchase_economy_plus(plane,economy_sold,name):
    
    rows = len(plane)
    cols = len(plane[0])  
    seats = get_avail_seats(plane,economy_sold)

    if seats < 1:
        return plane
      
    if random.randrange(100) > 30:
        order = [x for x in range(rows)]

        random.shuffle(order)
   
        for row in order:
            if plane[row][0] == "win":
                plane[row][0] = name
                return plane
            elif plane[row][len(plane[0])-1] == "win":
                plane[row][len(plane[0])-1] = name
                return  plane

    found_seat = False
    while not(found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
            plane[r_row][r_col] = name
            found_seat = True
    return plane

def seat_economy(plane,economy_sold,name):
    
    rows =len(plane)
    cols=len(plane[0])


    #The code from 79-96 is what I developed in an attempt to accomplish my goal of if the value for any key:value pair was 2 or 3, take the key associated with the value and assign it to name. I wanted to keep it simple by with the logic being if an item in the dictionary is u-1 : 2, or u-4 : 3; if val_list.index(2) and plane row (i) and cols(i and i+1) was available then "name" should equal the key of that index. After failing multiple times, lines 143-149 were just experiments to test that the statements produced what I predicted. I did realize that "position = val_list.index(3)" and "position2 = val_list.index(2)" only referenced the first find of that value. I feel like with more time I would have eventually figured it out. I did learn a lot about dictionaries and key:pair relationships.

  
    '''
    key_list = list(economy_sold.keys())
    val_list = list(economy_sold.values())
 
    for i in range(rows):
      for j in range(cols-1):
        if val_list.index(2) and plane[i][j]=="avail" and plane[i][j+1]=="avail":
               name = key_list[val_list.index(2)]
               plane[i][j]= name
               plane[i][j+1]= name
              
                       
    for i in range(rows):
      for j in range(cols-2):
        if val_list.index(3) and plane[i][j]=="avail" and plane[i][j+1]=="avail" and plane[i][j+2]=="avail":
               name = key_list[val_list.index(3)]
               plane[i][j]= name
               plane[i][j+1]=name
               plane[i][j+2]=name
      '''        

    found_seat = False
    while not (found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
              plane[r_row][r_col] = name
              found_seat = True
   
    return plane

def purchase_economy_block(plane,economy_sold,number,name):
    
    seats_avail = get_total_seats(plane)
    seats_avail = seats_avail - get_number_economy_sold(economy_sold)

    if seats_avail >= number:
        economy_sold[name]=number
    return economy_sold

def fill_plane(plane):
    
    economy_sold={}
    total_seats = get_total_seats(plane)
    
    ep_number=1
    u_number=1

    max_family_size = 3
    while total_seats > 1:
        r = random.randrange(100)
        if r > 30:
            plane = purchase_economy_plus(plane,economy_sold,"ep-%d"%ep_number)
            ep_number = ep_number + 1
            total_seats = get_avail_seats(plane,economy_sold)
        else:
            economy_sold = purchase_economy_block(plane,economy_sold,1+random.randrange(max_family_size),"u-%d"%u_number)
            u_number = u_number + 1

        
    for name in economy_sold.keys():
        for i in range(economy_sold[name]):
          plane = seat_economy(plane,economy_sold,name)
    
    ''' 
    print(economy_sold)
    key_list = list(economy_sold.keys())
    val_list = list(economy_sold.values())
    position = val_list.index(3)
    print(key_list[position])
    position2 = val_list.index(2)
    print(key_list[position2])
    '''   
    return plane
        
def main():
    plane = create_plane(10,5)
    plane = fill_plane(plane)
    print(get_plane_string(plane))
if __name__=="__main__":
    main()
