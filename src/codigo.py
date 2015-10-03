######################
#Nuno Mendes, 73716
#Ricardo Simas, 72769
#IASD - Projecto 1
#Outubro 2015
######################

client = open('input2.cli') #open .cli file
client_line=client.readline() #read the first line from the .cli file
number_clients=client_line.split() #the first line tells how many clients exist
C=number_clients[0]
C=int(C) #the number of clients is now an integer

#legend:

#city_map_words[0] -> departure city
#city_map_words[1] -> arrival city
#city_map_words[2] -> type of transport
#city_map_words[3] -> time duration
#city_map_words[4] -> cost
#city_map_words[5] -> ti
#city_map_words[6] -> tf
#city_map_words[7] -> daily periodicity

#client_words[0] -> client's id. number
#client_words[1] -> departure city
#client_words[2] -> arrival city
#client_words[3] -> time instant after which the client is available to travel
#client_words[4] -> optimization criterion
#client_words[5] -> number of constraints
#client_words[6] and [7] -> constrains if they exist

while C>0: #while there are clients travelling, this program is running

#read each client's info
    client_line=client.readline()
    client_words=client_line.split()

    city_map = open('input1.map') #open .map file
    city_map_line=city_map.readline() #read the first line from the .map file
    number_cities_connections=city_map_line.split() #the first line tells how many cities and connections exist
    N=number_cities_connections[0]
    N=int(N) #the number of cities is now an integer
    L=number_cities_connections[1]
    L=int(L) #the number of connections is now an integer

    i=0
    map_line={}

    while L>0:
        #read each connection's info
        city_map_line=city_map.readline()
        city_map_words=city_map_line.split()
        if client_words[1]==city_map_words[0] and int(city_map_words[6])>=int(client_words[3]):
            #the departure cities in both files have to be equal and the
            #time instant after which the client is available to travel has to be
            #lower than the time instant after which there are no more departures (tf)
            map_line[i]=city_map_line
            #only the connections that respect these conditions are up to being used
            i+=1
        else:
            pass    
        L-=1

    print(map_line) #list of connections that can be used for each client

    total_time=0
    total_cost=0
    
    C-=1 #this client's journey has ended
