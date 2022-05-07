class CliInterface:
    def renderDepartures(self, departures):
        for departure in departures:
            print(f"Time: {departure['time']}\t Direction: {departure['direction']}")