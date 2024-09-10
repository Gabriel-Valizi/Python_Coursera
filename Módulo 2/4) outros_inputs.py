segs_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segs_str)

horas = total_segs // 3600 # divisão inteira
segs_restantes = total_segs % 3600 # resto da divisão

minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(horas, "horas, ", minutos, "minutos e", segs_restantes_final, "segundos.")