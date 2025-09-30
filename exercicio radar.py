velocidade = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_carro_passou_radar_1 = velocidade > RADAR_1
#sempre optar por variaveis com nomes descritivos
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
      local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        vel_carro_passou_radar_1

if vel_carro_passou_radar_1:
    print ("velocidade acima do permitido no radar 1")

if carro_multado_radar_1:
    print ("carro multado no radar 1")