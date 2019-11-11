B532="""
{
    bikeRentalStation(id: "532") {
        name
        bikesAvailable
        spacesAvailable
        allowDropoff
    }
}
"""
B533="""
{
    bikeRentalStation(id: "533") {
        name
        bikesAvailable
        spacesAvailable
        allowDropoff
    }
}
"""
B541="""
{
    bikeRentalStation(id: "541") {
        name
        bikesAvailable
        spacesAvailable
        allowDropoff
    }
}
"""
B539="""
{
    bikeRentalStation(id: "539") {
        name
        bikesAvailable
        spacesAvailable
        allowDropoff
    }
}
"""
B545="""
{
    bikeRentalStation(id: "545") {
        name
        bikesAvailable
        spacesAvailable
        allowDropoff
    }
}
"""
B547="""
{
    bikeRentalStation(id: "547") {
        name
        bikesAvailable
        spacesAvailable
        allowDropoff
    }
}
"""
LST=[B532,B533,B539,B541,B545,B547]

S1="""
{
  stop(id: "HSL:2222214") {
    name
      stoptimesWithoutPatterns {
      scheduledArrival
      realtimeArrival
      arrivalDelay
      scheduledDeparture
      realtimeDeparture
      departureDelay
      realtime
      realtimeState
      serviceDay
      headsign
      trip{
        directionId
        route{
          shortName
          mode
        }
      }
    }
  }  
}
"""
S2="""
{
  stop(id: "HSL:2222234") {
    name
      stoptimesWithoutPatterns {
      scheduledArrival
      realtimeArrival
      arrivalDelay
      scheduledDeparture
      realtimeDeparture
      departureDelay
      realtime
      realtimeState
      serviceDay
      headsign
      trip{
        directionId
        route{
          shortName
          mode
        }
      }
    }
  }  
}
"""