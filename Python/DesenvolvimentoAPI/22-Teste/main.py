from timeFutebol import TimeFutebol

time = TimeFutebol("Vasco", "Brasil")
time.derrotas = 10
time.vitorias = 11
print(time.analisaSituacao(time.vitorias, time.derrotas))
print(time.toString())
time.ganhar()
time.perder()
time.perder()
print(time.toString())
print(time.analisaSituacao(time.vitorias, time.derrotas))