class CliInterface:
    def render_departures(self, departures):
        for departure in departures:
            print(f"Time: {departure['time']}\t Direction: {departure['direction']}")