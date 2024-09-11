segs_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segs_str)

dias = total_segs // 86400
segs_restantes1 = total_segs % 86400

horas = segs_restantes1 // 3600 # divisão inteira
segs_restantes2 = segs_restantes1 % 3600 # resto da divisão

minutos = segs_restantes2 // 60
segs_restantes_final = segs_restantes2 % 60

print(dias, "dias, ", horas, "horas, ", minutos, "minutos e", segs_restantes_final, "segundos.")