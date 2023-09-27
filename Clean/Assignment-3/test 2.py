clients = { "John": 20000, "Mary": 50000, "Lars": 100, "Hannah": 100500, "Lukas": 200040, }

def some_class (clients):
    tup_list = (clients.items())

    final_dict = {"Google": [], "Microsoft": [], "Techworld": [], "MLsolutions": []} 
 
    for i in clients:
        if clients[i] <= 100000 and i != "Lars":
            clients[i] = clients[i]/2
            k = i, clients[i]
            final_dict["Google"].append(k) 
            final_dict["Microsoft"].append(k) 
        else:
            clients[i] = clients[i]*0.4
            k = i, clients[i]
            final_dict["Google"].append(k) 
            final_dict["Microsoft"].append(k)
            clients[i] = clients[i]/4
            k = i, clients[i]
            final_dict["Techworld"].append(k) 
            final_dict["MLsolutions"].append(k)

    print(final_dict)

            



some_class(clients)
