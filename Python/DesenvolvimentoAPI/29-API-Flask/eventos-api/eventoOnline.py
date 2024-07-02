from evento import Evento

class EventoOnline (Evento):
    id = 0

    def __init__(self, nome, local):
        EventoOnline.id += 1

        localId = local + str(EventoOnline.id)

        super().__init__(nome, localId)

        self._id = EventoOnline.id
